import os
import pymongo
from dotenv import load_dotenv

# Load environment variables from .env file located in /src/configs
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../configs/.env'))

class mongoLoader:
    def __init__(self):
        """
        Initializes the MongoLoader object by reading the MongoDB URI from the .env file
        and connecting to the specified database and collection.
        """
        # Load the MongoDB URI from environment variables
        mongo_uri = os.getenv('MONGO_URI')

        if not mongo_uri:
            raise ValueError("MONGO_URI is not set in the .env file")

        self.db_name = "honeypott3r"  # Database name
        self.collection_name = "scan_results"  # Collection name
        
        # Set up the MongoDB client
        self.client = pymongo.MongoClient(mongo_uri)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]

    def upload(self, report_data: dict):
        """
        Uploads the given report data to MongoDB.

        Args:
            report_data (dict): The report data to be uploaded to the database.
        """
        try:
            # Insert the report data into the MongoDB collection
            self.collection.insert_one(report_data)
            print("Report data successfully uploaded to MongoDB!")
        except Exception as e:
            print(f"Error uploading report data: {e}")
