from creaGrafiMan import creaGraf1, creaGraf2, creaGraf3, creaGraf4
from creaGrafiRand import creaGrafiRC,creaGrafiRWC
from time import time

def hasCycleDfs(graph,dim):
    if dim==0:
        print("\nEmpty graph can't execute a DFS")
        return
    if dim==1 or dim==2:
        print("\nGraph with dimension=1 or dimension=2 can't contain a cycle")
        return
    nodes=graph[0].getNodes()
    for node in nodes:       #viene fatta la dfs da ogni nodo per questo avviene più volte la print cè/non cè ciclo
        print(f'\nDFS partendo dal nodo {node}:')
        s = graph[0].dfs(node.id, dim)


if __name__ == "__main__":
    dim = 100
    # ritornano una lista graph = [grafo, listaArchi]

    # MANUAL GRAPH

    #graph = creaGraf1(dim)     # è un grafo con ciclo
    #graph = creaGraf2(dim)     # è un grafo senza ciclo
    #graph = creaGraf3(dim)     # è un grafo senza ciclo
    #graph = creaGraf4(dim)       # è un grafo con ciclo

    # RANDOM GRAPH

    #graph = creaGrafiRC(dim)  # è un grafo con ciclo con vertici random (ciclo a cerchio)
    graph = creaGrafiRWC(dim) # è un grafo senza ciclo con vertici random
    # (come sopra senza l'arco che collega l'ultimo vertice al primo)

    # hasCycleDfs

    hasCycleDfs(graph,dim)






