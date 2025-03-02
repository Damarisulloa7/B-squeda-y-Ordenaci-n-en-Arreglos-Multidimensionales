def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Devuelve posición (fila, columna)
    return None

# Matriz 3x3 de ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

valor_buscar = 5  # Valor a buscar
resultado = buscar_valor(matriz, valor_buscar)

# Mostrar resultados
print("=== Búsqueda en Matriz Bidimensional ===")
print("\nMatriz original:")
for fila in matriz:
    print(fila)

if resultado:
    print(f"\n✅ El valor {valor_buscar} se encontró en la posición (fila {resultado[0]}, columna {resultado[1]})")
else:
    print(f"\n❌ El valor {valor_buscar} no existe en la matriz")
