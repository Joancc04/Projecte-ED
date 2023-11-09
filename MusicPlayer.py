from MusicData import MusicData
from time import time, sleep
#import vlc
import cfg

# ==== FUNC 4 ====
class MusicPlayer(): 
    def __init__(self, MData):
        self._MD: MusicData = MData
    
    def print_song(self, uuid: str):
        self._MD.show_info(uuid)
        
    def play_file(self, ff):
        pass


    def play_song(self, uuid: str, mode: int):
        if mode == 0:
            self.print_song(uuid)
        elif mode == 1:
            self.print_song(uuid)
            self.play_file(self._MD.get_path(uuid))
        elif mode == 2:
            self.play_file(self._MD.get_path(uuid))
            a = 1

    MD = property(lambda self: self._MD)
