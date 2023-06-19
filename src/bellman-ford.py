from math import inf


def Bellman_Ford(G: dict[int, dict[int, float]], v: int) -> dict[int, float]:
    """Algoritmo de Bellman-Ford. (versão de Szwarcfiter[2018])

    Args:
        G (dict): Dígrafo D = (V, E), matriz de pesos ω e livre de ciclos negativos
        v (int): _description_

    Returns:
        dict[int, float]: Valor de distância c(n - 1, i) a cada vi ∈ V .

    Algorithm:
    ```
    ...
    ```
    """