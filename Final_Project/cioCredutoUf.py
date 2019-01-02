import random
from unionfind.quickFind import QuickFind
from unionfind.quickUnion import QuickUnion
import graph.Graph_AdjacencyList as grafo
from graph.Graph import GraphBase, Edge, Node
from list.DoubleLinkedList import ListaDoppiamenteCollegata as List
from CacaGrafi import cacaGrafi

"""
class edgeIter:

    def __init__(self):
        self.ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = edges[self.ind]
        self.ind += 1
        return value
"""

def hasCycleUF(graph,arcList):
    uf=QuickUnion()
    nodes=graph.getNodes()
    for n in nodes:
        uf.makeSet(n)
    uf.print()

    edges=graph.getEdges()

    for i in range(0,len(arcList)-1):
        a=arcList[i][0]
        b=arcList[i][1]
        u=uf.nodes[a]
        v=uf.nodes[b]
        print("u: ", u)
        print("v: ", v)
        print("a: ", a)
        print("b: ", b)
        print("find(u): ", uf.find(u))
        print("find(v): ", uf.find(v))

        if uf.find(u) == uf.find(v):
            print("Cycle detected!")
            return
        else:
            uf.union(u, v)
            print("else union")
            uf.print()
    print("NO cycle detected.")
    return



if __name__ == "__main__":

###cacagrafi
    dim=5


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

    """
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
    """

    """
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
    """

    """
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
    """
###hascycleUF

    hasCycleUF(graph,arcListWD)