import Operaciones
def calculadora():
    print("Seleccione una función:")
    print("1. Longitud (metros a kilómetros)")
    print("2. Masa (gramos a kilogramos)")
    print("3. Temperatura (Celsius a Fahrenheit)")

    opcion = input("Ingrese el número de la operación que desea realizar (1/2/3): ")
#Es para ver si el usuario a ingresado en si un número y no otro caracter como una letra o algún signo.
    if opcion in ['1', '2', '3']:
        try:
            num1 = float(input("Ingrese el número el cual quiere cambiar: "))
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")
            return

        if opcion == '1':
            print(f"El resultado de la longitud en kilómetros es: {Operaciones.longitud(num1)} km")
        elif opcion == '2':
            print(f"El resultado de la masa en kilogramos es: {Operaciones.masa(num1)} kg")
        elif opcion == '3':
            print(f"El resultado de la temperatura en Fahrenheit es: {Operaciones.temperatura(num1)} °F")
    else:
        print("Opción no válida. Seleccione una opción del 1 al 3.")

if __name__ == "__main__":
    calculadora() 