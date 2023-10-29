from MusicID import MusicID
from MusicFiles import MusicFiles
from MusicPlayer import MusicPlayer
import os
# ==== FUNC 5 ====

class PlayLists:
    def __init__(self, M_ID, MP):
        self._musicID: MusicID = M_ID
        self._musicPlayer: MusicPlayer = MP
        self._next_playlist: PlayLists = None

    def load_file(self, file: str):
        with open(file, 'r', encoding='UTF-8') as M3U_Playlist:
            for line in M3U_Playlist.readlines():
                line.removesuffix('\n')
                if line[0] != '#' and line[-4:] == '.mp3' and os.path.exists(line): 
                    self._musicID.generate_uuid(line)

    def play(self):
        mode = input('''
mode : 0 printem cançó per pantalla
mode : 1 printem cançó i fem play
mode : 2 play de la cançó però no print
                     Escriu l'opció: ''')
        for song in self._musicID.uuid_list:
            pass

        MusicPlayer.play_song(uuid=None, mode=mode)

    next_playlist = property( lambda self: self._next_playlists, 
                              lambda self, playlist: setattr(self, '_next_playlist', playlist) )