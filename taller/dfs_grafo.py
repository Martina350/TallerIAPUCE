from taller.depuracion import traza
from taller.grafo import reconstruir_camino


def dfs_grafo(grafo, inicio, meta, depurar=False):
    pila = [inicio]
    visitados = {inicio}
    padres = {inicio: None}

    while pila:
        actual = pila.pop()

        if depurar:
            print("\n[DFS]")
            traza(actual, pila, visitados)

        if actual == meta:
            return reconstruir_camino(padres, inicio, meta)

        for vecino in reversed(grafo[actual]):
            if vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = actual
                pila.append(vecino)
                if depurar:
                    print(f"  vecino {vecino}, padre {actual}")

    return []
