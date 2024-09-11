def longitud(metros):
    return metros / 1000

def masa(gramos):
    return gramos / 1000

def temperatura(celsius):
    return (9/5) * celsius + 32

def calculadora():
    print("Seleccione una función:")
    print("1. Longitud (metros a kilómetros)")
    print("2. Masa (gramos a kilogramos)")
    print("3. Temperatura (Celsius a Fahrenheit)")

    opcion = input("Ingrese el número de la operación que desea realizar (1/2/3): ")

    if opcion in ['1', '2', '3']:
        try:
            num1 = float(input("Ingrese el número el cual quiere cambiar: "))
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")
            return

        if opcion == '1':
            print(f"El resultado de la longitud en kilómetros es: {longitud(num1)} km")
        elif opcion == '2':
            print(f"El resultado de la masa en kilogramos es: {masa(num1)} kg")
        elif opcion == '3':
            print(f"El resultado de la temperatura en Fahrenheit es: {temperatura(num1)} °F")
    else:
        print("Opción no válida. Seleccione una opción del 1 al 3.")
 
if __name__ == "__main__":
    calculadora()