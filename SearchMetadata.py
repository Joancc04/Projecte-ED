from MusicData import MusicData
from MusicID import MusicID


# ==== FUNC 6 ====
class SearchMetadata():
    def __init__(self, MD):
        self._musicData: MusicData = MD
    
    def browser(self, key: str, sub: str) -> list:
        uuids_retorn: list = []       
        uuids_retorn = [uuid for uuid, _ in self._musicData if self._musicData.get_attribute(uuid, key).find(sub) != -1]
        if uuids_retorn:
            return uuids_retorn
        print("No results found with the given key.")
    
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
        return [uuid for uuid in list1 if uuid not in list2] + \
            [uuid for uuid in list2 if uuid not in list1] 