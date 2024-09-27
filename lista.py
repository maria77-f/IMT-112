import random
lista=[]
def genelist(rango,min,max,lista):
    for i in range (rango):
        x=random.randint(min,max)
        lista.append(x)
    return lista
genelist(50,5,50,lista)
print(lista)
print(len(lista))