def seccion(titulo):
    print("\n" + "=" * 60)
    print(titulo)
    print("=" * 60)


def traza(nodo, frontera, visitados, vecinos=None, padre=None, costo=None):
    print(f"  actual:   {nodo}")
    print(f"  frontera: {list(frontera)}")
    print(f"  visitados:{set(visitados)}")
    if vecinos is not None:
        print(f"  vecinos:  {list(vecinos)}")
    if padre is not None:
        print(f"  padre:    {padre}")
    if costo is not None:
        print(f"  costo g:  {costo}")


def validar_camino(camino, inicio, meta):
    if not camino:
        raise ValueError("camino vacio")
    if camino[0] != inicio or camino[-1] != meta:
        raise ValueError("el camino no va de inicio a meta")
    print("camino ok")
