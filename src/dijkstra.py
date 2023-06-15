from heap import Heap

def Dijkstra(D: tuple[list[int]], w: tuple[tuple[int]]) -> Heap:
    ...


"""
para i ← 2, . . . , n faça
    c(i) ← ω(v1, vi);
c(1) ← 0;
H ← {v1, v2, . . . , vn} % Inicializa heap H com V (G);
enquanto H ̸= ∅ fa ̧ca
    w ← vértice em H que minimiza c(w);
    para z ∈ N(w) ∩ H fa ̧ca
        se c(w) + ω(w, z) < c(z) ent ̃ao
            c(z) ← c(w) + ω(w, z);
            Atualizar c(z) em H;
"""
