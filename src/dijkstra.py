from math import inf
from heap import MinHeap


def Dijkstra(G: dict[int, dict[int, float]], v: int = None) -> dict[int, float]:
    """Algoritmo de Dijkstra

    Args:
        G (dict): Dígrafo  ponderado
        v (int): Vértice inicial

    Returns:
        dict[int, float]: Mapa de caminhos mínimos

    Algorithm:
    ```
    para i ← 2, . . . , n faça
        c(i) ← ω(v1, vi)
    c(1) ← 0
    H ← {v1, v2, . . . , vn} % Inicializa heap H com V(G)
    enquanto H ̸= ∅ faça
        w ← vértice em H que minimiza c(w)
        para z ∈ N(w) ∩ H fa ̧ca
            se c(w) + ω(w, z) < c(z) ent ̃ao
                c(z) ← c(w) + ω(w, z)
                Atualizar c(z) em H
    ```
    """

    if not G:
        return None
    if not v:
        v = G.keys()[0]

    c = {i: G[v][i] if i in G[v] else inf for i in G}
    c[v] = 0

    H = MinHeap(c)

    while H:
        w = H.pop()
        for z in G[w]:
            if z in H:
                if c[z] > c(w) + G[w][z]:
                    c[z] = c(w) + G[w][z]
                    H.update(z, c[z])


A = {
    1: {
        2: 3,
        3: -4,
        5: 1
    },
    2: {
        1: -2,
        3: -5,
        5: 3
    },
    3: {
        4: 2
    },
    4: {1: 3},
    5: {
        2: 10,
        3: 1,
        4: 9
    }
}

print(*Dijkstra(A,1), sep='\n')