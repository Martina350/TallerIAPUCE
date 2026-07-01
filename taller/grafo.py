GRAFO_EJEMPLO = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}


def reconstruir_camino(padres, inicio, meta):
    if meta not in padres:
        return []

    camino = []
    actual = meta
    while actual is not None:
        camino.append(actual)
        actual = padres[actual]

    camino.reverse()
    if camino and camino[0] == inicio:
        return camino
    return []


def analizar_grafo(grafo):
    print("Vecinos de A:", grafo["A"])

    sin_salida = [nodo for nodo, lista in grafo.items() if not lista]
    print("Nodos sin salida:", sin_salida)

    rutas = [["A", "B", "E", "F"], ["A", "C", "F"]]
    print("Rutas de A a F:", rutas)
