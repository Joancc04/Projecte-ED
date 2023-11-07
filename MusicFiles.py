import os
# ==== FUNC 1 ====
#ROOT_DIR = "C:\\Users\\joanc\\OneDrive\\Escritorio\\Projecte-ED"

class MusicFiles():
    def __init__(self, ROOT_DIR):
        self._ROOT_DIR: str = ROOT_DIR
        self._files: list = []
        self._added: list = []
        self._removed: list = []
        self.reload_fs()

    def reload_fs(self, path: str = None):
        new_files: set = set()
        if path is None: 
            path = self._ROOT_DIR
        for directory, _, files in os.walk(path):
            for file in files:
                if file[-4:] == '.mp3': 
                    new_files.add(directory + os.sep + file)
        if not self._files: 
            self._files = new_files
        elif new_files != self._files:
            self._added = list(new_files - set(self._files))
            self._removed = list(set(self._files) - new_files)
        
    files = property(lambda self: self._files)
    files_added = property(lambda self: self._added)
    files_removed = property(lambda self: self._removed)

