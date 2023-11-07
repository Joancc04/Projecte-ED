from MusicPlayer import MusicPlayer
from MusicData import MusicData

import os
from time import time

# ==== FUNC 5 & 7 ====

class PlayList:
    def __init__(self, MP, MD, playlist_file):
        self._musicPlayer: MusicPlayer = MP
        self._musicData: MusicData = MD
        self._songs: list = []
        self._next_playlist: PlayList = None
        self._file = playlist_file
        
        

    def load_file(self, file: str = None):
        if file is None: 
            file = self._file
        with open(file, 'r', encoding='UTF-8') as M3U_Playlist:
            for file in M3U_Playlist.readlines():
                file = file.replace('\n', "")
                if file[0] != '#' and file[-4:] == '.mp3' and self._musicData.exists_file(file): 
                    self._songs.append(self._musicData.get_uuid(file))

    def add_song_at_end(self, uuid: str):
        self._songs.append(uuid)

    def remove_first_song(self): 
        del self._songs[0]

    def remove_last_song(self):
        del self._songs[-1]

    def play(self):
        mode = int(input('''
mode : 0 printem cançó per pantalla
mode : 1 printem cançó i fem play
mode : 2 play de la cançó però no print
Escriu l'opció: '''))
        for song_id in self._songs:
            self._musicPlayer.play_song( uuid=song_id,
                                         mode=mode )
            

    def set_next_playlist(self, playlist):
        self._next_playlist = playlist
    
    next_playlist = property( lambda self: self._next_playlists, 
                              lambda self, playlist: setattr(self, '_next_playlist', playlist) )