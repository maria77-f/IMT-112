def descomponer_numero(n):
    if n < 10:
        return [n]
    else:
        return descomponer_numero(n // 10) + [n % 10]

try:
    n = int(input("Ingresa un número entero: "))
    resultado = descomponer_numero(n)
    print(f"Los dígitos de {n} son: {resultado}")
except ValueError:
    print("Por favor, ingresa un número válido.")


