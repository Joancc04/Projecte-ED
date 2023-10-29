import eyed3
from cfg import get_canonical_pathfile

PATH = "Scott_Holmes_-_07_-_Inspirational_Outlook.mp3"
metadada = eyed3.load(PATH)
print(metadada.tag.artist)