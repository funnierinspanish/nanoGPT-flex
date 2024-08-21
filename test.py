import sys
import os
import logging
from pathlib import Path



def main():

    # Check if the output directory exists
    if Path("output").exists():
        logging.info("output directory exists")
    else:
        logging.error("No output/ directory found....")

    # Check if the input directory exists
    if Path("input").exists():
        logging.info("input directory exists")
        logging.info("//////////////////////////////////////////")
        logging.info("Files in the input directory:")
        for file in os.listdir('output'):
            logging.info(file)
    else:
        logging.error("No input/ directory found....")

    try:
        Path("subdir").mkdir(parents=True, exist_ok=True)
        logging.info("Created subdir/")
        Path("subdir/more").mkdir(parents=True, exist_ok=True)
        logging.info("Created subdir/more/")

        with open("this_was_in_root.txt", "w") as file:
            file.write("This file was created in the root directory.")
            logging.info("Created this_was_in_root.txt")

        with open("subdir/more/this_was_in_root.txt", "w") as file:
            file.write("This file was created in the subdir/more/ directory.")
            logging.info("Created subdir/more/this_was_in_root.txt")

        with open("output/new_output.txt", "w") as file:
            file.write("This file was created in the out directory.")
            logging.info("Created output/new_output.txt")

        os.system("cp this_was_in_root.txt output/copied_from_root.txt")
        logging.info("Copied this_was_in_root.txt to output/copied_from_root.txt")
        os.system("cp subdir/more/this_was_in_root.txt output/copied_from_root_subdir.txt")
        logging.info("Copied subdir/more/this_was_in_root.txt to output/copied_from_root_subdir.txt")
        
        os.system("cp shakespeare_char/val.bin output/the_val.bin")
        logging.info("Copied shakespeare_char/val.bin to output/the_val.bin")

        os.system("cp shakespeare_char/train.bin output/the_train.bin")
        logging.info("Copied shakespeare_char/val.bin to output/the_val.bin")

        try:
            # list files in the root directory
            print("//////////////////////////////////////////")
            logging.info("Files in the output directory:")
            for file in os.listdir('output'):
                logging.info(file)
        except Exception as e:
            logging.error(f"Error listing files in root directory: {e}")
            sys.exit(1)

        try:
            # list files in the root directory
            print("//////////////////////////////////////////")
            logging.info("Files in the root directory:")
            for file in os.listdir():
                logging.info(file)
        except Exception as e:
            logging.error(f"Error listing files in root directory: {e}")
            sys.exit(1)

    except Exception as e:
        logging.error(f"Error with files operations: {e}") 
        sys.exit(1)

print("init")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Example logs
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
print("This is a regular print statement")
print("-----------------------------------------------")
main()
print("-----------------------------------------------/")
sys.exit(0)