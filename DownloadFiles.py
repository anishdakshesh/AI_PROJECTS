import os
import requests
import mimetypes
import threading
from pathlib import Path

# Function to download a file
def download_file(url, destination):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

# Function to classify and move files based on their extension
def classify_and_move(file_path, destination_folder):
    extension = file_path.suffix.lower()

    # Define categories and their corresponding extensions
    categories = {
        'photos': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'videos': ['.mp4', '.avi', '.mkv', '.mov'],
        'songs': ['.mp3', '.wav', '.flac', '.ogg'],
        'others': []
    }

    category = 'others'  # Default category

    for cat, exts in categories.items():
        if extension in exts:
            category = cat
            break

    # Create the destination folder if it doesn't exist
    category_folder = destination_folder / category
    category_folder.mkdir(parents=True, exist_ok=True)

    # Move the file to the appropriate folder
    new_file_path = category_folder / file_path.name
    file_path.rename(new_file_path)
    print(f'Moved "{file_path.name}" to {category} folder.')

# Function to continuously check and process files in the download folder
def file_processor(download_folder, destination_folder):
    while True:
        for file_path in download_folder.glob('*'):
            if file_path.is_file():
                classify_and_move(file_path, destination_folder)
            elif file_path.is_dir():
                file_processor(file_path, destination_folder)  # Recursively process subdirectories
        # Sleep to avoid high CPU usage in the background
        threading.Event().wait(5)

if __name__ == '__main__':
    download_folder = Path('downloads')  # Specify your download folder
    destination_folder = Path('sorted_files')  # Specify your destination folder

    # Create the download and destination folders if they don't exist
    download_folder.mkdir(parents=True, exist_ok=True)
    destination_folder.mkdir(parents=True, exist_ok=True)

    # Start the file processing thread
    processing_thread = threading.Thread(target=file_processor, args=(download_folder, destination_folder))
    processing_thread.start()

    # Your main program continues here
    while True:
        url = input('Enter the URL of the file to download (or "exit" to quit): ')
        if url == 'exit':
            break
        filename = url.split('/')[-1]
        download_path = download_folder / filename
        download_file(url, download_path)
