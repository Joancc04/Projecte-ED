from SearchMetadata import SearchMetadata
from MusicPlayer import MusicPlayer
from MusicFiles import MusicFiles
from MusicData import MusicData
from PlayList import PlayList
from MusicID import MusicID
import cfg

'''
== CÀRREGA DE DADES ==
1. Conseguir paths amb la classe MusicFiles 
2. Generar UUID de totes les cançons amb la classe MusicID 
3. Carregar les metadades de totes les cancçons amb els paths dins de la classe MusicID i 
guardar les dades dins de la class MusicData 

== REPRODUCCIÓ DE CANÇONS I BÚSQUEDA DE METADADES ==
4. Crear un objecte MusicPlayer amb les dades de MusicData que tinguem fins el moment  
5. Crear un objecte SearchMetadata també amb utilitzant l'objecte MusicData
5. Crear un objecte PlayList utilitzant el l'object MusicPlayer que hem creat anteriorment i 
amb la direcció del fitxer playlist.

'''
# Aconseguim els paths de tots els arxius dins de ROOT_DIR
# ROOT_DIR = r"C:\Users\joanc\OneDrive\Escritorio\Projecte-ED"

mssg: str = '''
Escull una opció: 
    1- Reproduïr playlist
    2- Consultar metadades de cançons
    0- Sortir
-> '''

mssg_v2: str = '''\nQuè desitjes fer a continuació?''' + mssg

mssg2: str = '''
#==========| SISTEMA GESTOR MUSICAL |==========#
Fet per:
    - Joan Colillas Ceballos 1670247
    - Bernat Vidal Viles 1670982
    - Adrià Díaz García 1665210
'''
mssg3: str = '''
Cercar metadades per:
    1- Títol
    2- Gènere
    3- Àlbum
    4- Artista
'''


#Obtenim el ROOT_DIR
ROOT_DIR = cfg.get_root()

# Adreça de l'arxiu de playlist 'm3u' que es vulgui utilizar en el programa
'''
!!!!!!!!!!!
Important posar el path de l'arxiu M3U per tal de que funcioni tot el relacionat amb la 
classe PlayList
M3U_FILE = r"C:\Users\joanc\OneDrive\Escritorio\Projecte-ED\blues.m3u"
# M3U_FILE = r"C:\Users\joanc\OneDrive\Escritorio\Projecte-ED\Prova_playlist.m3u"
'''
M3U_FILE = r''

#Inicialitzem MusicFiles amb el ROOT_DIR
MF = MusicFiles(ROOT_DIR)

#Inicialitzem MusicID
Music_ID = MusicID()
Music_ID.initiate(MF)

#Inicialitzem MusicData
Music_Data = MusicData(Music_ID)

#Inicialitzem MusicPlayer
Music_Player = MusicPlayer(Music_Data)

#Inicialitzem el Searcher
searcher = SearchMetadata(Music_Data)

# Inicialitzem la playlist
play_list = PlayList(MP=Music_Player, playlist_file=M3U_FILE)

print(mssg2)
op: int = int(input(mssg))
while op != 0:
    if op == 1:
        play_list.load_file()
        play_list.play()
        input("Prem enter per continuar")
    elif op == 2:
        op_searcher = int(input(mssg3))
        if op_searcher == 1:
            text: str = input("Introdueix títol: ")
            searcher.title(text)
        elif op_searcher == 2:
            text: str = input("Introdueix gènere: ")
            searcher.genre(text)
        elif op_searcher == 3:
            text: str = input("Introdueix àlbum: ")
            searcher.album(text)
        elif op_searcher == 4:
            text: str = input("Introdueix artista: ")
            searcher.artist(text)
        else:
            print("ERROR: Opció no vàlida")
        input("Prem enter per continuar")
    else:
        print("ERROR: Opció no vàlida")

    op: int = int(input(mssg_v2))


'''
album -> year
genre -> Pop
title -> Out, Die
'''