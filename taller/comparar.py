from taller.mapa import dibujar_camino


def comparar_en_mapa(mapa, algoritmos):
    print("\n| Algoritmo | Encontro | Longitud | Nota |")
    print("|-----------|----------|----------|------|")

    for nombre, funcion in algoritmos.items():
        camino = funcion(mapa)
        encontro = "si" if camino else "no"
        largo = len(camino) if camino else 0

        if nombre == "BFS":
            nota = "camino mas corto"
        elif nombre == "DFS":
            nota = "puede ser mas largo"
        elif nombre == "A*":
            nota = "optimo con manhattan"
        else:
            nota = ""

        print(f"| {nombre:<9} | {encontro:<8} | {largo:<8} | {nota} |")

        if camino:
            print(f"\n  {nombre}: {camino}")
            print(dibujar_camino(mapa, camino))
            print()
