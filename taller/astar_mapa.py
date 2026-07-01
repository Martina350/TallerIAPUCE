import heapq

from taller.depuracion import traza
from taller.grafo import reconstruir_camino
from taller.mapa import buscar_simbolo, vecinos


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar_mapa(mapa, inicio=None, meta=None, depurar=False):
    inicio = inicio or buscar_simbolo(mapa, "S")
    meta = meta or buscar_simbolo(mapa, "G")

    frontera = []
    heapq.heappush(frontera, (0, inicio))

    padres = {inicio: None}
    costo = {inicio: 0}

    while frontera:
        _, actual = heapq.heappop(frontera)

        if depurar:
            print("\n[A*]")
            traza(
                actual,
                [p for _, p in frontera],
                costo.keys(),
                vecinos=vecinos(mapa, actual),
                costo=costo[actual],
            )

        if actual == meta:
            return reconstruir_camino(padres, inicio, meta)

        for vecino in vecinos(mapa, actual):
            nuevo = costo[actual] + 1
            if vecino not in costo or nuevo < costo[vecino]:
                costo[vecino] = nuevo
                f = nuevo + manhattan(vecino, meta)
                heapq.heappush(frontera, (f, vecino))
                padres[vecino] = actual
                if depurar:
                    print(f"  vecino {vecino} g={nuevo} f={f} padre {actual}")

    return []
