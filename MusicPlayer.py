from time import time, sleep
from MusicData import MusicData
import vlc

class MusicPlayer(): 
    def __init__(self, MData):
        self._MD: MusicData = MData
    
    def print_song(self, uuid: str):
        self._MD.show_info(uuid)
        
    def play_file(self, file: str):
        player = vlc.MediaPlayer(file)
        player.play()
        
        timeout = time() + self._MD.get_duration(self._MD.get_uuid(file)[0])
        while True:
            if time() < timeout:
                try:
                    sleep(1)
                except KeyboardInterrupt: # STOP amb <CTRL>+<C> a la consola
                    break
            else:
                break
    
        player.stop()
        print("\nFinal!") 


    def play_song(self, uuid: str, mode: int):
        if mode == 0:
            self.print_song(uuid)
        elif mode == 1:
            self.print_song(uuid)
            self.play_file(self._MD.get_arxiu(uuid))
        elif mode == 2:
            self.play_file(self._MD.get_arxiu(uuid))
            

    MD = property(lambda self: self._MD)
