from ufCheckQuickUnion import hasCycleUFQU,hasCycleUFQUB,hasCycleUFQUBPC,hasCycleUFQUBPS
from ufCheckQuickFind import hasCycleUFQF,hasCycleUFQFB
from dfsCheck import hasCycleDfs
from creaGrafiRand import creaGrafiRC,creaGrafiRWC
from time import time
if __name__ == "__main__":

    # ARRAY PER PYPLOT

    tempoUFQUC=[]          #tempo UnionFindCheck con QuickUnion in grafo con ciclo
    tempoUFQFC=[]          #tempo UnionFindCheck con QuickFind in grafo con ciclo
    tempoDFSC=[]           #tempo DfsCheck in grafo con ciclo
    tempoUFQUWC = []       #tempo UnionFindCheck con QuickUnion in grafo senza ciclo
    tempoUFQFWC = []       #tempo UnionFindCheck con QuickFind in grafo senza ciclo
    tempoDFSWC = []        #tempo DfsCheck grafo senza ciclo
    tempoUFQUBC=[]         #tempo UnionFindCheck con QuickUnionBalanced in grafo con ciclo
    tempoUFQUBWC=[]        #tempo UnionFindCheck con QuickUnionBalanced in grafo senza ciclo
    tempoUFQFBWC=[]        #tempo UnionFindCheck con QuickFindBalanced in grafo senza ciclo
    tempoUFQFBC=[]         #tempo UnionFindCheck con QuickFindBalanced in grafo con ciclo
    tempoUFQUBPCC=[]       #tempo UnionFindCheck con QuickUnionBalancedPathCompression in grafo con ciclo
    tempoUFQUBPSC=[]       #tempo UnionFindCheck con QuickUnionBalancedPathSplitting in grafo con ciclo
    tempoUFQUBPCWC = []    #tempo UnionFindCheck con QuickUnionBalancedPathCompression in grafo senza ciclo
    tempoUFQUBPSWC = []    #tempo UnionFindCheck con QuickUnionBalancedPathSplitting in grafo senza ciclo

    #dim=[5,10,25,50,100,250,500,1000,2500] #NB gia con n=1000 e 2500 la creazione del grafo è molto lenta
    #dim = [5, 10, 25, 50]                  # sono inseriti principalmente per fare i grafici
    dim=[0,1,2]  #NB per dim=0 nelle dfs vi è un controllo per ritornare sempre 0.0,(ma in realta potrebbe impiegare
    #un po per la chiamata)in quanto viene fatta una dfs da ogni nodo presi i tempi e fatta la media,altrimenti dividerebbe per 0

    #GRAFI CON CICLI

    for i in range(0,len(dim)):
        graph_C=creaGrafiRC(dim[i])

        # QUICKUNION BALANCED with PATH SPLITTING

        start = time()
        hasCycleUFQUBPS(graph_C[0], graph_C[1], dim[i])
        elapsed = time() - start
        tempoUFQUBPSC.append(elapsed)
        print("\nUFQuickUnionBalancedPathSplittingCheck time elapsed with graph (cycle) dimension:", dim[i], "-->", elapsed)

        # QUICKUNION BALANCED with PATH COMPRESSION

        start = time()
        hasCycleUFQUBPC(graph_C[0], graph_C[1], dim[i])
        elapsed = time() - start
        tempoUFQUBPCC.append(elapsed)
        print("\nUFQuickUnionBalancedPathCompressionCheck time elapsed with graph (cycle) dimension:", dim[i], "-->", elapsed)

        # QUICKUNION BALANCED

        start = time()
        hasCycleUFQUB(graph_C[0], graph_C[1], dim[i])
        elapsed = time() - start
        tempoUFQUBC.append(elapsed)
        print("\nUFQuickUnionBalancedCheck time elapsed with graph (cycle) dimension:", dim[i], "-->", elapsed)

        # QUICKFIND BALANCED

        start = time()
        hasCycleUFQFB(graph_C[0], graph_C[1], dim[i])
        elapsed = time() - start
        tempoUFQFBC.append(elapsed)
        print("\nUFQuickFindBalancedCheck time elapsed with graph (cycle) dimension:", dim[i], "-->", elapsed)

        #QUICKUNION

        start = time()
        hasCycleUFQU(graph_C[0], graph_C[1], dim[i])
        elapsed = time() - start
        tempoUFQUC.append(elapsed)
        print("\nUFQuickUnionCheck time elapsed with graph (cycle) dimension:", dim[i], "-->", elapsed)

        #QUICKFIND

        start=time()
        hasCycleUFQF(graph_C[0],graph_C[1],dim[i])
        elapsed=time()-start
        tempoUFQFC.append(elapsed)
        print("\nUFQuickFindCheck time elapsed with graph (cycle) dimension:", dim[i], "-->", elapsed)

        # DFS
        if dim[i]==0:
            elapsed=0.0
            tempoDFSC.append(elapsed)
            print("\nDFScheck avg time elapsed with graph (cycle) dimension:", dim[i], "-->", elapsed)
        else:
            start = time()
            hasCycleDfs(graph_C,dim[i])
            elapsed = (time() - start) / dim[i]
            tempoDFSC.append(elapsed)
            print("\nDFScheck avg time elapsed with graph (cycle) dimension:", dim[i], "-->", elapsed)

    # GRAFI SENZA CICLI

    for i in range(0, len(dim)):
        graph_WC = creaGrafiRWC(dim[i])

        # QUICKUNION BALANCED with PATH SPLITTING

        start = time()
        hasCycleUFQUBPS(graph_WC[0], graph_WC[1], dim[i])
        elapsed = time() - start
        tempoUFQUBPSWC.append(elapsed)
        print("\nUFQuickUnionBalancedPathSplittingCheck time elapsed with graph (not cycle) dimension:", dim[i], "-->",elapsed)

        # QUICKUNION BALANCED with PATH COMPRESSION

        start = time()
        hasCycleUFQUBPC(graph_WC[0], graph_WC[1], dim[i])
        elapsed = time() - start
        tempoUFQUBPCWC.append(elapsed)
        print("\nUFQuickUnionBalancedPathCompressionCheck time elapsed with graph (not cycle) dimension:", dim[i], "-->",elapsed)

        # QUICKUNION BALANCED

        start = time()
        hasCycleUFQUB(graph_WC[0], graph_WC[1], dim[i])
        elapsed = time() - start
        tempoUFQUBWC.append(elapsed)
        print("\nUFQuickUnionBalancedCheck time elapsed with graph (not cycle) dimension:", dim[i], "-->", elapsed)

        # QUICKFIND BALANCED

        start = time()
        hasCycleUFQFB(graph_WC[0], graph_WC[1], dim[i])
        elapsed = time() - start
        tempoUFQFBWC.append(elapsed)
        print("\nUFQuickFindBalancedCheck time elapsed with graph (not cycle) dimension:", dim[i], "-->", elapsed)

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
        if dim[i]==0:
            elapsed=0.0
            tempoDFSWC.append(elapsed)
            print("\nDFScheck avg time elapsed with graph (cycle) dimension:", dim[i], "-->", elapsed)
        else:
            start = time()
            hasCycleDfs(graph_WC,dim[i])
            elapsed = (time() - start) / dim[i]
            tempoDFSWC.append(elapsed)
            print("\nDFScheck avg time elapsed with graph (not cycle) dimension:", dim[i], "-->", elapsed)

    # ARRAY PER PYPLOT PRINT

    print("\nDFS cycle array",tempoDFSC)
    print("DFS without cycle array",tempoDFSWC)
    print("UFQuickUnion cycle array",tempoUFQUC)
    print("UFQuickUnion without cycle array", tempoUFQUWC)
    print("UFQuickUnionBalanced cycle array", tempoUFQUBC)
    print("UFQuickUnionBalanced without cycle array", tempoUFQUBWC)
    print("UFQuickFind cycle array", tempoUFQFC)
    print("UFQuickFind without cycle array", tempoUFQFWC)
    print("UFQuickFindBalanced cycle array", tempoUFQFC)
    print("UFQuickFindBalanced without cycle array", tempoUFQFBWC)
    print("UFQuickUnionBalancedPathCompression cycle array", tempoUFQUBPCC)
    print("UFQuickUnionBalancedPathCompression without cycle array", tempoUFQUBPCWC)
    print("UFQuickUnionBalancedPathSplitting cycle array", tempoUFQUBPSC)
    print("UFQuickUnionBalancedPathSplitting without cycle array", tempoUFQUBPSWC)



