from collections import deque

from taller.depuracion import traza
from taller.grafo import reconstruir_camino


def bfs_grafo(grafo, inicio, meta, depurar=False):
    cola = deque([inicio])
    visitados = {inicio}
    padres = {inicio: None}

    while cola:
        actual = cola.popleft()

        if depurar:
            print("\n[BFS]")
            traza(actual, cola, visitados)

        if actual == meta:
            return reconstruir_camino(padres, inicio, meta)

        for vecino in grafo[actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = actual
                cola.append(vecino)
                if depurar:
                    print(f"  vecino {vecino}, padre {actual}")

    return []
