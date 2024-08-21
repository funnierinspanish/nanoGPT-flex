import os
from pathlib import Path
import logging

# Example logs
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
print("This is a regular print statement")

# Check if the output directory exists
if Path("output").exists():
    logging.debug("Output directory exists")
else:
    try:
        Path("output").mkdir(parents=True, exist_ok=True)
        logging.debug("Created output/")
    except Exception as e:
        logging.error(f"Error creating output directory: {e}")

# # Check if the root directory exists
# if Path("input").exists():
#     print("root directory exists")
# else:
#     Path("input").mkdir(parents=True, exist_ok=True)
#     print("Created ")


Path("subdir/more").mkdir(parents=True, exist_ok=True)
logging.debug("Created subdir/more/")

with open("this_was_in_root.txt", "w") as file:
    file.write("This file was created in the root directory.")
    logging.debug("Created this_was_in_root.txt")

with open("subdir/more/this_was_in_root.txt", "w") as file:
    file.write("This file was created in the subdir/more/ directory.")
    logging.debug("Created subdir/more/this_was_in_root.txt")

with open("output/new_output.txt", "w") as file:
    file.write("This file was created in the out directory.")
    logging.debug("Created output/new_output.txt")

os.system("cp this_was_in_root.txt output/copied_from_root.txt")
logging.debug("Copied this_was_in_root.txt to output/copied_from_root.txt")
os.system("cp subdir/more/this_was_in_root.txt output/copied_from_root_subdir.txt")
logging.debug("Copied subdir/more/this_was_in_root.txt to output/copied_from_root_subdir.txt")