import random
import graph.Graph_AdjacencyList as grafo

def cacaGrafi(dim):
    graph = grafo.GraphAdjacencyList()

    graph.print()

    # add nodes
    nodes = []
    for i in range(dim):
        node = graph.addNode(random.randint(0,100))
        print("Node inserted:", node)
        nodes.append(node)

    graph.print()

    # connect all nodes
    for node_src in nodes:
        for node_dst in nodes:
            if node_src != node_dst:
                print("---")
                print("Adjacent nodes {},{}: {}".format(node_src.id, node_dst.id,graph.isAdj(node_src.id, node_dst.id)))
                graph.insertEdge(node_src.id, node_dst.id,node_src.id + node_dst.id)
                print("Edge inserted: from {} to {}".format(node_src.id,node_dst.id))
                print("Adjacent nodes {},{}: {}".format(node_src.id, node_dst.id,graph.isAdj(node_src.id, node_dst.id)))
                graph.print()
                print("---")

    # num nodes/edges
    print("Num Nodes:", graph.numNodes())
    print("Num Edges with doubles :", graph.numEdges())


if __name__ == "__main__":
    cacaGrafi(3)

