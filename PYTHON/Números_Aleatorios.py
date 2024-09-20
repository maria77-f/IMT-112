import random 
numero_secreto=random.randint(1,100)
print("al juego de adivinar un número")
print("He elegido un número del 1 al 100. ¿Puedes adivinar cuál es?")
intentos=0

while True:
    
        adivinanza= int (input("Introduce tu adivinanza:"))
        intentos+=1

        if adivinanza < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo")
        elif adivinanza > numero_secreto:
             print("Demasiado alto. Intenta de nuevo")
        else:
            print(f"Adivinaste el número. Y el número de intentos fue {intentos}")
            break
    
