from MusicData import MusicData
from MusicID import MusicID


# ==== FUNC 6 ====
class SearchMetadata():
    def __init__(self, M_ID, MD):
        self._musicID: MusicID = M_ID
        self._musicData: MusicData = MD
    
    def browser(self, key: str, sub: str):
        uuids_retorn = []
        for uuid in self._MusicID._uuid_list.values():
            if self._MusicData._songs[uuid]._data[key].find(sub) != -1:
                uuids_retorn.append(uuid)
                
        if len(uuids_retorn) > 0:
            return uuids_retorn
        return "No s'ha trobat cap resultat amb els criteris especificats"
    
    def title(self, sub: str) -> list:
        return self.browser('title', sub)
                  
    def artist(self, sub: str) -> list:
        return self.browser('artist', sub) 
    
    def album(self, sub: str) -> list:
        return self.browser('album', sub)
    
    def genre(self, sub: str) -> list:
        return self.browser('genre', sub)
    
    def and_operator(self, list1: list, list2: list) -> list:                
        return [uuid for uuid in list1 if uuid in list2]
    
    def or_operator(self, list1: list, list2: list) -> list:
        or_uuids1 = [uuid for uuid in list1 if uuid not in list2]       
        or_uuids2 = [uuid for uuid in list2 if uuid not in list1]     
        return or_uuids1 + or_uuids2