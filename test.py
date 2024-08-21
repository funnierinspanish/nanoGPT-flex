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
        # list files in the /input directory
        print("//////////////////////////////////////////")
        logging.info("Files in the /input directory:")
        for file in Path('/input').rglob('*'):
            if file.is_file():
                print(file)
    except Exception as e:
        logging.error(f"Error listing files in /input directory: {e}")

    try:
        with open("/output/this_was_in_root.bin", "w") as file:
            file.write("This file was created in the root directory.")
            logging.info("Created /out/this_was_in_root.bin")
    except Exception as e:
        logging.error(f"Error listing files in /output directory: {e}")

    
    try:
        # list files in the models directory
        print("//////////////////////////////////////////")
        logging.info("Files in the models directory:")
        for file in Path('models').rglob('*'):
            if file.is_file():
                print(file)
    except Exception as e:
        logging.error(f"Error listing files in models directory: {e}")

    try:
        # list files in the input directory
        print("//////////////////////////////////////////")
        logging.info("Files in the input directory:")
        for file in Path('input').rglob('*'):
            if file.is_file():
                print(file)
    except Exception as e:
        logging.error(f"Error listing files in input directory: {e}")


    try:
        with open("/output/anotherbin.bin", "w") as file:
            file.write("lorem ipsum dolor sit amet consectetur adipiscing elit lorem ipsum dolor sit amet consectetur adipiscing elit lorem ipsum dolor sit amet consectetur adipiscing elit lorem ipsum dolor sit amet consectetur adipiscing elit lorem ipsum dolor sit amet consectetur adipiscing elitlorem ipsum dolor sit amet consectetur adipiscing elitlorem ipsum dolor sit amet consectetur adipiscing elitlorem ipsum dolor sit amet consectetur adipiscing elitlorem ipsum dolor sit amet consectetur adipiscing elitlorem ipsum dolor sit amet consectetur adipiscing elitlorem ipsum dolor sit amet consectetur adipiscing elitlorem ipsum dolor sit amet consectetur adipiscing elitlorem ipsum dolor sit amet consectetur adipiscing elitlorem ipsum dolor sit amet consectetur adipiscing elitlorem ipsum dolor sit amet consectetur adipiscing elit." )
            logging.info("Created /out/anotherbin.bin")
    except Exception as e:
        logging.error(f"Error listing files in /output directory: {e}")


    try:
        # list files in the /output directory
        print("//////////////////////////////////////////")
        logging.info("Files in the /output directory:")
        for file in Path('/output').rglob('*'):
            if file.is_file():
                print(file)
    except Exception as e:
        logging.error(f"Error listing files in /output directory: {e}")


print("init")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Example logs

print("/-----------------------------------------------")
main()
print("-----------------------------------------------/")
sys.exit(0)