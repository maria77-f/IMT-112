#método de búsqueda binaria
lista=[8,2,3,45,7,93,10,37,90,11]

for i in range(len(lista)):
    #print(f"INDICE={i} nVALOR={lista[i]}")
    for j in range(0,(len(lista)-i-1)):
        print(f"({lista[j]}, {lista[j+1]})")
        if(lista[j]>lista[j+1]):
            lista[j],lista[j+1]=lista[j+1], lista[j]
        print(f"\n ===========\nCAMBIO( {lista[j]}, {lista[j+1]})\n=========")
        


