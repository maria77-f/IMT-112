def calcularpromedio(notas): #función para calcular el promedio de notas de cada estudiante.
    return sum(notas)/len(notas) #len(notas) para contar cuantos elementos hay en la lista.
notasestudiantes=[]
for  estudiante in range(3):
    print(f"Ingresando notas para el estudiante {estudiante+1}:")
    notas=[]
    for i in range (3):
        nota=float(input(f"Ingrese la nota {i+1}:"))
        notas.append(nota)
    notasestudiantes.append(notas)

for i, notas in enumerate (notasestudiantes): #enumerate sirve para saber la posición de cada elemento de una lista y también el contenido de cada posición.
    promedio=calcularpromedio(notas)
    print(f"El promedio del estudiante {i+1} es: {promedio:.2f}") #.2f para que el promedio se muestre con dos decimales.