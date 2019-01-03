import random
from unionfind.quickFind import QuickFind
from unionfind.quickUnion import QuickUnion
import graph.Graph_AdjacencyList as grafo
from graph.Graph import GraphBase, Edge, Node
from list.DoubleLinkedList import ListaDoppiamenteCollegata as List
from CacaGrafi import cacaGrafi
from creaGraf import creaGraf1, creaGraf2, creaGraf3, creaGraf4
from decoratorProgetto import timer


class edgeIter:
    "iteratore per scandire gli archi in arcList"
    def __init__(self):
        self.ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        indiceArco = self.ind
        self.ind += 1
        return indiceArco

"""
BOZZA DI ITERATOR CHE SCANDISCE GLI ARCHI IN ARCLIST E RESTITUISCE DIRETTAMENTE a E b (coda e testa) CHE UTILIZZO IN HASCYCLEUF

    def __init__(self):
        self.ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        values = []
        a_value = arcList[self.ind][0]
        values.append(a_value)
        b_value = arcList[self.ind][1]
        values.append(b_value)
        self.ind += 1
        return values

def hasCycleUF(graph,arcList):
    uf=QuickUnion()
    nodes=graph.getNodes()
    for n in nodes:
        uf.makeSet(n)
    uf.print()

    # edges=graph.getEdges()

    iter = edgeIter()

    for i in range(0,len(arcList)):
        arco = next(iter) 
        print("ARCO PRESO DA ITERATORE: ", arco)
        a=arco[0]
        b=arc0[1]
        u=uf.nodes[a]
        v=uf.nodes[b]
        ...

"""
@timer
def hasCycleUF(graph, arcList, dimens):
    uf=QuickUnion()
    nodes=graph.getNodes()
    for n in nodes:
        uf.makeSet(n)
    uf.print()

    # edges=graph.getEdges()

    iter = edgeIter()

    for i in range(0,len(arcList)):
        ind = next(iter) 
        print("\nITERATOR. Arco scelto: ", "(" + str(arcList[ind][0])+", "+str(arcList[ind][1]) + ")" + "\n")
        a=arcList[ind][0]
        b=arcList[ind][1]
        u=uf.nodes[a]
        v=uf.nodes[b]

        print(f'Find sul nodo {u}:\t{uf.find(u)}')
        print(f'Find sul nodo {v}:\t{uf.find(v)}')

        if uf.find(u) == uf.find(v):
            print("find(u) == find(v)\n" + "\nCycle detected!\n")
            return
        else:
            uf.union(u, v)
            print("find(u) != find(v) => union(u, v):\n")
            uf.print()
    print("\nNO cycle detected.\n")
    return




if __name__ == "__main__":

    dim=5
    graph = creaGraf1(dim)  # ritorna una lista graph = [grafo, listaArchi]
    
    ###hascycleUF

    hasCycleUF(graph[0],graph[1], dim)
