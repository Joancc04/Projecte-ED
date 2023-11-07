from SearchMetadata import SearchMetadata
from MusicPlayer import MusicPlayer
from MusicFiles import MusicFiles
from MusicData import MusicData
from PlayList import PlayList
from MusicID import MusicID


'''
== CÀRREGA DE DADES ==
1. Conseguir paths amb la classe MusicFiles 
2. Generar UUID de totes les cançons amb la classe MusicID 
3. Carregar les metadades de totes les cancçons amb els paths dins de la classe MusicID i 
guardar les dades dins de la class MusicData 

== REPRODUCCIÓ DE CANÇONS ==
4. Crear un objecte MusicPlayer amb les dades de MusicData que tinguem fins el moment  
5. Finalment, fer la playlist 

'''
# Aconseguim els paths de tots els arxius dins de ROOT_DIR
ROOT_DIR = r"C:\Users\joanc\OneDrive\Escritorio\Projecte-ED"
MF = MusicFiles(ROOT_DIR)

Music_ID = MusicID()
Music_ID.initiate(MF)

Music_Data = MusicData(Music_ID)

Music_Player = MusicPlayer(Music_Data)
file = r"C:\Users\joanc\OneDrive\Escritorio\Projecte-ED\blues.m3u"
# file = r"C:\Users\joanc\OneDrive\Escritorio\Projecte-ED\caca.m3u"

# PY = PlayList( MP=Music_Player,
#           playlist_file=file )
# PY.load_file()
# PY.play()

searcher = SearchMetadata(Music_Data)
searcher.genre('pop')