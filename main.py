from MusicFiles import MusicFiles
from MusicID import MusicID
from MusicData import MusicData
from MusicPlayer import MusicPlayer
from PlayList import PlayList


'''
== CÀRREGA DE DADES ==
1. Conseguir paths amb la classe MusicFiles NASHE
2. Generar UUID de totes les cançons amb la classe MusicID NASHE
3. Carregar les metadades de totes les cancçons amb els paths dins de la classe MusicID i 
guardar les dades dins de la class MusicData NASHE

== REPRODUCCIÓ DE CANÇONS ==
4. Crear un objecte MusicPlayer amb les dades de MusicData que tinguem fins el moment NASHE 
5. Finalment, fer la playlist 

'''
# Aconseguim els paths de tots els arxius dins de ROOT_DIR
ROOT_DIR = r"C:\Users\joanc\OneDrive\Escritorio\Projecte-ED"
MF = MusicFiles(ROOT_DIR)

Music_ID = MusicID()
Music_ID.initiate(MF)

Music_Data = MusicData(Music_ID)

Music_Player = MusicPlayer(Music_Data)

uuid = Music_Data.songs
uuid = uuid[5][0]


print(uuid)
Music_Player.play_song(mode=2, uuid=uuid)

# file = 'añlkjfñalksjdfñlaksdjf.m3u'
# PY = PlayList( MD=Music_Data,
#          MP=Music_Player,
#          playlist_file=file )



# MD = MusicData()
# M_ID = MusicID()

# for path in MF.files:
#     M_ID.generate_uuid(path)
# # M_id.uuid_list = {path: uuid}


    
# music_p = MusicPlayer(MD)
# playlist = PlayLists(M_ID, music_p)
# playlist.play()
# input()