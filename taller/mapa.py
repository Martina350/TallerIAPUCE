import textwrap
from pathlib import Path

DIRECCIONES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def cargar_mapa_texto(texto):
    limpio = textwrap.dedent(texto).strip()
    filas = [linea.strip() for linea in limpio.splitlines() if linea.strip()]
    if not filas:
        raise ValueError("El mapa esta vacio")

    ancho = len(filas[0])
    if any(len(fila) != ancho for fila in filas):
        raise ValueError("Las filas no tienen el mismo ancho")

    return [list(fila) for fila in filas]


def cargar_mapa_archivo(ruta):
    with open(ruta, encoding="utf-8") as f:
        return cargar_mapa_texto(f.read())


def buscar_simbolo(mapa, simbolo):
    for fila, datos in enumerate(mapa):
        for col, celda in enumerate(datos):
            if celda == simbolo:
                return (fila, col)
    raise ValueError(f"No hay {simbolo} en el mapa")


def es_libre(mapa, pos):
    fila, col = pos
    return mapa[fila][col] != "#"


def dentro(mapa, pos):
    fila, col = pos
    return 0 <= fila < len(mapa) and 0 <= col < len(mapa[0])


def vecinos(mapa, pos):
    fila, col = pos
    resultado = []
    for df, dc in DIRECCIONES:
        nuevo = (fila + df, col + dc)
        if dentro(mapa, nuevo) and es_libre(mapa, nuevo):
            resultado.append(nuevo)
    return resultado


def dibujar_camino(mapa, camino):
    copia = [fila[:] for fila in mapa]
    for fila, col in camino:
        if copia[fila][col] not in {"S", "G"}:
            copia[fila][col] = "*"
    return "\n".join("".join(fila) for fila in copia)
