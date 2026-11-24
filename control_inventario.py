# Nombre del estudiante: Ingrid Lorena López Olarte
# Grupo: 213022_1093
# Programa: Ingeniería de Sistemas
# Curso: Fundamentos de Programación
# Problema 3: Control de inventario y reabastecimiento (Fase 5 - POA)


def calcular_cantidad_pedir(stock_actual, stock_minimo):
    """
    Calcula la cantidad exacta de unidades que se deben solicitar.

    Si el stock actual es menor que el stock mínimo requerido,
    retorna la diferencia. En caso contrario, retorna 0.
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


def mostrar_informe_reabastecimiento(inventario):
    """Recorre la matriz y muestra cada artículo y su cantidad a solicitar."""
    ancho = 55

    print("=" * ancho)
    print("INFORME DE REABASTECIMIENTO DE INVENTARIO".center(ancho))
    print("=" * ancho)
    print(f"{'Artículo':<30} | {'Cantidad a solicitar':>22}")
    print("-" * ancho)

    for articulo in inventario:
        # Formato: [Código, Nombre, Stock actual, Stock mínimo]
        nombre_articulo = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        cantidad_pedir = calcular_cantidad_pedir(
            stock_actual, stock_minimo
        )

        print(f"{nombre_articulo:<30} | {cantidad_pedir:>22}")

    print("=" * ancho)


def main():
    # Matriz de inventario con 6 artículos (mínimo requerido: 5).
    # Formato: [Código, Nombre, Stock actual, Stock mínimo requerido]

    matriz_inventario = [
        ["ART-001", "Teclado Mecánico", 8, 15],
        ["ART-002", "Mouse ", 20, 12],
        ["ART-003", "Monitor", 5, 10],
        ["ART-004", "Audífonos", 10, 10],
        ["ART-005", "Memoria USB 64GB", 3, 25],
        ["ART-006", "Cable HDMI 2m", 18, 10]
    ]

    mostrar_informe_reabastecimiento(matriz_inventario)


if __name__ == "__main__":
    main()