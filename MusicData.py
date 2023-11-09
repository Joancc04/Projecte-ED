from cfg import get_canonical_pathfile
from MusicID import MusicID
import eyed3
import numpy
import sys

# ==== FUNC 3 ====
class MusicData:
    class Song_Meta:
        def __init__(self):
            self._data: dict = {}
            
        def load_MetaData(self, file: str):
            metadata = eyed3.load(get_canonical_pathfile(file))
            if metadata is None:
                print("ERROR: Arxiu MP3 erroni!")
                sys.exit(1)
            
            self._data['album'] = metadata.tag.album
            self._data['title'] = metadata.tag.title
            self._data['artist'] = metadata.tag.artist
            self._data['duration'] = int(numpy.ceil(metadata.info.time_secs))
            
            try:
                genre = metadata.tag.genre.name
            except Exception:
                self._data['genre'] = "None"
            else:
                self._data['genre'] = genre
        
        title = property(lambda self: self._data['title'])
        artist = property(lambda self: self._data['artist'])
        album = property(lambda self: self._data['album'])
        genre = property(lambda self: self._data['genre'])
        duration = property(lambda self: self._data['duration'])
        song_properties = property(lambda self: self._data)
    
    class Song(Song_Meta):
        def __init__(self, file: str, uuid: str):
            super().__init__()
            self._file: str = file
            self._uuid: str = uuid
            super().load_MetaData(self._file)
        
        def print(self):
            print(f'''
#============================| {self.title} |=======================#
Duració: \t{self.duration} segons
Artista: \t{self.artist}
Àlbum:   \t{self.album}
Gènere: \t{self.genre}           
''')

        file = property(lambda self: self._file)
    # ________________FI DE SUBLCLASSES_____________________________________________________________________

    def __init__(self, MID: MusicID = None):
        self._songs: dict = {}
        self._Music_ID: MusicID = MID
        self.load_data()

    def add_song(self, file_path: str, uuid: str = None):
        if uuid is not None and uuid not in self._songs:
            self._songs[uuid] = self.Song( file=file_path,
                                           uuid=uuid )
        elif not uuid:
            print(f"Song with path {file_path} is already in the database MUSIC_ID.")
        else:
            generated_uuid = self._Music_ID.generate_uuid(file_path)
            self.add_song(file_path=file_path, uuid=generated_uuid)
    
    def load_data(self):
        for uuid, file_path in self._Music_ID.items:
            self.add_song(uuid=uuid, file_path=file_path)
    
    def remove_song(self, uuid: str):
        try: 
            del self._songs[uuid]
        except: 
            print("UUID given does not exist")
    
    def get_attribute(self, uuid: str, attribute_name: str) -> str:
        song = self._songs.get(uuid, None)
        if song:
            return getattr(song, attribute_name)
        else:
            print("UUID given does not exist")
            return 'No_songs_found'

    def show_info(self, uuid: str):
        try:
            self._songs[uuid].print()
            print(f"[ UUID: {uuid[:11]}... | file_path: {self._songs[uuid].file}]")
        except KeyError:
            print(f"ERROR: There is no song with uuid: {uuid} in the database MusicData.")

    def get_uuid(self, file: str) -> str:
        return self._Music_ID.get_uuid(file)

    def get_path(self, uuid: str) -> str:
        return self._Music_ID.get_path(uuid)
    
    def exists_file(self, given_file: str) -> bool:
        return True if given_file in [song.file for _, song in self._songs.items()] else False

    songs = property(lambda self: list(self._songs.items()))