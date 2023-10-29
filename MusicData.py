import eyed3
import sys
from cfg import get_canonical_pathfile

class MusicData:
    
    class Music:
        def __init__(self, file):
            self._data = {}
            self.load_MetaData(file)
            

        def load_MetaData(self, file):
            file = get_canonical_pathfile(file)
            metadata = eyed3.load(file)
            if metadata is None:
                print("ERROR: Arxiu MP3 erroni!")
                sys.exit(1)
            self._data['title'] = metadata.tag.title
            self._data['artist'] = metadata.tag.artist
            self._data['album'] = metadata.tag.album
            try:
                genre = metadata.tag.genre.name
            except:
                self._data['genre'] = "None"
            else:
                self._data['genre'] = genre
        
        
        title = property(lambda self: self._data['title'])
        artist = property(lambda self: self._data['artist'])
        album = property(lambda self: self._data['album'])
        Genre = property(lambda self: self._data['Genre'])
        song_properties = property(lambda self: self._data)
    

    def _init_(self):
        self._songs: dict = {}

    def add_song(self, uuid, file):
        if uuid not in self._data:
            self._data[uuid] = self.Music(file)
    
    def remove_song(self, uuid):
        try:
            del self._data[uuid]
        except:
            print("L'UUID introduit no existeix.")

    def get_title(self, uuid):
        try:
            return self._data[uuid].title
        except:
            print("L'UUID introduit no existeix.")

    def get_artist(self, uuid):
        try:
            return self._data[uuid].artist
        except:
            print("L'UUID introduit no existeix.")

    def get_album(self, uuid):
        try:
            return self._data[uuid].album
        except:
            print("L'UUID introduit no existeix.")

    def get_genre(self, uuid):
        try:
            return self._data[uuid].genre
        except:
            print("L'UUID introduit no existeix.")
    
    