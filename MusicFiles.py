import cfg
import os

# ==== FUNC 1 ====
class MusicFiles():
    def __init__(self, ROOT_DIR=None):
        self._ROOT_DIR: str = ""
        self._removed: list = []
        self._files: list = []
        self._added: list = []

    def reload_fs(self, path: str = None):
        new_files: list = list()
        if path is None:
            path = cfg.get_root()
        for directory, _, files in os.walk(path):
            for file in files:
                if file[-4:] == '.mp3': 
                    new_files.append(os.path.join(directory, file))
        
        self._added = [file for file in new_files if file not in self._files]
        self._removed = [file for file in self._files if file not in new_files]
        self._files = new_files
        
    def files_added(self):
        return self._added
    
    def files_removed(self):
        return self._removed

