from MusicData import MusicData

# ==== FUNC 6 ====
class SearchMetadata():
    def __init__(self, MD):
        self._musicData: MusicData = MD
    
    def browser(self, key: str, sub: str) -> list:
        uuids_retorn: list = []       
        uuids_retorn = [uuid for uuid, _ in self._musicData.songs 
                        if self._musicData.get_attribute(uuid, key)
                        and self._musicData.get_attribute(uuid, key).find(sub) != -1]
        if uuids_retorn:
            return uuids_retorn
    
    def title(self, sub: str):
        self.return_w_info(self.browser('title', sub), sub, 'title')
                  
    def artist(self, sub: str):
        self.return_w_info(self.browser('artist', sub, sub, 'artist')) 
    
    def album(self, sub: str):
        self.return_w_info(self.browser('album', sub), sub, 'album')
    
    def genre(self, sub: str):
        self.return_w_info(self.browser('genre', sub), sub, 'genre')
    
    def and_operator(self, list1: list, list2: list):                
        return [uuid for uuid in list1 if uuid in list2]
    
    def or_operator(self, list1: list, list2: list):  
        return [uuid for uuid in list1 if uuid not in list2] + \
            [uuid for uuid in list2 if uuid not in list1] 

    def return_w_info(self, l_uuids: list, sub: str, name: str):
        if not l_uuids:
            print(f"\nNo songs found for attribute [{name}] : {sub}")
        else:
            print(f"- {len(l_uuids)} songs found for attribute [{name}] : {sub}")
            for uuid in l_uuids:
                print(f"UUID: {uuid[:12]}... | Title: {self._musicData.get_attribute(uuid, 'title')}")