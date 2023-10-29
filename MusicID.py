import uuid
import cfg_diaz

class MusicID():
    def __init__(self):
        self._uuid_list = {}
    
    def generate_uuid(self, file: str) -> str:
        file_path_canonic = cfg_diaz.get_canonical_pathfile(file)
        mp3_uuid = str(uuid.uuid5(uuid.NAMESPACE_URL, file_path_canonic))

        trobat = False
        for path in self._uuid_list:
            if str(self._uuid_list[path]) == mp3_uuid:
                trobat = True 
                break
                
        if trobat == False:
            self._uuid_list[file] = mp3_uuid
            print("Afegit\n")
        else:
            print("Aquest arxiu no s'utilitzarà, ja hi ha el mateix UUID en ús\n")
            
        
    def get_uuid(self, file: str) -> str:
        try:
            return self._uuid_list[file]
        except:
            print("No existeix UUID per al path proporcionat\n")
            return None
    
    
    def remove_uuid(self, uuid: str):
        eliminat = False
        for path in self._uuid_list:
            if str(self._uuid_list[path]) == uuid:
                del self._uuid_list[path]
                eliminat = True
                print("UUID", uuid, "eliminada amb exit\n")
                break

        if not eliminat:
            print("ERROR: no s'ha trobat l'UUID a eliminar\n")