import random
lista=[]
largolista=50
min=5
max=50
def genelist(rango,min,max,lista):
    for i in range (rango):
        x=random.randint(min,max)
        lista.append(x)
    return lista
genelist(largolista,min,max,lista)
print(lista)
print(len(lista))