import sys
import pathlib
import datetime

class Logger:
    """Redirects print output to both terminal and a log file."""
    banner = r"""
#####################################################################################################
##     __  __                                      ____              __     __     _____           ##
##    / / / /  ____     ____     ___     __  __   / __ \   ____     / /_   / /_   |__  /   _____   ##
##   / /_/ /  / __ \   / __ \   / _ \   / / / /  / /_/ /  / __ \   / __/  / __/    /_ <   / ___/   ##
##  / __  /  / /_/ /  / / / /  /  __/  / /_/ /  / ____/  / /_/ /  / /_   / /_    ___/ /  / /       ## 
## /_/ /_/   \____/  /_/ /_/   \___/   \__, /  /_/       \____/   \__/   \__/   /____/  /_/        ##
##                                    /____/                                                       ## 
#####################################################################################################                                
"""

    def __init__(self):
        log_dir = pathlib.Path(__file__).resolve().parent.parent / "logs"  
        log_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.log_file = log_dir / f"ScanResult_{timestamp}.log"

        self.terminal = sys.stdout
        self.log = self.log_file.open("w", encoding="utf-8")
        self.logging_enabled = False  # Start with logging disabled

    def start_logging(self):
        """Starts logging to the log file and writes the banner."""
        if not self.logging_enabled:
            self.log.write(self.banner + "\n\n")  # Write the banner at the top
            self.log.flush()
            self.logging_enabled = True
        sys.stdout = self  # Redirect stdout

    def write(self, message):
        self.terminal.write(message)
        self.terminal.flush()
        if self.logging_enabled:
            self.log.write(message)
            self.log.flush()

    def flush(self):
        self.terminal.flush()
        if self.logging_enabled:
            self.log.flush()

    def stop_logging(self):
        """Stops writing to the log file but continues printing to the terminal."""
        sys.stdout = self.terminal  # Restore normal stdout
        self.logging_enabled = False
        self.log.close()
