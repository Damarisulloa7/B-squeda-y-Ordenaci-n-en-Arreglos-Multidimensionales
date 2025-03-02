def ordenar_fila(matriz, fila):
    # Usamos Bubble Sort para ordenar la fila
    n = len(matriz[fila])
    for i in range(n - 1):
        for j in range(n - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                # Intercambiar elementos
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]

# Matriz 3x3 de ejemplo.
matriz = [
    [9, 5, 7],
    [4, 2, 1],
    [6, 8, 3]
]

fila_a_ordenar = 1  # Índice basado en 0 (0 = primera fila)

# Mostrar matriz original
print("=== Ordenación de Fila en Matriz ===")
print("\nMatriz original:")
for fila in matriz:
    print(fila)

# Ordenar la fila seleccionada
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar matriz modificada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
