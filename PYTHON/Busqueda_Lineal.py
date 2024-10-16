import U2funcions as tarea 
import time
listaNum=[]
listaComp=int(input("Ingrese la catidad de datos para la lista: "))
minAl=int(input("Ingrese la cantidad mínima para generar los números aleatorios: "))
maxAl=int(input("Ingrese la cantidad mínima para generar los números aleatorios: "))

inicio=time.time()
tarea.generarLista(listaComp, listaNum, minAl, maxAl)
for i in range (100000):
    print("a")
fin=time.time()
print(f"Tiempo transcurrido de la generación de la lista \n {(fin-inicio)/1000} ms")


print(listaNum)
print(len(listaNum))
print(type(listaNum))

numeroaEncontrar=int(input("Ingrese el número a encontrar: "))
tarea.encontrarnumero(listaNum,numeroaEncontrar)

x=sorted(listaNum)
print(x)
# busqueda binaria