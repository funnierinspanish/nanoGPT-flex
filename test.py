import sys
import os
import logging
from pathlib import Path
import time



def main():
    # Starting the script
    time.sleep(1)
    logging.info("Starting.........")
    time.sleep(2)
    logging.info("...........................")
    time.sleep(3)
    logging.info("...........................................")
    time.sleep(1)

    logging.info("Started!")

    try:
        # list files in the root directory
        print("//////////////////////////////////////////")
        logging.info("Files in the /input directory:")
        for file in os.listdir('/input'):
            logging.info(file)
    except Exception as e:
        logging.error(f"Error listing files in /input directory: {e}")

    try:
        # list files in the root directory
        print("//////////////////////////////////////////")
        logging.info("Files in the /output directory:")
        for file in os.listdir('/output'):
            logging.info(file)
        with open("/output/this_was_in_root.bin", "w") as file:
            file.write("This file was created in the root directory.")
            logging.info("Created this_was_in_root.txt")
    except Exception as e:
        logging.error(f"Error listing files in /output directory: {e}")

    
    try:
        # list files in the root directory
        print("//////////////////////////////////////////")
        logging.info("Files in the /models directory:")
        for file in os.listdir('/models'):
            logging.info(file)
    except Exception as e:
        logging.error(f"Error listing files in /models directory: {e}")


print("init")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Example logs

print("/-----------------------------------------------")
main()
print("-----------------------------------------------/")
sys.exit(0)