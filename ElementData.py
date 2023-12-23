import eyed3
import numpy
import cfg
import sys


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

class ElementData(Song_Meta):
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