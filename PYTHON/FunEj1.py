import random
import time 
def ingresar_lista():
    lista = []  # Lista vacía para almacenar los números únicos ingresados
    print("Ingresa números para la lista (escribe 'fin' para terminar):")
    while True:
        entrada = input("Número: ")
        if entrada.lower() == 'fin':  #lower(). Convierte las letras de un texto en minúsculas
            break
        try:
            numero = int(entrada)  # Intenta convertir la entrada a un número entero
            if numero in lista:  # Verifica si el número ya está en la lista
                print("El número ya está en la lista. Ingresa otro número.")
            else:
                lista.append(numero)  # Agrega el número a la lista si es único
        except ValueError:
            print("Por favor, ingresa un número válido.")
    return lista

def generar_lista_aleatoria(n):
    return random.sample(range(1,n*10),n)

def ordenar_lista(lista):
    n=len(lista)
    for i in range(n):
        for j in range(0,n-i-1):
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1]=lista[j+1], lista[j]
    return lista 

def busqueda_lineal(lista,numero):
    inicio=time.time()
    for i, valor in enumerate(lista):
        if valor==numero:
            fin=time.time()
            print(f"Tiempo de ejecución de la búsqueda lineal: {fin - inicio:.8f} segundos")
            return i
    fin=time.time()
    print(f"Tiempo de ejecución de la búsqueda lineal: {fin - inicio:.8f} segundos")
    return -1

def busqueda_binaria(lista,numero):
    inicio=time.time()
    izquierda=0
    derecha=len(lista)-1
    while izquierda <= derecha:
        medio=(izquierda+derecha)//2
        if lista[medio]==numero:
            fin=time.time()
            print(f"Tiempo de ejecución de la búsqueda lineal: {fin - inicio:.8f} segundos")
            return medio
        elif lista[medio]<numero:
            izquierda=medio+1
        else:
            derecha=medio-1
    fin=time.time()
    print(f"Tiempo de ejecución de la búsqueda lineal: {fin - inicio:.8f} segundos")
    return -1

def realizar_busqueda_binaria(lista, numero):
    respuesta = input("¿La lista está ordenada? (s/n): ").lower()
    if respuesta == 'n':  
        print("Ordenando la lista antes de realizar la búsqueda binaria.")
        lista = ordenar_lista(lista)
    elif respuesta != 's':  
        print("Respuesta no válida. Asumiendo que la lista no está ordenada.")
        lista = ordenar_lista(lista)
    return busqueda_binaria(lista, numero)

def descomponer_numero(n):
    if n < 1:
        return n 
    else:
        return descomponer_numero(n//10)+[n%10]
    
def elegir_lista():
    print("¿De qué lista deseas trabajar?")
    print("1. Lista ingresada manualmente")
    print("2. Lista generada aleatoriamente")
    while True:
        opcion = input("Selecciona una opción (1 o 2): ")
        if opcion == '1':
            return 'manual'
        elif opcion == '2':
            return 'aleatoria'
        else:
            print("Opción no válida, por favor ingresa 1 o 2.") 



