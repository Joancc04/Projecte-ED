import vlc
from MusicPlayer import MusicPlayer
from time import time, sleep

# MusicPlayer.play_file("Scott_Holmes_-_07_-_Inspirational_Outlook.mp3")

# player = vlc.MediaPlayer("Scott_Holmes_-_07_-_Inspirational_Outlook.mp3")
# player.play()

# timeout = time() + 170
# while True:
#     if time() < timeout:
#         try:
#             sleep(1)
#         except KeyboardInterrupt: # STOP amb <CTRL>+<C> a la consola
#             break
#     else:
#         break
# player.stop()
# input("asdfasdf")
from cfg import get_canonical_pathfile
import vlc
import os
import sys

whereami = os.getcwd()
for directory, _, files in os.walk(whereami):
    print(get_canonical_pathfile(directory))



# file = r"C:\Users\joanc\OneDrive\Escritorio\Projecte-ED\installers\classical.mp3"
# cum = vlc.MediaPlayer(file)
# cum.play()