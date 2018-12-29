import random
import graph.Graph_AdjacencyList as grafo
from graph.Graph import GraphBase as visit

# ***** in questo file ci sono i codici che generano due grafi con un ciclo manualmente e ne fa dfsCycleCheck *****
# uno dei due è completamente manuale l'altro fa il ciclo manualmente e il resto a caso
# se si cambia seed dimensione del grafo o numero di archi potrebbero esserci piu cicli nel secondo
def cacaGrafi(dim):
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
    return graph




if __name__ == "__main__":
    nodi=cacaGrafi(5)
    nodes=nodi.getNodes()
    for node in nodes:       #viene fatta la dfs da ogni nodo per questo avviene più volte la print cè/non cè ciclo
        s = nodi.dfs(node.id)
        # NB la dfs e' una modifica di quella dei tutor  nel file Graph.py della cartella graph





#piu giu un altro possibile grafo con ciclo











"""def cacaGrafi(dim):
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

    return graph"""
