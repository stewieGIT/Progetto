from creaGrafiMan import creaGraf1, creaGraf2, creaGraf3, creaGraf4
from creaGrafiRand import creaGrafiRC,creaGrafiRWC
from time import time

if __name__ == "__main__":
    dim = 500
    # ritornano una lista graph = [grafo, listaArchi]

    # MANUAL GRAPH

    #graph = creaGraf1(dim)     # è un grafo con ciclo
    #graph = creaGraf2(dim)     # è un grafo senza ciclo
    #graph = creaGraf3(dim)     # è un grafo senza ciclo
    #graph = creaGraf4(dim)       # è un grafo con ciclo

    # RANDOM GRAPH

    graph = creaGrafiRC(dim)  # è un grafo con ciclo con vertici random (ciclo a cerchio)
    #graph = creaGrafiRWC(dim) # è un grafo senza ciclo con vertici random
    # (come sopra senza l'arco che collega l'ultimo vertice al primo)

    # hascycleDFS

    nodes=graph[0].getNodes()
    start = time()
    for node in nodes:       #viene fatta la dfs da ogni nodo per questo avviene più volte la print cè/non cè ciclo
        print(f'\nDFS partendo dal nodo {node}:')
        s = graph[0].dfs(node.id, dim)
    elapsed = (time() - start) / 500
    print("\nDFS avg time is",elapsed,"seconds")
        # NB la dfs e' una modifica di quella del codice visto a lezione nel file Graph.py della cartella graph






