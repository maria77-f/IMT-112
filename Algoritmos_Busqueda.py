#Búsqueda lineal
import random 
lista=[]
for i in range (100):
    n=random.randint(0,100)
    lista.append(n)
valor=int(input("Ingrese el valor que quiere encontrar: "))
def busqueda_lineal(lista,valor):
    for i in range (len(lista)):
        if lista[i]==valor:
            return i
    return -1
print(len(lista))
