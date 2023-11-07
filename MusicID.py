import uuid
from MusicFiles import MusicFiles
from cfg import get_canonical_pathfile

# ==== FUNC 2 ====
class MusicID():
    def __init__(self):
        self._units = {}
    
    def initiate(self, MF: MusicFiles):
        for file in MF.files:
            self.generate_uuid(file)

    def generate_uuid(self, file: str) -> str:
        if not self.exists_file(file):
            mp3_uuid = str(uuid.uuid5(uuid.NAMESPACE_URL, get_canonical_pathfile(file)))
            self._units[mp3_uuid] = file
            print(f"\x1B[3m// Song with UUID: {mp3_uuid[:10]}... has been added\x1B[23m")
            return mp3_uuid
        print(f"\x1B[3m// Song with file {file} is already in the database.\x1B[23m")
        return False
            
    def remove_uuid(self, uuid: str):
        try:
            del self._units[uuid]
        except KeyError:
            print(f"ERROR: There is no song with UUID: {uuid} in the database")
    
    def remove_song(self, file):
        song_id = self.get_uuid(file)
        if song_id:
            del self._units[song_id]
        else:
            print(f"ERROR: There is no song with file: {file} in the databse.")

    def get_uuid(self, file: str) -> str:
        return [uuid for uuid, d_file in self._units.items() if d_file == file][0]

    def get_path(self, uuid):
        return self._units[uuid]

    def exists_file(self, file):
        return True if file in [file for _, file in self._units.items()] else False
    
    items = property(lambda self:self._units.items())