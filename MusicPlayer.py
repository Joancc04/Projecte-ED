import cfg
import vlc
from time import time, sleep
from MusicData import MusicData

class MusicPlayer(): 

    def __init__(self, MData):
        self._mdata: MusicData = MData
    
    def print_song(self, uuid: str):
        print(f"Reproduïnt [{self._mdata.get_name(uuid)}]")
        print(f"Duració: {self._mdata.get_duration(uuid)} segons")
        print(f"Títol: {self._mdata.get_title(uuid)}")
        print(f"Artista: {self._mdata.get_artist(uuid)}")
        print(f"Àlbum: {self._mdata.get_album(uuid)}")
        print(f"Gènere: {self._mdata.get_genre(uuid)}")
        print(f"UUID: {self._mdata.get_uuid(uuid)}")
        print(f"Arxiu: {cfg.get_canonical_pathfile(self._mdata.get_arxiu(uuid))}")
        
    
    def play_file(self, file: str):
        player = vlc.MediaPlayer(file)
        player.play()
        
        timeout = time() + 170 #MData.get_duration
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
            self.play_file(self._mdata.get_arxiu(uuid))
        elif mode == 2:
            self.play_file(self._mdata.get_arxiu(uuid))
    
    def get_attr(self, attr):
        pass


    MD = property(lambda self: self._mdata)