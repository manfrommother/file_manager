import os
import shutil
import zipfile
from typing import Dict

class FileManager:
    
    def __init__(self, source_zip:str, destination_dir:str, folder_names: Dict[str, str]):
        self.source_zip = source_zip
        self.destination_dir = destination_dir
        self.folder_name = folder_names

    def extract_and_organize(self):
        with zipfile.ZipFile(self.source_zip, 'r') as zip_ref:
            zip_ref.extractall(self.destination_dir)

        for root, _, files in os.walk(self.destination_dir):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    self._move_file(file_path)

    def _move_file(self, file_path: str):
        extension = os.path.splitext(file_path)[1].lower()
        folder_name = self.folder_name.get(extension, 'others')
        destination_folder = os.path.join(self.destination_dir, folder_name)
        os.makedirs(destination_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(destination_folder, os.path.basename(file_path)))
        
