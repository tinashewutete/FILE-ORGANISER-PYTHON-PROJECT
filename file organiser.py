import tkinter as tk
from tkinter import filedialog
import os
import shutil

def select_folder():
    root = tk.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected

target_directory = select_folder()

# Define a mapping of extensions to folder names
extension_mapping = {
    'jpg': 'Images', 'jpeg': 'Images', 'png': 'Images', 'gif': 'Images', 'bmp': 'Images',
    'mp4': 'Videos', 'avi': 'Videos', 'mov': 'Videos', 'mkv': 'Videos',
    'mp3': 'Music', 'wav': 'Music', 'flac': 'Music',
    'pdf': 'Documents', 'doc': 'Documents', 'docx': 'Documents', 'txt': 'Documents', 'rtf': 'Documents',
    'zip': 'Zipped', 'rar': 'Zipped', 'tar': 'Zipped', 'gz': 'Zipped',
    'psd': 'Mockups'
}

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {os.path.basename(folder_path)}")
    return folder_path

if target_directory:
    print(f"Selected folder: {target_directory}")
    all_items = os.listdir(target_directory)
    files = [item for item in all_items if os.path.isfile(os.path.join(target_directory, item))]
    print("\nFiles in the directory:")
    for file in files:
        print(file)

    print("\nOrganizing files:")
    others_folder = os.path.join(target_directory, 'Others')

    for file in files:
        name, extension = os.path.splitext(file)
        extension = extension.lstrip('.').lower()

        if extension in extension_mapping:
            folder_name = extension_mapping[extension]
            destination_folder = create_folder_if_not_exists(os.path.join(target_directory, folder_name))
        else:
            # For unmapped extensions, move to the 'Others' folder
            destination_folder = create_folder_if_not_exists(others_folder)

        source_path = os.path.join(target_directory, file)
        destination_path = os.path.join(destination_folder, file)
        try:
            shutil.move(source_path, destination_path)
            print(f"Moved '{file}' to '{os.path.basename(destination_folder)}' folder.")
        except Exception as e:
            print(f"An error occurred while moving '{file}': {e}")

else:
    print("No folder selected.")