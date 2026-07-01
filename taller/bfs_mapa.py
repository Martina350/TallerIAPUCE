from collections import deque

from taller.depuracion import traza
from taller.grafo import reconstruir_camino
from taller.mapa import buscar_simbolo, vecinos


def bfs_mapa(mapa, inicio=None, meta=None, depurar=False):
    inicio = inicio or buscar_simbolo(mapa, "S")
    meta = meta or buscar_simbolo(mapa, "G")

    cola = deque([inicio])
    visitados = {inicio}
    padres = {inicio: None}

    while cola:
        actual = cola.popleft()

        if depurar:
            print("\n[BFS mapa]")
            traza(actual, cola, visitados, vecinos=vecinos(mapa, actual))

        if actual == meta:
            return reconstruir_camino(padres, inicio, meta)

        for vecino in vecinos(mapa, actual):
            if vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = actual
                cola.append(vecino)
                if depurar:
                    print(f"  vecino {vecino}, padre {actual}")

    return []
