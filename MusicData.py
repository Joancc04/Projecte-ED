import eyed3
import sys
from cfg import get_canonical_pathfile
import numpy


class MusicData:
    class Music:
        def __init__(self, file):
            self._data: dict = {}
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
            self._data['duration'] = int(numpy.ceil(metadata.info.time_secs))
            self._data['file'] = file
            try:
                genre = metadata.tag.genre.name
            except:
                self._data['genre'] = "None"
            else:
                self._data['genre'] = genre
        
        
        title = property(lambda self: self._data['title'])
        artist = property(lambda self: self._data['artist'])
        album = property(lambda self: self._data['album'])
        genre = property(lambda self: self._data['genre'])
        duration = property(lambda self: self._data['duration'])
        song_properties = property(lambda self: self._data)
        file = property(lambda self: self._data['file'])


    def __init__(self):
        self._songs: dict = {}

    def add_song(self, uuid, file):
        if uuid not in self._songs:
            self._songs[uuid] = self.Music(file)
    
    def remove_song(self, uuid):
        try: del self._songs[uuid]
        except: print("L'UUID introduit no existeix.")

    def get_title(self, uuid):
        try: return self._songs[uuid].title
        except: print("L'UUID introduit no existeix.")
            
    def get_artist(self, uuid):
        try: return self._songs[uuid].artist
        except: print("L'UUID introduit no existeix.")
           
    def get_album(self, uuid):
        try: return self._songs[uuid].album
        except: print("L'UUID introduit no existeix.")
            
    def get_genre(self, uuid):
        try: return self._songs[uuid].genre
        except: print("L'UUID introduit no existeix.")

    def get_arxiu(self, uuid):
        try: return self._songs[uuid].file
        except: print("L'UUID introduit no existeix.")
            
    def get_duration(self, uuid):
        try: return self._songs[uuid].duration
        except: print("L'UUID introduit no existeix.")
    
    def get_uuid(self, file):
        return [uuid for uuid, song in self._songs.items() if song.file == file]