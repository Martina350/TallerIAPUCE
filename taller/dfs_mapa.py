from taller.depuracion import traza
from taller.grafo import reconstruir_camino
from taller.mapa import buscar_simbolo, vecinos


def dfs_mapa(mapa, inicio=None, meta=None, depurar=False):
    inicio = inicio or buscar_simbolo(mapa, "S")
    meta = meta or buscar_simbolo(mapa, "G")

    pila = [inicio]
    visitados = {inicio}
    padres = {inicio: None}

    while pila:
        actual = pila.pop()

        if depurar:
            print("\n[DFS mapa]")
            traza(actual, pila, visitados, vecinos=vecinos(mapa, actual))

        if actual == meta:
            return reconstruir_camino(padres, inicio, meta)

        for vecino in reversed(vecinos(mapa, actual)):
            if vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = actual
                pila.append(vecino)
                if depurar:
                    print(f"  vecino {vecino}, padre {actual}")

    return []
