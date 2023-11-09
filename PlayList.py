from MusicPlayer import MusicPlayer
from MusicData import MusicData
from MusicID import MusicID
import os


# ==== FUNC 5 & 7 ====
class PlayList:
    def __init__(self, MI: MusicID, MP: MusicPlayer):
        print(MI, MP)
        self._musicID: MusicID = MI
        self._next_playlist: PlayList = None
        self._musicPlayer: MusicPlayer = MP
        self._musicData: MusicData = self._musicPlayer.MD
        self._songs: list = []
        
    def load_file(self, file: str = None):
        self._songs = []
        if file is None: 
            file = self._file
        if os.path.exists(file):
            with open(file, 'r', encoding='latin-1') as M3U_Playlist:
                for file in M3U_Playlist.readlines():
                    file = file.replace('\n', '')
                    if file[0] != '#' and file[-4:] == '.mp3': 
                        uuid = self._musicID.get_uuid(file)
                        self.add_song_at_end(uuid)

    def add_song_at_end(self, uuid: str):
        self._songs.append(uuid)

    def remove_first_song(self): 
        if self._songs:
            del self._songs[0]

    def remove_last_song(self):
        if self._songs:
            del self._songs[-1]

    def play(self, mode):
        for song_id in self._songs:
            self._musicPlayer.play_song( uuid=song_id,
                                         mode=mode )
            

    def set_next_playlist(self, playlist):
        self._next_playlist = playlist
    
    def __len__(self):
        return len(self._songs)
    
    next_playlist = property( lambda self: self._next_playlists, 
                              lambda self, playlist: setattr(self, '_next_playlist', playlist) )