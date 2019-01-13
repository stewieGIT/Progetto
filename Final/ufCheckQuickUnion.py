from unionfind.quickUnion import QuickUnionBalanced,QuickUnion,QuickUnionBalancedPathCompression,QuickUnionBalancedPathSplitting
from creaGrafiMan import creaGraf1, creaGraf2, creaGraf3, creaGraf4
from creaGrafiRand import creaGrafiRWC,creaGrafiRC
from decoratorProgetto import timer

# Gli algoritmi in questo file sono tutti uguali,cambia solo la versione di unionFind utilizzata

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

#QUICKUNION BALANCED WITH PATH COMPRESSION

@timer
def hasCycleUFQUBPC(graph, arcList, dimens):
    if dimens==0:
        print("Empty graph can't build a unionFind data structure")
        return
    if dimens==1 or dimens==2:
        print("\nGraph with dimension=1 or dimension=2 can't contain a cycle")
        return
    uf=QuickUnionBalancedPathCompression()
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
            uf.union(u, v)
            print("find(u) != find(v) => union(u, v):\n")
            uf.print()
    print("\nNO cycle detected.\n")
    return

#QUICKUNION BALANCED WITH PATH SPLITTING

@timer
def hasCycleUFQUBPS(graph, arcList, dimens):
    if dimens==0:
        print("Empty graph can't build a unionFind data structure")
        return
    if dimens==1 or dimens==2:
        print("\nGraph with dimension=1 or dimension=2 can't contain a cycle")
        return
    uf=QuickUnionBalancedPathSplitting()
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
            uf.union(u, v)
            print("find(u) != find(v) => union(u, v):\n")
            uf.print()
    print("\nNO cycle detected.\n")
    return

#QUICKUNION BALANCED

@timer
def hasCycleUFQUB(graph, arcList, dimens):
    if dimens==0:
        print("Empty graph can't build a unionFind data structure")
        return
    if dimens==1 or dimens==2:
        print("\nGraph with dimension=1 or dimension=2 can't contain a cycle")
        return
    uf=QuickUnionBalanced()
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
            uf.union(u, v)
            print("find(u) != find(v) => union(u, v):\n")
            uf.print()
    print("\nNO cycle detected.\n")
    return

# QUICKUNION

@timer
def hasCycleUFQU(graph, arcList, dimens):
    if dimens==0:
        print("Empty graph can't build a unionFind data structure")
        return
    if dimens==1 or dimens==2:
        print("\nGraph with dimension=1 or dimension=2 can't contain a cycle")
        return
    uf=QuickUnion()
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
            uf.union(u, v)
            print("find(u) != find(v) => union(u, v):\n")
            uf.print()
    print("\nNO cycle detected.\n")
    return


if __name__ == "__main__":

    dim=100
    #ritornano una lista graph = [grafo, listaArchi]

    # MANUAL GRAPH

    #graph = creaGraf1(dim)     # è un grafo con ciclo
    #graph = creaGraf2(dim)     # è un grafo senza ciclo
    #graph = creaGraf3(dim)      # è un grafo senza ciclo
    #graph = creaGraf4(dim)     # è un grafo con ciclo

    # RANDOM GRAPH

    graph = creaGrafiRC(dim)  # è un grafo con o senza ciclo random (per ora ha dim^2 archi perciò ha il ciclo per forza)
    #graph = creaGrafiRWC(dim) # è un grafo senza ciclo

    #hascycleUF

    hasCycleUFQU(graph[0],graph[1],dim)   #dim serve per il decorator
    hasCycleUFQUB(graph[0], graph[1], dim)
    hasCycleUFQUBPC(graph[0],graph[1],dim)
    hasCycleUFQUBPS(graph[0],graph[1],dim)