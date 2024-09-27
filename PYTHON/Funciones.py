def ingresar_matriz():
    matriz=[]
    print("Ingresa los elementos de la matriz (3x3): ")
    for i in range (3):
        fila=[]
        for j in range (3):
            valor=int(input(f"Elemento [{i+1}][{j+1}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    print("Matriz ingresada:")
    for fila in matriz: 
        for elemento in fila:
            print(f"{elemento}", end=" ")
        print()

def suma_total(matriz):
    total=0
    for fila in matriz:
        total+=sum(fila)
    return total

def suma_filas_columnas(matriz):
    suma_filas=[sum(fila) for fila in matriz]
    suma_columnas=[sum([matriz[i][j] for i in range(3)]) for j in range(3)]
    print(f"Suma de cada fila: {suma_filas}")
    print(f"Suma de cada fila: {suma_columnas}")

def maximo_minimo(matriz):
    maximo=max(max(fila) for fila in matriz)
    minimo=min(min(fila) for fila in matriz)
    print(f"Número máximo: {maximo}: ")
    print(f"Número mínimo: {minimo}: ")

def main():
    matriz=ingresar_matriz()
    mostrar_matriz(matriz)
    total=suma_total(matriz)
    print(f"Suma total de los elementos: {total}")
    suma_filas_columnas(matriz)
    maximo_minimo(matriz)

main()