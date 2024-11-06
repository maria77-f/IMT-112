import FunEj1 as f

def main():
    lista_manual = []
    lista_aleatoria = []
    lista_ordenada = []
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
            lista_manual = f.ingresar_lista()

        elif opcion == '2':
            n = int(input("¿Cuántos números aleatorios deseas generar? "))
            lista_aleatoria = f.generar_lista_aleatoria(n)

        elif opcion == '3':
            if lista_manual or lista_aleatoria:
                lista_a_ordenar = f.elegir_lista()
                if lista_a_ordenar == 'manual':
                    print("Lista antes de ordenar:", lista_manual)
                    lista_ordenada = f.ordenar_lista(lista_manual)
                    print("Lista ordenada:", lista_ordenada)
                elif lista_a_ordenar == 'aleatoria':
                    print("Lista antes de ordenar:", lista_aleatoria)
                    lista_ordenada = f.ordenar_lista(lista_aleatoria)
                    print("Lista ordenada:", lista_ordenada)
            else:
                print("No hay listas generadas aún.")

        elif opcion == '4':
            if lista_manual or lista_aleatoria:
                lista_a_buscar = f.elegir_lista()
                numero = int(input("Ingresa el número a buscar: "))
                if lista_a_buscar == 'manual':
                    resultado = f.busqueda_lineal(lista_manual, numero)
                elif lista_a_buscar == 'aleatoria':
                    resultado = f.busqueda_lineal(lista_aleatoria, numero)

                if resultado != -1:
                    print(f"El número {numero} fue encontrado en la posición {resultado}.")
                else:
                    print(f"El número {numero} no fue encontrado en la lista.")
            else:
                print("No hay listas generadas aún.")

        elif opcion == '5':
            if lista_ordenada:
                lista_a_buscar = f.elegir_lista()
                numero = int(input("Ingresa el número a buscar: "))
                respuesta = input("Recuerda que la lista debe estar ordenada para la búsqueda binaria. ¿Está ordenada? (s/n): ")
                if respuesta.lower() == 's':
                    if lista_a_buscar == 'manual':
                        lista_ordenada = f.ordenar_lista(lista_manual)
                        resultado = f.busqueda_binaria(lista_ordenada, numero)
                    elif lista_a_buscar == 'aleatoria':
                        lista_ordenada = f.ordenar_lista(lista_aleatoria)
                        resultado = f.busqueda_binaria(lista_ordenada, numero)

                    if resultado != -1:
                        print(f"El número {numero} fue encontrado en la posición {resultado}.")
                    else:
                        print(f"El número {numero} no fue encontrado en la lista.")
                else:
                    print("Recuerda ordenar la lista antes de hacer la búsqueda binaria.")
            else:
                print("No hay listas ordenadas aún.")

        elif opcion == '6':
            if lista_manual or lista_aleatoria:
                lista_a_descomponer = f.elegir_lista()
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

        elif opcion == '7':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, por favor intenta de nuevo.")
main()