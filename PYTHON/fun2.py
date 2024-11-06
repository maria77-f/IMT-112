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

def generar_lista_aleatoria(n): #Genera lista de números únicos aleatorios.
    return random.sample(range(1, n * 10), n) #toma dos argumentos: una secuencia (en este caso, el rango de números generado) y un número n, que indica cuántos elementos aleatorios se deben extraer de esa secuencia. 
#La función garantiza que no haya elementos repetidos en la muestra.
#Este fragmento genera una secuencia de números que comienza en 1 y 
# termina en n * 10 - 1. Así, si n = 5, el rango sería de 1 a 49.
def ordenar_lista(lista):
    n = len(lista)  # Longitud de la lista
    for i in range(n): # Este bucle externo se ejecuta n veces, donde n es la longitud de la lista. En cada iteración, 
    #coloca el elemento más grande aún no ordenado al final de la lista.
        for j in range(0, n - i - 1): #Este es el bucle interno. Su función es recorrer la lista desde el inicio 
        #hasta el último elemento aún no ordenado. # En cada iteración del bucle externo i, el número de comparaciones 
        # necesarias se reduce en 1, ya que los últimos elementos de la lista ya están en orden.
            if lista[j] > lista[j + 1]:  # Intercambia si el elemento es mayor que el siguiente
                lista[j], lista[j + 1] = lista[j + 1], lista[j] #Ordena de manera ascendente.
    return lista

def busqueda_lineal(lista, numero):
    inicio = time.time()  # Captura el tiempo inicial
    for i, elemento in enumerate(lista):  # Recorre la lista buscando el número
        if elemento == numero:
            fin = time.time()  # Captura el tiempo final
            print(f"Tiempo de ejecución de la búsqueda lineal: {fin - inicio:.8f} segundos")
            return i  # Retorna la posición si encuentra el número
    fin = time.time()
    print(f"Tiempo de ejecución de la búsqueda lineal: {fin - inicio:.8f} segundos")
    return -1  # Retorna -1 si no se encuentra el número

def busqueda_binaria(lista, numero):
    inicio = time.time()
    inicio_idx = 0
    fin_idx = len(lista) - 1
    while inicio_idx <= fin_idx:
        medio = (inicio_idx + fin_idx) // 2  # Calcula el punto medio
        if lista[medio] == numero:
            fin = time.time()
            print(f"Tiempo de ejecución de la búsqueda binaria: {fin - inicio:.8f} segundos")
            return medio
        elif lista[medio] < numero:
            inicio_idx = medio + 1
        else:
            fin_idx = medio - 1
    fin = time.time()
    print(f"Tiempo de ejecución de la búsqueda binaria: {fin - inicio:.8f} segundos")
    return -1

def realizar_busqueda_binaria(lista, numero):
    respuesta = input("¿La lista está ordenada? (s/n): ").lower()
    if respuesta == 'n':  # Ordena la lista si el usuario indica que no está ordenada
        print("Ordenando la lista antes de realizar la búsqueda binaria.")
        lista = ordenar_lista(lista)
    elif respuesta != 's':  # Ordena la lista si la respuesta es inválida
        print("Respuesta no válida. Asumiendo que la lista no está ordenada.")
        lista = ordenar_lista(lista)
    return busqueda_binaria(lista, numero)