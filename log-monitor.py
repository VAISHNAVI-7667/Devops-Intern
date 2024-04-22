import os
import time
import signal
import logging

# Configure logging
logging.basicConfig(filename='log_monitor.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Function to handle Ctrl+C signal for graceful exit
def signal_handler(signal, frame):
    print("\nExiting...")
    logging.info("Log monitoring stopped.")
    exit(0)

# Function to monitor log file for new entries
def monitor_log(log_file):
    logging.info(f"Start monitoring log file: {log_file}")
    print(f"Start monitoring log file: {log_file}")
    try:
        with open(log_file, 'r') as f:
            # Move to the end of the file
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if line:
                    print(line.strip())  # Display new log entry
                    logging.info(f"New log entry: {line.strip()}")
                time.sleep(0.1)  # Adjust sleep time as needed
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"Error: {e}")
        logging.error(f"Error: {e}")
    finally:
        logging.info("Stopped monitoring log file.")

# Function to analyze log file
def analyze_log(log_file):
    logging.info(f"Start analyzing log file: {log_file}")
    print(f"Start analyzing log file: {log_file}")
    try:
        with open(log_file, 'r') as f:
            lines = f.readlines()
            error_count = 0
            keyword_count = {}
            for line in lines:
                if "ERROR" in line:
                    error_count += 1
                # Add more keyword checks as needed
                # Example: if "HTTP" in line:
                #            keyword_count["HTTP"] = keyword_count.get("HTTP", 0) + 1
            print(f"Total Errors: {error_count}")
            logging.info(f"Total Errors: {error_count}")
            # Log more keyword counts if needed
    except Exception as e:
        print(f"Error: {e}")
        logging.error(f"Error: {e}")
    finally:
        logging.info("Finished analyzing log file.")

if _name_ == "_main_":
    # Handle Ctrl+C signal
    signal.signal(signal.SIGINT, signal_handler)

    log_file = "sample.log"  # Change to the path of your log file
    monitor_log(log_file)
    analyze_log(log_file)
