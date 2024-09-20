import random

# Lista de palabras, deben ser strings
palabras = ["programacion", "juego", "teclado", "python", "computadora"]
palabra_secreta = random.choice(palabras)
longitud_palabra = len(palabra_secreta)
progreso = ["_"] * longitud_palabra
intentos_restantes = 6
letras_intentadas = []

#"join" es para unir las cadenas, por ejemplo, en este caso serían los "_"

def mostrar_progreso():
    print("Palabra: " + " ".join(progreso))
    print(f"Intentos restantes: {intentos_restantes}")
    print(f"Letras intentadas: {', '.join(letras_intentadas)}")

def adivinar_letras(letra):
    global intentos_restantes
    if letra in letras_intentadas:
        print(f"Ya has intentado la letra '{letra}'. Prueba con otra.")
        return
    letras_intentadas.append(letra)
#Aquí, i es el índice de la letra en palabra_secreta, y l es la letra en sí. 
# Esto te permite actualizar la lista progreso en la posición correcta.
    if letra in palabra_secreta:
        print(f"¡Bien! La letra '{letra}' está en la palabra.")
        for i, l in enumerate(palabra_secreta):
            if l == letra:
                progreso[i] = letra
    else:
        print(f"La letra '{letra}' no está en la palabra.")
        intentos_restantes -= 1

while intentos_restantes > 0 and "_" in progreso:
    mostrar_progreso()
#El método lower() en Python se utiliza para convertir todas las letras de una cadena a minúsculas.
    letra = input("Adivina una letra: ").lower()


#len(letra) != 1:
# Esta condición verifica si la longitud de la entrada (letra) es diferente de 1.
#  Esto asegura que el usuario introduzca exactamente una sola letra. 
# Si el usuario ingresa más de una letra o ninguna, esta condición se evalúa como True.
    if len(letra) != 1 or not letra.isalpha():
        print("Introduce solo una letra.")
        continue
#isalpha() es un método que comprueba si todos los caracteres de la cadena son letras del alfabeto 
# (sin incluir números o caracteres especiales). La expresión not letra.isalpha() se evalúa como True 
# si hay algún carácter que no sea una letra. Esto asegura que la entrada del usuario sea solo letras.
    adivinar_letras(letra)

if "_" not in progreso:
    print(f"Has adivinado la palabra: {palabra_secreta}")
else:
    print(f"Te has quedado sin intentos. La palabra era: {palabra_secreta}")
#Si no hay guiones bajos en progreso, significa que el jugador ha adivinado todas las letras de la palabra.