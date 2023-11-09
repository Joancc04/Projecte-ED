import cfg
from MusicFiles import MusicFiles
import uuid

# ==== FUNC 2 ====
class MusicID():
    def __init__(self):
        self._units = {}

    def generate_uuid(self, file: str):
        if not self.exists_file(file):
            mp3_uuid = str(uuid.uuid5(uuid.NAMESPACE_URL, cfg.get_canonical_pathfile(file)))
            if mp3_uuid in self._units:
                print("UUID JA EN LA BASE DE DADES")
            self._units[mp3_uuid] = file
            print(f"\x1B[3m// Song with UUID: {mp3_uuid[:10]}... has been added\x1B[23m")
            return mp3_uuid
        print(f"\x1B[3m// Song with file {file} is already in the database.\x1B[23m")
        
    def remove_uuid(self, uuid: str):
        try:
            del self._units[uuid]
        except KeyError:
            print(f"ERROR: There is no song with UUID: {uuid} in the database")
    
    def remove_song(self, file: str):
        song_id = self.get_uuid(file)
        if song_id:
            del self._units[song_id]
        else:
            print(f"ERROR: There is no song with file: {file} in the databse.")

    def get_uuid(self, file: str) -> str:
        for uuid_units, d_file in self._units.items():
            if file == d_file:
                return uuid_units
        return None

    def get_path(self, uuid: str) -> str:
        return self._units[uuid]

    def exists_file(self, file: str) -> bool:
        return True if file in [file for _, file in self._units.items()] else False
    
    def __len__(self):
        return len(self._units.keys())
    
    items = property(lambda self: self._units.items())