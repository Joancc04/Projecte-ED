from MusicData import MusicData

# ==== FUNC 6 ====
class SearchMetadata():
    __slots__ = ('_musicData')

    def __init__(self, MD):
        self._musicData: MusicData = MD

    def title(self, sub: str):
        uuids = [uuid for uuid, _ in self._musicData.songs
                    if self._musicData.get_title(uuid)
                    and self._musicData.get_title(uuid).lower().find(sub) != -1]
        print("TITLE", uuids, sub)
        return uuids
                  
    def artist(self, sub: str):
        uuids = [uuid for uuid, _ in self._musicData.songs
                    if self._musicData.get_artist(uuid)
                    and self._musicData.get_artist(uuid).lower().find(sub) != -1]
        print("ARTIST", uuids, sub)
        return uuids
    
    def genre(self, sub: str):
        uuids = [uuid for uuid, _ in self._musicData.songs
                    if self._musicData.get_genre(uuid)
                    and self._musicData.get_genre(uuid).lower().find(sub) != -1]
        print("GENRE", uuids, sub)
        return uuids
    
    def album(self, sub: str):
        uuids = [uuid for uuid, _ in self._musicData.songs
                    if self._musicData.get_album(uuid)
                    and self._musicData.get_album(uuid).lower().find(sub) != -1]
        print("ALBUM", uuids, sub)
        return uuids
        
    
    def and_operator(self, list1: list, list2: list):                
        return [uuid for uuid in list1 if uuid in list2]
    
    def or_operator(self, list1: list, list2: list):  
        return [uuid for uuid in list1 if uuid not in list2] + \
            [uuid for uuid in list2 if uuid not in list1] 

    def return_w_info(self, l_uuids: list, sub: str, name: str):
        if not l_uuids:
            print(f"\nNo songs found for attribute [{name}] : {sub}")
        else:
            out_l = []
            print(f"- {len(l_uuids)} songs found for attribute [{name}] : {sub}")
            for uuid in l_uuids:
                attr_value = self._musicData.get_attribute(uuid, 'title')
                print(f"UUID: {uuid[:12]}... | Title: {attr_value}")
                out_l.append(attr_value)
            return out_l
    
    def __repr__(self):
        return f'MusicFiles({self._musicData})'