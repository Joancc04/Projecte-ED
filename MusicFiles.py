import os

#ROOT_DIR = "C:\\Users\\joanc\\OneDrive\\Escritorio\\Projecte-ED"

class MusicFiles():
    def __init__(self, ROOT_DIR):
        self._RD: str = ROOT_DIR
        self._files: list = []
        self._added: list = []
        self._removed: list = []

    def reload_fs(self, path: str = None):
        new_files: set = set()
        if path is None: path = self._RD
        for directory, _, files in os.walk(path):
            for file in files:
                if file.endswith(".mp3"): 
                    new_files.add(directory + os.sep + file)
        if new_files != self._files and self._files:
            self._added = list(new_files - set(self._files))
            self._removed = list(set(self._files) - new_files)

    files = property(lambda self: self._files)
    files_added = property(lambda self: self._added)
    files_removed = property(lambda self: self._removed)

#mf = MusicFiles(ROOT_DIR)
