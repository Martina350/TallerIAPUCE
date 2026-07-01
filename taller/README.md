# Taller: BFS, DFS y A* en Python

Implementacion del taller descrito en `TALLER.md`. Este codigo vive aparte del material de referencia en `src/`.

## Contenido del entregable

| Requisito | Ubicacion |
|---|---|
| Codigo funcional BFS, DFS y A* | `bfs_grafo.py`, `dfs_grafo.py`, `bfs_mapa.py`, `dfs_mapa.py`, `astar_mapa.py` |
| Dos mapas de prueba | `mapas/mapa_simple.txt`, `mapas/mapa_obstaculos.txt` |
| Salida de consola | `python -m taller.ejecutar` |
| Como ejecutar | Este archivo |
| Reflexion final | Seccion al final |

## Estructura

```text
taller/
├── README.md
├── ejecutar.py          # corre todas las fases
├── grafo.py             # grafo de ejemplo y reconstruccion de camino
├── bfs_grafo.py         # BFS en grafo
├── dfs_grafo.py         # DFS en grafo
├── mapa.py              # carga de mapas y vecinos
├── bfs_mapa.py          # BFS en mapa
├── dfs_mapa.py          # DFS en mapa
├── astar_mapa.py        # A* en mapa
├── depuracion.py        # trazas de depuracion
├── comparar.py          # tabla comparativa
└── mapas/
    ├── mapa_simple.txt
    └── mapa_obstaculos.txt
```

## Instalacion

Desde la raiz del repositorio:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

Instalar el proyecto en modo editable:

```bash
pip install -e .
```

## Como ejecutar

Correr todo el taller con trazas y comparacion:

```bash
python -m taller.ejecutar
```

Guardar la salida en un archivo (para la captura del entregable):

```bash
python -m taller.ejecutar > salida.txt
```

Ejecutar las pruebas del taller:

```bash
pytest tests/test_taller.py
```

## Mapas de prueba

Simbolos usados:

| Simbolo | Significado |
|---|---|
| `S` | Inicio |
| `G` | Meta |
| `.` | Celda libre |
| `#` | Obstaculo |

**mapa_simple.txt** — mapa abierto de 4x5, sin obstaculos.

**mapa_obstaculos.txt** — mapa de 6x7 con varios obstaculos.

## Algoritmos implementados

| Algoritmo | Archivo | Donde se usa |
|---|---|---|
| BFS | `bfs_grafo.py`, `bfs_mapa.py` | Grafo y mapa |
| DFS | `dfs_grafo.py`, `dfs_mapa.py` | Grafo y mapa |
| A* | `astar_mapa.py` | Mapa con heuristica Manhattan |

## Resultados en mapa_obstaculos.txt

| Algoritmo | Encontro camino | Longitud | Nota |
|---|---|---:|---|
| BFS | si | 12 | camino mas corto |
| DFS | si | 22 | puede ser mas largo |
| A* | si | 12 | optimo con Manhattan |

En el grafo de ejemplo (`A` a `F`):

- BFS: `['A', 'C', 'F']` (3 nodos, camino mas corto)
- DFS: `['A', 'B', 'E', 'F']` (4 nodos)

## Parte A: comprension

1. **Por que BFS encuentra el camino mas corto en grafos sin pesos?**  
   Porque explora por niveles: primero todos los nodos a distancia 1, luego a distancia 2, y asi. La primera vez que llega a la meta, lo hizo con el menor numero de pasos posible.

2. **Por que DFS puede encontrar una ruta mas larga?**  
   Porque se mete profundo en una rama antes de probar otras. Puede llegar a la meta por un camino largo aunque exista uno mas corto en otra rama.

3. **Que ventaja tiene A* frente a BFS?**  
   Con una buena heuristica, A* prioriza nodos que parecen mas cercanos a la meta. En mapas grandes suele visitar menos celdas que BFS y aun asi encontrar el camino optimo.

4. **Que ocurre si la heuristica sobreestima el costo real?**  
   A* puede dejar de ser optimo: podria ignorar caminos mas baratos porque la estimacion los hace ver peores de lo que son.

5. **Por que es util imprimir la frontera durante la depuracion?**  
   Permite ver que nodos faltan por explorar y detectar si un nodo entra varias veces, si la frontera crece demasiado o si el algoritmo se queda atascado.

## Parte B: programacion

| Tarea | Estado | Archivo |
|---|---|---|
| BFS en grafo | listo | `bfs_grafo.py` |
| DFS en grafo | listo | `dfs_grafo.py` |
| BFS en mapa | listo | `bfs_mapa.py` |
| A* en mapa | listo | `astar_mapa.py` |
| Comparacion de resultados | listo | `comparar.py` + `ejecutar.py` |

## Parte C: depuracion

Las trazas estan en `depuracion.py` y se activan con `depurar=True`. Muestran:

- nodo actual
- frontera (cola, pila o prioridad)
- visitados
- vecinos validos
- padre asignado
- costo acumulado `g` en A*

Ejemplo de uso:

```python
from taller.bfs_grafo import bfs_grafo
from taller.grafo import GRAFO_EJEMPLO

bfs_grafo(GRAFO_EJEMPLO, "A", "F", depurar=True)
```

## Ejemplo de salida (resumen)

```text
Fase 2 - BFS grafo
['A', 'C', 'F']

Fase 3 - DFS grafo
['A', 'B', 'E', 'F']

Comparacion BFS / DFS / A*
| BFS       | si       | 12       | camino mas corto |
| DFS       | si       | 22       | puede ser mas largo |
| A*        | si       | 12       | optimo con manhattan |
```

Para ver la salida completa con trazas, ejecutar `python -m taller.ejecutar`.

## Reflexion final

El algoritmo mas facil de depurar fue BFS, porque la cola hace predecible el orden de exploracion: siempre se revisa el nodo mas antiguo primero. Con las trazas de frontera y visitados se ve rapido si un vecino se agrega dos veces o si el camino se reconstruye mal.

El error que mas aparecio fue marcar nodos como visitados tarde o no guardar bien el diccionario de padres. En un intento inicial el mismo nodo entraba varias veces a la frontera y el camino reconstruido no llegaba al inicio. Revisar capa por capa — primero el mapa, luego vecinos, luego visitados — ayudo a aislar el problema.

Usaria BFS cuando todos los movimientos cuestan igual y necesito el camino mas corto, como en un laberinto sin pesos. DFS lo usaria si solo me importa encontrar alguna solucion y el espacio de busqueda es manejable. A* lo elegiria en mapas grandes con obstaculos, porque con Manhattan visita menos nodos que BFS y sigue dando el camino optimo en este tipo de mapa.
