import random
import graph.Graph_AdjacencyList as grafo

# In questo file vengono generati grafi random con e senza cicli per la fase di testing

# Viene creato un grafo con ciclo in cui ogni vertuce ha un arco col successivo e l'ultimo vertice ne ha uno con il primo

def creaGrafiRC(dim):
    random.seed(2)
    graph = grafo.GraphAdjacencyList()

    graph.print()

    # add nodes
    nodes = []
    for i in range(dim):
        node = graph.addNode(random.randint(0,100))
        print("Node inserted [key:value]:", node)
        nodes.append(node)

    graph.print()
    edges = []  # lista degli archi considerando (u,v) e (v,u)
    arcListWD = []  # lista degli archi considerando solo (u,v)
    # connect all nodes
    for i in range(0,dim-1):           # NB range(0,numeroArchi)
            node_src = nodes[i]
            node_dst = nodes[i + 1]
            arcListWD.append([node_src.id, node_dst.id])
            edges.append([node_src, node_dst])
            edges.append([node_dst, node_src])
            print("---")
            print("Adjacent nodes {},{}: {}".format(node_src.id, node_dst.id,graph.isAdj(node_src.id, node_dst.id)))
            graph.insertEdge(node_src.id, node_dst.id,node_src.id + node_dst.id)
            graph.insertEdge(node_dst.id, node_src.id, node_src.id + node_dst.id)
            print("Edge inserted: from {} to {}".format(node_src.id,node_dst.id))
            print("Adjacent nodes {},{}: {}".format(node_src.id, node_dst.id,graph.isAdj(node_src.id, node_dst.id)))
            graph.print()
            print("---")
    node_src = nodes[dim-1]
    node_dst = nodes[0]
    arcListWD.append([node_src.id, node_dst.id])
    edges.append([node_src, node_dst])
    edges.append([node_dst, node_src])
    print("---")
    print("Adjacent nodes {},{}: {}".format(node_src.id, node_dst.id, graph.isAdj(node_src.id, node_dst.id)))
    graph.insertEdge(node_src.id, node_dst.id, node_src.id + node_dst.id)
    graph.insertEdge(node_dst.id, node_src.id, node_src.id + node_dst.id)
    print("Edge inserted: from {} to {}".format(node_src.id, node_dst.id))
    print("Adjacent nodes {},{}: {}".format(node_src.id, node_dst.id, graph.isAdj(node_src.id, node_dst.id)))
    graph.print()
    print("---")

    # num nodes/edges
    print("Num Nodes:", graph.numNodes())
    print("Num Edges with doubles :", graph.numEdges())
    a = []
    a.append(graph)
    a.append(arcListWD)
    return a

# crea grafi senza cicli (grafo lineare ogni vertice ha un arco con il successivo tranne l'ultimo)
# i cui vertici hanno chiave random

def creaGrafiRWC(dim):
    random.seed(2)
    graph = grafo.GraphAdjacencyList()

    graph.print()

    # add nodes
    nodes = []
    for i in range(dim):
        node = graph.addNode(random.randint(0,100))
        print("Node inserted [key:value]:", node)
        nodes.append(node)

    graph.print()
    edges = []  # lista degli archi considerando (u,v) e (v,u)
    arcListWD = []  # lista degli archi considerando solo (u,v)
    # connect all nodes
    for i in range(0,dim-1):           # NB range(0,numeroArchi)
            node_src=nodes[i]
            node_dst=nodes[i+1]
            arcListWD.append([node_src.id, node_dst.id])
            edges.append([node_src, node_dst])
            edges.append([node_dst, node_src])
            print("---")
            print("Adjacent nodes {},{}: {}".format(node_src.id, node_dst.id,graph.isAdj(node_src.id, node_dst.id)))
            graph.insertEdge(node_src.id, node_dst.id,node_src.id + node_dst.id)
            graph.insertEdge(node_dst.id, node_src.id, node_src.id + node_dst.id)
            print("Edge inserted: from {} to {}".format(node_src.id,node_dst.id))
            print("Adjacent nodes {},{}: {}".format(node_src.id, node_dst.id,graph.isAdj(node_src.id, node_dst.id)))
            graph.print()
            print("---")

    # num nodes/edges
    print("Num Nodes:", graph.numNodes())
    print("Num Edges with doubles :", graph.numEdges())
    a = []
    a.append(graph)
    a.append(arcListWD)
    return a
