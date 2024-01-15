# Import modules for interacting with the operating system.
import os
import datetime

directory = r"" # Add your directory here.

# Get current name and time
now = datetime.datetime.now()
current_date = now.strftime("%m-%d-%Y")

# Define a dictionary of old and new file names
replacement_file_names = {} # Add the files you need renamed here.


# Loop for iterative renaming
# 

renamed_files = []
for filename in os.listdir(directory):
    if filename in replacement_file_names.keys():
        old_name = os.path.join(directory, filename)
        new_name = os.path.join(directory, replacement_file_names[filename])
        os.rename(old_name, new_name)
        renamed_files.append(f"{filename} -> {replacement_file_names[filename]}")

print("The following files have been renamed: ")
print("\n".join(renamed_files))        
