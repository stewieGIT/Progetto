import random
import graph.Graph_AdjacencyList as grafo
from graph.Graph import GraphBase as visit

# questo file genera grafi a caso e ne fa dfsCycleCheck
# cambiando numero archi,vertici e seed si generano grafi diversi con o senza cicli (a caso)

def cacaGrafi(dim):
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
    edges=[]
    # connect all nodes
    for i in range(0,dim**2):
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
    nodi = cacaGrafi(5)
    nodes=nodi.getNodes()
    for node in nodes:       #viene fatta la dfs da ogni nodo per questo avviene più volte la print cè/non cè ciclo
        s = nodi.dfs(node.id)
        # NB la dfs e' una modifica di quella dei tutor  nel file Graph.py della cartella graph

