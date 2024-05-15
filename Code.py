import os
import shutil

downloads_folder_path = os.path.expanduser("~/Downloads")

for file in os.listdir(downloads_folder_path):
    if os.path.isfile(os.path.join(downloads_folder_path, file)):
        filename, file_extension = os.path.splitext(file)
        folder_to_organize_file = os.path.join(downloads_folder_path, file_extension[1:])

        if not os.path.isdir(folder_to_organize_file):
            os.mkdir(folder_to_organize_file)

        shutil.move(os.path.join(downloads_folder_path, file), os.path.join(folder_to_organize_file, file))
