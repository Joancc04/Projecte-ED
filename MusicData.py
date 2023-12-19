import cfg
from MusicID import MusicID
import eyed3
import numpy
import sys
import os


# ==== FUNC 3 ====
class MusicData:
    class Song_Meta:
        __slots__ = ('_data')

        def __init__(self):
            self._data: dict = {}
            
        def load_MetaData(self, file: str):
            metadata = eyed3.load(cfg.get_canonical_pathfile(file))
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
        __slots__ = ('_file', '_uuid')

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

    __slots__ = ('_songs')

    def __init__(self):
        self._songs: dict = {}

    def add_song(self, uuid: str, file_path: str = None):
        if os.path.exists(file_path):
            self._songs[uuid] = self.Song( file=file_path,
                                           uuid=uuid )
        else:
            print("FAKEEEEE")
        
    
    def load_metadata(self, uuid):
       pass
   # ********
    
    def remove_song(self, uuid: str):
        try: 
            del self._songs[uuid]
        except: 
            print("UUID given does not exist")
    
        
    def get_title(self, uuid):
        try:
            song = self._songs[uuid]
        except Exception:
            return None
        else:
            return song.title
    
    def get_album(self, uuid):
        try:
            song = self._songs[uuid]
        except Exception:
            return None
        else:
            return song.album
    
    def get_artist(self, uuid):
        try:
            song = self._songs[uuid]
        except Exception:
            return None
        else:
            return song.artist
    
    def get_genre(self, uuid):
        try:
            song = self._songs[uuid]
        except Exception:
            return None
        else:
            return song.genre
    
    def get_filename(self, uuid):
        try:
            song = self._songs[uuid]
        except Exception:
            return None
        else:
            return song.file
        
    def get_duration(self, uuid):
        try:
            song = self._songs[uuid]
        except Exception:
            return None
        else:
            return song.duration
    
    def show_info(self, uuid: str):
        try:
            self._songs[uuid].print()
            #print(f"[ UUID: {uuid[:11]}... | file_path: {self._songs[uuid].file}]")
        except KeyError:
            return None
            
    def get_uuid(self, file: str) -> str:
        return self._Music_ID.get_uuid(file)

    def get_path(self, uuid: str) -> str:
        return self._Music_ID.get_path(uuid)
    
    def exists_file(self, given_file: str) -> bool:
        return True if given_file in [song.file for _, song in self._songs.items()] else False
    
    def __len__(self):
        return len(self._songs)
        
    def __repr__(self):
        return f'MusicData({self._songs})'
    
    def __iter__(self):
        for i in self._songs:
            yield i

    songs = property(lambda self: list(self._songs.items()))