import random
import graph.Graph_AdjacencyList as grafo
from graph.Graph import GraphBase as visit

def creaGraf1(dim):
    random.seed(3)
    graph = grafo.GraphAdjacencyList()

    graph.print()

    # add nodes
    nodes = []
    for i in range(dim):
        node = graph.addNode(random.randint(0,100))
        print("Node inserted [key:value]:", node)
        nodes.append(node)
    graph.print()
    edges=[]
    arcListWD=[]
    # MANUAL CYCLE
    node_src = nodes[0]
    node_dst = nodes[1]
    arcListWD.append([node_src.id,node_dst.id])
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

    node_src = nodes[0]
    node_dst = nodes[4]
    arcListWD.append([node_src.id,node_dst.id])
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

    node_src = nodes[2]
    node_dst = nodes[3]
    arcListWD.append([node_src.id,node_dst.id])
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

    node_src = nodes[0]
    node_dst = nodes[2]
    arcListWD.append([node_src.id,node_dst.id])
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

    node_src = nodes[1]
    node_dst = nodes[2]
    arcListWD.append([node_src.id,node_dst.id])
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
    
    a=[]
    a.append(graph)
    a.append(arcListWD)
    return a

def creaGraf2(dim):
    random.seed(3)
    graph = grafo.GraphAdjacencyList()

    graph.print()

    # add nodes
    nodes = []
    for i in range(dim):
        node = graph.addNode(random.randint(0,100))
        print("Node inserted [key:value]:", node)
        nodes.append(node)
    graph.print()
    edges=[]
    arcListWD=[]
    # MANUAL CYCLE
    node_src = nodes[0]
    node_dst = nodes[1]
    arcListWD.append([node_src.id,node_dst.id])
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

    node_src = nodes[0]
    node_dst = nodes[4]
    arcListWD.append([node_src.id,node_dst.id])
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

    node_src = nodes[2]
    node_dst = nodes[3]
    arcListWD.append([node_src.id,node_dst.id])
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

    node_src = nodes[0]
    node_dst = nodes[2]
    arcListWD.append([node_src.id,node_dst.id])
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

    a=[]
    a.append(graph)
    a.append(arcListWD)
    return a

def creaGraf3(dim):
    random.seed(3)
    graph = grafo.GraphAdjacencyList()
    graph.print()

    # add nodes
    nodes = []
    for i in range(dim):
        node = graph.addNode(random.randint(0,100))
        print("Node inserted [key:value]:", node)
        nodes.append(node)
    graph.print()
    edges=[]
    arcListWD=[]
    # MANUAL CYCLE
    node_src = nodes[0]
    node_dst = nodes[1]
    arcListWD.append([node_src.id,node_dst.id])
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

    node_src = nodes[1]
    node_dst = nodes[2]
    arcListWD.append([node_src.id,node_dst.id])
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

    node_src = nodes[2]
    node_dst = nodes[3]
    arcListWD.append([node_src.id,node_dst.id])
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

    node_src = nodes[3]
    node_dst = nodes[4]
    arcListWD.append([node_src.id,node_dst.id])
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

    a=[]
    a.append(graph)
    a.append(arcListWD)
    return a


def creaGraf4(dim):
    random.seed(3)
    graph = grafo.GraphAdjacencyList()

    graph.print()

    # add nodes
    nodes = []
    for i in range(dim):
        node = graph.addNode(random.randint(0,100))
        print("Node inserted [key:value]:", node)
        nodes.append(node)
    graph.print()
    edges=[]
    arcListWD=[]
    # MANUAL CYCLE
    node_src = nodes[0]
    node_dst = nodes[1]
    arcListWD.append([node_src.id,node_dst.id])
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

    node_src = nodes[1]
    node_dst = nodes[2]
    arcListWD.append([node_src.id,node_dst.id])
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

    node_src = nodes[2]
    node_dst = nodes[0]
    arcListWD.append([node_src.id,node_dst.id])
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

    # connect all nodes
    for i in range(0,2):
            node_src=random.choice(nodes)
            node_dst=random.choice(nodes)
            if node_src != node_dst:
                arcListWD.append([node_src.id,node_dst.id])
                edges.append([node_src, node_dst])
                edges.append([node_dst, node_src])
                if edges.count([node_src,node_dst])==1 :
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

    a=[]
    a.append(graph)
    a.append(arcListWD)
    return a

