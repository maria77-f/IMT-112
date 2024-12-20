import fun2 as f
def main():
    lista = []  # Lista que se utilizará en las diferentes opciones del menú

    while True:
        print("Menú Principal")
        print("1. Ingresar lista manualmente")
        print("2. Generar lista aleatoria")
        print("3. Ordenar lista")
        print("4. Búsqueda lineal")
        print("5. Búsqueda binaria")
        print("6. Descomponer número en dígitos")
        print("7. Salir")

        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            # Generar una lista única de números ingresados por teclado
            lista = f.ingresar_lista()
            print("Lista ingresada:", lista)

        elif opcion == '2':
            # Generar una lista de n números aleatorios únicos
            try:
                n = int(input("Ingresa el tamaño de la lista: "))
                lista = f.generar_lista_aleatoria(n)
                print("Lista aleatoria generada:", lista)
            except ValueError:
                print("Por favor, ingresa un número válido.")

        elif opcion == '3':
            # Ordenar la lista actual
            if lista:
                lista = f.ordenar_lista(lista)
                print("Lista ordenada:", lista)
            else:
                print("La lista está vacía. Primero debes ingresar o generar una lista.")

        elif opcion == '4':
            # Búsqueda Lineal
            if lista:
                try:
                    numero = int(input("Ingresa el número a buscar: "))
                    resultado = f.busqueda_lineal(lista, numero)
                    if resultado != -1: #-1 para indicar una búsqueda fallida
                        print(f"El número {numero} se encontró en la posición {resultado} usando búsqueda lineal.")
                    else:
                        print(f"El número {numero} no se encontró en la lista.")
                except ValueError:
                    print("Por favor, ingresa un número válido.")
            else:
                print("La lista está vacía. Primero debes ingresar o generar una lista.")

        elif opcion == '5':
            # Búsqueda Binaria
            if lista:
                try:
                    numero = int(input("Ingresa el número a buscar: "))
                    resultado = f.realizar_busqueda_binaria(lista, numero)
                    if resultado != -1:
                        print(f"El número {numero} se encontró en la posición {resultado} usando búsqueda binaria.")
                    else:
                        print(f"El número {numero} no se encontró en la lista.")
                except ValueError:
                    print("Por favor, ingresa un número válido.")
            else:
                print("La lista está vacía. Primero debes ingresar o generar una lista.")

        elif opcion == '6':
            if lista_manual or lista_aleatoria:
                lista_a_descomponer = elegir_lista()
                if lista_a_descomponer == 'manual':
                    numero = int(input("Elige un número de la lista manual para descomponer: "))
                    if numero in lista_manual:
                        print(f"Los dígitos de {numero} son:", f.descomponer_numero(numero))
                    else:
                        print(f"El número {numero} no está en la lista.")
                elif lista_a_descomponer == 'aleatoria':
                    numero = int(input("Elige un número de la lista aleatoria para descomponer: "))
                    if numero in lista_aleatoria:
                        print(f"Los dígitos de {numero} son:", f.descomponer_numero(numero))
                    else:
                        print(f"El número {numero} no está en la lista.")
            else:
                print("No hay listas generadas aún.")

        else:
            # Mensaje de error para opciones no válidas
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")
main()

