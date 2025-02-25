import os
import pymongo
import gridfs
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../configs/.env'))

class mongoLoader:
    def __init__(self):
        """Initialize MongoDB connection and GridFS."""
        mongo_uri = os.getenv('MONGO_URI')
        if not mongo_uri:
            raise ValueError("MONGO_URI is not set in the .env file")

        self.db_name = "honeypott3r"
        self.collection_name = "scan_results"

        # Set up MongoDB client
        self.client = pymongo.MongoClient(mongo_uri)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]
        self.fs = gridfs.GridFS(self.db)  # Initialize GridFS

    def upload(self, report_data: dict, log_file: str):
        """
        Uploads the report data and its associated log file in a single MongoDB document.
        
        Args:
            report_data (dict): The structured report data.
            log_file (str): The name of the log file to upload (from /src/logs/).
        """
        try:
            log_path = os.path.join(os.path.dirname(__file__), '../logs', log_file)
            print(f"log file found: {log_path}")

            # Upload log file to GridFS
            with open(log_path, "rb") as file_data:
                log_file_id = self.fs.put(file_data, filename=log_file)

            # Attach the log file ID to the report data
            report_data["log_file_id"] = log_file_id  

            # Insert report with log file reference into scan_results
            self.collection.insert_one(report_data)

            print(f"Report and log file uploaded successfully! Log ID: {log_file_id}")

        except Exception as e:
            print(f"Error uploading report and log file: {e}")

    def get_logfile(self, log_file_id, output_path=None):
        """
        Retrieves the log file from GridFS using the log_file_id.
        
        Args:
            log_file_id (str or ObjectId): The GridFS file ID to fetch.
            output_path (str, optional): Path to save the file. If None, returns the file content.
        
        Returns:
            str: File content as a string if output_path is None, else saves the file.
        """
        try:
            from bson import ObjectId  # Import inside function to avoid global dependency
            
            # Ensure log_file_id is an ObjectId
            if isinstance(log_file_id, str):
                log_file_id = ObjectId(log_file_id)

            # Fetch the file from GridFS
            log_file = self.fs.get(log_file_id)
            
            if output_path:
                with open(output_path, "wb") as f:
                    f.write(log_file.read())
                print(f"Log file saved to: {output_path}")
            else:
                return log_file.read().decode("utf-8")  # Return as string if no path is given

        except Exception as e:
            print(f"Error retrieving log file: {e}")
            return None