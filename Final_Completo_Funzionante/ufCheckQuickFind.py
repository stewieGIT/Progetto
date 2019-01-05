from unionfind.quickFind import QuickFindBalanced,QuickFind
from creaGrafiMan import creaGraf1, creaGraf2, creaGraf3, creaGraf4
from creaGrafiRand import creaGrafiRWC,creaGrafiRC
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


#QUICKFIND BALANCED

@timer
def hasCycleUFQFB(graph, arcList, dimens):
    uf=QuickFindBalanced()
    nodes=graph.getNodes()
    for n in nodes:
        uf.makeSet(n)
    uf.print()

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
            uf.union(uf.findRoot(u),uf.findRoot(v) )
            print("find(u) != find(v) => union(u, v):\n")
            uf.print()
    print("\nNO cycle detected.\n")
    return

#QUICKFIND

@timer
def hasCycleUFQF(graph, arcList, dimens):
    uf=QuickFind()
    nodes=graph.getNodes()
    for n in nodes:
        uf.makeSet(n)
    uf.print()

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
            uf.union(uf.findRoot(u),uf.findRoot(v) )
            print("find(u) != find(v) => union(u, v):\n")
            uf.print()
    print("\nNO cycle detected.\n")
    return


if __name__ == "__main__":

    dim=500
    #ritornano una lista graph = [grafo, listaArchi]

    # MANUAL GRAPH

    #graph = creaGraf1(dim)     # è un grafo con ciclo
    #graph = creaGraf2(dim)     # è un grafo senza ciclo
    #graph = creaGraf3(dim)      # è un grafo senza ciclo
    #graph = creaGraf4(dim)     # è un grafo con ciclo

    # RANDOM GRAPH

    graph = creaGrafiRC(dim)  # è un grafo con ciclo (con vertici di chiave random)
    #graph = creaGrafiRWC(dim) # è un grafo senza ciclo

    #hascycleUF

    hasCycleUFQF(graph[0],graph[1],dim)   #dim serve per il decorator
    hasCycleUFQFB(graph[0], graph[1], dim)

