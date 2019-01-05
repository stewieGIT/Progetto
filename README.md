<h2> Progetto </h2>

<strong>Algorithm</strong> 
Checks whether a Graph has a cycle 
procedure hasCycleUF(Graph G) → bool 
uf ← UnionFind 
for all unvisited (u, v) ∈ E(G) do 
  if uf.find(u) == uf.find(v) then cycle detected 
  else uf.union(u, v)
return no cycle present

<strong>Dato un grafo G connesso, non orientato e non pesato, implementare due algoritmi per determinare se G ha almeno un ciclo:</strong>

• <strong>hasCycleUF(G)</strong> che usa la struttura dati UnionFind come descritto in Algorithm 1 e un iterator per scandire tutti gli edge del grafo

• <strong>hasCycleDFS(G)</strong> che usa l’approccio della visita in profondità (Depth-First Search)

Dopo aver scelto l’implementazione di UnionFind (QuickFind, QuickUnion, ecc) che minimizza il tempo di esecuzione di hasCycleUF(G), confrontare il tempo di esecuzione dei due algoritmi al variare della dimensione del grafo di input. I dati degli esperimenti devono essere scritti su un file da un decorator di Python (applicato alle funzioni dei due algoritmi) con il formato n, t su ogni riga dove n è il numero di archi del grafo e t il tempo di esecuzione dell’algoritmo. Inoltre implementare un algoritmo che genera grafi con o senza cicli, da usare nella fase di testing.

