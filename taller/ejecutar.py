from pathlib import Path

from taller.astar_mapa import astar_mapa
from taller.bfs_grafo import bfs_grafo
from taller.bfs_mapa import bfs_mapa
from taller.comparar import comparar_en_mapa
from taller.depuracion import seccion
from taller.dfs_grafo import dfs_grafo
from taller.dfs_mapa import dfs_mapa
from taller.grafo import GRAFO_EJEMPLO, analizar_grafo
from taller.mapa import buscar_simbolo, cargar_mapa_archivo, vecinos

MAPAS = Path(__file__).resolve().parent / "mapas"


def main():
    seccion("Fase 1 - grafo")
    analizar_grafo(GRAFO_EJEMPLO)

    seccion("Fase 2 - BFS grafo")
    print(bfs_grafo(GRAFO_EJEMPLO, "A", "F", depurar=True))

    seccion("Fase 3 - DFS grafo")
    print(dfs_grafo(GRAFO_EJEMPLO, "A", "F", depurar=True))

    mapa_simple = cargar_mapa_archivo(MAPAS / "mapa_simple.txt")
    seccion("Fase 4 - mapa")
    inicio = buscar_simbolo(mapa_simple, "S")
    print("S:", inicio)
    print("G:", buscar_simbolo(mapa_simple, "G"))
    print("vecinos de S:", vecinos(mapa_simple, inicio))

    mapa = cargar_mapa_archivo(MAPAS / "mapa_obstaculos.txt")
    seccion("Fase 5 - A*")
    print(astar_mapa(mapa, depurar=True))

    seccion("Comparacion BFS / DFS / A*")
    comparar_en_mapa(mapa, {"BFS": bfs_mapa, "DFS": dfs_mapa, "A*": astar_mapa})


if __name__ == "__main__":
    main()
