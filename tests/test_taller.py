from pathlib import Path

from taller.astar_mapa import astar_mapa
from taller.bfs_grafo import bfs_grafo
from taller.bfs_mapa import bfs_mapa
from taller.dfs_grafo import dfs_grafo
from taller.dfs_mapa import dfs_mapa
from taller.grafo import GRAFO_EJEMPLO
from taller.mapa import buscar_simbolo, cargar_mapa_archivo, vecinos

MAPAS = Path(__file__).resolve().parents[1] / "taller" / "mapas"


def test_bfs_grafo():
    assert bfs_grafo(GRAFO_EJEMPLO, "A", "F") == ["A", "C", "F"]


def test_dfs_grafo():
    camino = dfs_grafo(GRAFO_EJEMPLO, "A", "F")
    assert camino[0] == "A" and camino[-1] == "F"


def test_mapa():
    mapa = cargar_mapa_archivo(MAPAS / "mapa_simple.txt")
    assert buscar_simbolo(mapa, "S") == (0, 0)
    assert (0, 1) in vecinos(mapa, (0, 0))


def test_bfs_mapa():
    mapa = cargar_mapa_archivo(MAPAS / "mapa_obstaculos.txt")
    camino = bfs_mapa(mapa)
    assert camino[0] == buscar_simbolo(mapa, "S")
    assert camino[-1] == buscar_simbolo(mapa, "G")


def test_astar_mapa():
    mapa = cargar_mapa_archivo(MAPAS / "mapa_obstaculos.txt")
    assert len(astar_mapa(mapa)) == len(bfs_mapa(mapa))


def test_dfs_mapa():
    mapa = cargar_mapa_archivo(MAPAS / "mapa_obstaculos.txt")
    assert dfs_mapa(mapa)[-1] == buscar_simbolo(mapa, "G")
