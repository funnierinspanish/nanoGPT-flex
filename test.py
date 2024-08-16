import os
from pathlib import Path

# Check if the output directory exists
if Path("output").exists():
    print("Output directory exists")
else:
    Path("output").mkdir(parents=True, exist_ok=True)
    print("Created output/")

# Check if the input directory exists
if Path("input").exists():
    print("Input directory exists")
else:
    Path("input").mkdir(parents=True, exist_ok=True)
    print("Created input/")


Path("input/subdir/more").mkdir(parents=True, exist_ok=True)
print("Created input/subdir/more/")

with open("input/this_was_in_input.txt", "w") as file:
    file.write("This file was created in the Input directory.")
    print("Created input/this_was_in_input.txt")

with open("input/subdir/more/this_was_in_input.txt", "w") as file:
    file.write("This file was created in the Input/subdir/more/ directory.")
    print("Created input/subdir/more/this_was_in_input.txt")

with open("output/new_output.txt", "w") as file:
    file.write("This file was created in the out directory.")
    print("Created output/new_output.txt")

os.system("cp input/this_was_in_input.txt output/copied_from_input.txt")
print("Copied input/this_was_in_input.txt to output/copied_from_input.txt")
os.system("cp input/subdir/more/this_was_in_input.txt output/copied_from_input_subdir.txt")
print("Copied input/subdir/more/this_was_in_input.txt to output/copied_from_input_subdir.txt")