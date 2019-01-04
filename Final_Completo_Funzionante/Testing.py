from ufCheckQuickUnion import hasCycleUFQU
from ufCheckQuickFind import hasCycleUFQF
from creaGrafiRand import creaGrafiRC,creaGrafiRWC
from time import time
if __name__ == "__main__":
    tempoUFQUC=[]
    tempoUFQFC=[]
    tempoDFSC=[]
    tempoUFQUWC = []
    tempoUFQFWC = []
    tempoDFSWC = []
    dim=[5,10,25,50,100,250,500,1000,2500]

    #GRAFI CON CICLI

    for i in range(0,len(dim)):
        graph_C=creaGrafiRC(dim[i])

        #QUICKFIND
        start=time()
        hasCycleUFQF(graph_C[0],graph_C[1],dim[i])
        elapsed=time()-start
        tempoUFQFC.append(elapsed)
        print("\nUFQuickFindCheck time elapsed with graph (cycle) dimension:", dim[i], "-->", elapsed)

        # DFS

        start = time()
        hasCycleUFQU(graph_C[0], graph_C[1], dim[i])
        elapsed = time() - start
        tempoUFQUC.append(elapsed)
        print("\nUFQuickUnionCheck time elapsed with graph (cycle) dimension:", dim[i], "-->", elapsed)

        nodes = graph_C[0].getNodes()
        start = time()
        for node in nodes:  # viene fatta la dfs da ogni nodo e poi la media
            print(f'\nDFS partendo dal nodo {node}:')
            start = time()
            s = graph_C[0].dfs(node.id, dim)
        elapsed = (time() - start) / dim[i]
        tempoDFSC.append(elapsed)
        print("\nDFScheck time elapsed with graph (cycle) dimension:", dim[i], "-->", elapsed)

    # GRAFI SENZA CICLI

    for i in range(0, len(dim)):
        graph_WC = creaGrafiRWC(dim[i])

        # QUICKFIND
        start = time()
        hasCycleUFQF(graph_WC[0], graph_WC[1], dim[i])
        elapsed = time() - start
        tempoUFQFWC.append(elapsed)
        print("\nUFQuickFindCheck time elapsed with graph (not cycle) dimension:", dim[i], "-->", elapsed)

        # QUICKUNION
        start = time()
        hasCycleUFQU(graph_WC[0], graph_WC[1], dim[i])
        elapsed = time() - start
        tempoUFQUWC.append(elapsed)
        print("\nUFQuickUnionCheck time elapsed with graph (not cycle) dimension:", dim[i], "-->", elapsed)

        # DFS
        nodes = graph_WC[0].getNodes()
        start = time()
        for node in nodes:  # viene fatta la dfs da ogni nodo e poi la media
            print(f'\nDFS partendo dal nodo {node}:')
            start = time()
            s = graph_WC[0].dfs(node.id, dim)
        elapsed = (time() - start) / dim[i]
        tempoDFSWC.append(elapsed)
        print("\nDFScheck time elapsed with graph (not cycle) dimension:", dim[i], "-->", elapsed)


    print("\nDFS cycle array",tempoDFSC)
    print("DFS without cycle array",tempoDFSWC)
    print("UFQuickUnion cycle array",tempoUFQUC)
    print("UFQuickUnion without cycle array", tempoUFQUWC)
    print("UFQuickFind cycle array", tempoUFQFC)
    print("UFQuickFind without cycle array", tempoUFQFWC)