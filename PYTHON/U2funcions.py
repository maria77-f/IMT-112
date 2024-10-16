import random
def genlista(t,vmin,vmax,lista):
    for i in range(t):
        ale=random.randint(vmin,vmax)
        if ale not in lista:
            lista.append(ale)
    return lista

def encontrarnumero(lista,num):
    for i in range (len(lista)):
        if (num==lista[i]):
            print(f"Número encontrado en el índice{i}")
            return 1
        else:
            return -1
