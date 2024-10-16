import random
import time
lista=[]
for i in range (50):
    y=random.randint(1,50)
    lista.append(y)

lista.sort()
print("Lista ordenada:")
print(lista)

nro = int(input("Ingresa el número a buscar: "))   
def busq_bin(lista, nro):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista [medio] == nro:
            return medio
        elif lista [medio] <  nro:
            izquierda = medio + 1
        else: 
            derecha = medio -1
    return -1

inicio=time.time()
indice = busq_bin(lista, nro)
fin=time.time()
print(f"Tiempo transcurrido de la generación de la lista \n {(fin-inicio)/1000} ms")
if indice != -1:
    print(f'El número {nro} se encuentra en el índice {indice}.')
else:
    print(f'El número {nro} no está en la lista.')