import os
import shutil

path = input("Add your path:")
original_locations = {}

for file in os.listdir(path):
    if file.endswith(".py"):
        continue # ignore .py files

    if os.path.isdir(os.path.join(path, file)):
        continue # ignore directories

    if file.endswith(".lnk"):
        continue # ignore shortcuts

    file_type = file.split(".")[-1].lower()
    if file_type not in os.listdir(path):
        os.mkdir(os.path.join(path, file_type))

    destination = os.path.join(path, file_type, file)
    if os.path.exists(destination):
        os.remove(destination)

    shutil.move(os.path.join(path, file), destination)
    print(f"Moved {file} to {destination}")
    original_locations[file] = file_type + "/" + file

choice = input("Enter 1 to keep files organized or 2 to move files back to their original location: ")

if choice == "2":
    for file, relative_path in original_locations.items():
        original_location = os.path.join(path, relative_path)
        destination = os.path.join(path, file)

        if os.path.exists(destination):
            os.remove(destination)

        shutil.move(original_location, destination)
        print(f"Moved {file} back to {destination}")

    print("Files have been moved back to original directory.")
