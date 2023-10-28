import os, sys
ROOT_DIR = "C:\\Users\\joanc\\OneDrive\\Escritorio\\Projecte-ED"
    
def trobar_mp3(root_dir: str):
    l_mp3_dirs: list = []  # Llista per emmagatzemar els camins als arxius MP3
    for directory, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".mp3"): l_mp3_dirs.append(directory + os.sep + file)
    return l_mp3_dirs

print(sys.version)
print("aaa2", trobar_mp3(ROOT_DIR))

class MusicFiles():
    def __init__(ROOT_DIR, self):
        self._RD: str = ROOT_DIR
        self._files: list = []
        self._added: list = []
        self._removed: list = []

    def reload_fs(self, path: str):
        new_files: set = {}
        for directory, _, files in os.walk(path):
            for file in files:
                if file.endswith(".mp3"): 
                    new_files.add(directory + os.sep + file)
        if new_files != self._files:
            self._added = list(new_files - set(self._files))
            self._removed = list(set(self._files) - new_files)
            self._removed = [file for file in self._files if file not in new_files]
        

    def files_added() -> list:
        return 

    def files_removed() -> list: ...
    
    ROOT_DIR = property(lambda self: self._RD, lambda self, new_rd: setattr(self, "_RD", new_rd))
    files = property(lambda self: self._files)