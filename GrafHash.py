import copy

class GrafHash:
    """Graf amb Adjacency Map structure"""

    class Vertex:
        __slots__ = '_valor'

        def __init__(self, x):
            self._valor=x
                  
        def __str__(self):
            return str(self._valor)
    
################################Definicio Class _Vertex       
    
    def __init__(self, ln=[],lv=[],lp=[],digraf=False):
        """Crea graf (no dirigit per defecte, digraf si dirigit es True.
        """
        self._nodes = { }
        self._out = { }
        self._in = { } if digraf else self._out
              
        for n in ln:
            v=self.insert_vertex(n)
            #nodes[n]=v
        if lp==[]:
            for v in lv:
                self.insert_edge(v[0],v[1])
        else:
            for vA,pA in zip(lv,lp):
                self.insert_edge(vA[0],vA[1],pA)
    
    def es_digraf(self):
        return self._out!=self._in
            
    def insert_vertex(self, x):
        v= self.Vertex(x)
        self._nodes[x] = v
        self._out[x] = { }
        if self.es_digraf():
            self._in[x] = {}
        return v

    def insert_edge(self, n1, n2, p1=1):        
        self._out[n1][n2] = p1
        self._in[n2][n1] = p1
        
    def vertices(self):
        """Return una iteracio de tots els vertexs del graf."""
        return self._nodes.__iter__( )

    def edges(self,x):
        """Return una iteracio de tots els edges de x al graf."""
        return self._out[x].__iter__()
    
    def cicles(self):
        llista = []
        visited = []
        for v1 in self._nodes:
            visited.append(v1)
            for v2 in self._out[v1]:
                if v2 not in visited:
                    for v3 in self._out[v2]:
                        trobat = False
                        if (v3 not in visited) and (v1 in self._out[v3]):
                            cicle = [v1, v2, v3]
                            for tupla in llista:
                                if (cicle[0] in tupla) and (cicle[1] in tupla) and (cicle[2] in tupla):
                                    trobat = True
                      
                            if not trobat:
                                llista.append(cicle)

        return llista


    def __str__(self):
        cad="===============GRAF===================\n"
     
        for it in self._out.items():
            cad1="__________________________________________________________________________________\n"
            cad1=cad1+str(it[0])+" : "
            for valor in it[1].items():
                cad1=cad1+str(str(valor[0])+"("+ str(valor[1])+")"+" , " )
                            
            cad = cad + cad1 + "\n"
        
        return cad