import os
from pathlib import Path

Path("output").mkdir(parents=True, exist_ok=True)
Path("input").mkdir(parents=True, exist_ok=True)
Path("input/subdir/more").mkdir(parents=True, exist_ok=True)

with open("input/this_was_in_input.txt", "w") as file:
    file.write("This file was created in the Input directory.")

with open("input/subdir/more/this_was_in_input.txt", "w") as file:
    file.write("This file was created in the Input/subdir/more/ directory.")

with open("output/new_output.txt", "w") as file:
    file.write("This file was created in the out directory.")

os.system("cp input/this_was_in_input.txt output/copied_from_input.txt")
os.system("cp input/subdir/more/this_was_in_input.txt output/copied_from_input_subdir.txt")
