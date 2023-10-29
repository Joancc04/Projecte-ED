from MusicID import MusicID
import os

class PlayList:
    def __init__(self):
        pass

    def load_file(self, file: str):
        l_paths: list = []
        with open(file, 'r', encoding='UTF-8') as M3U_Playlist:
            for line in M3U_Playlist.readlines():
                line.removesuffix('\n')
                if line[0] != '#' and line[-4:] != '.mp3' and os.path.exists(line): 
                    l_paths.append(line)
                    
