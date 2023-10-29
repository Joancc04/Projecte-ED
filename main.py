from MusicFiles import MusicFiles
from MusicData import MusicData
from MusicID import MusicID
from MusicPlayer import MusicPlayer
from PlayList import PlayLists

MF = MusicFiles(r"C:\Users\joanc\OneDrive\Escritorio\Projecte-ED")
MF.reload_fs()
MD = MusicData()

M_ID = MusicID()
for path in MF.files:
    M_ID.generate_uuid(path)
# M_id.uuid_list = {path: uuid}

for file_path, uuid in M_ID.uuid_list:
    MD.add_song( uuid=uuid,
                 file=file_path )
    
music_p = MusicPlayer(MD)
playlist = PlayLists(M_ID, music_p)
playlist.play()
input()