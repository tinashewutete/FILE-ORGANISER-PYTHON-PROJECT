# Simple File Organizer

This Python script helps you organize files in a selected folder by grouping them into subfolders based on their file types (images, videos, documents, etc.).

## How to Use

1.  **Save the script:** Save the Python code as a `.py` file (e.g., `file_organizer.py`).
2.  **Run the script:** Open your terminal or command prompt, navigate to the directory where you saved the file, and run it using:
    ```bash
    python file_organizer.py
    ```
3.  **Select a folder:** A graphical dialog box will appear, prompting you to select the folder you want to organize.
4.  **Organization:** The script will then:
    * Create subfolders within the selected folder for different file types (e.g., Images, Videos, Documents, Music, Zipped, Mockups, Others).
    * Move the files into their corresponding folders based on their file extensions.

## Modules Used

This script utilizes the following Python modules:

* **`tkinter`**: This module is used to create the graphical user interface elements, specifically the "Browse For Folder" dialog box that allows you to easily select the directory you want to organize.
* **`os`**: This module provides functions for interacting with the operating system, such as listing files in a directory, creating new directories (folders), and joining path components.
* **`shutil`**: This module offers high-level file operations. In this script, it's used to efficiently move files from their original location to their newly organized folders.

## Supported File Types

The script currently organizes files into the following categories:

* **Images:** jpg, jpeg, png, gif, bmp
* **Videos:** mp4, avi, mov, mkv
* **Music:** mp3, wav, flac
* **Documents:** pdf, doc, docx, txt, rtf
* **Zipped:** zip, rar, tar, gz
* **Mockups:** psd
* **Others:** Files with extensions not listed above will be moved to an "Others" folder.

## Requirements

* Python 3.x

## Author

Tinashe Wutete

