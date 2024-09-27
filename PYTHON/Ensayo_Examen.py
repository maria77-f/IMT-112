import Funciones
def main():
    matriz= Funciones.ingresar_matriz()
    Funciones.mostrar_matriz(matriz)
    total= Funciones.suma_total(matriz)
    print(f"Suma total de los elementos: {total}")
    Funciones.suma_filas_columnas(matriz)
    Funciones.maximo_minimo(matriz)

main()
