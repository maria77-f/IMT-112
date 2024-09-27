def menu():
    print("""SISTEMA DE GESTIÓN DE NOTAS
          1. Agregar nota
          2. Eliminar nota
          3. Modificar nota
          4. Modificar todas las notas
          5. Obtener nota máxima y mínima
          6. Salir. Elige una opción:""")

def add_notas(notas):
    a=int(input("Ingrese nota: "))
    notas.append(a)
    return notas 

def del_notas(notas):
    ind=len(notas)
    a=int(input("Ingrese un índice para borrar alguna nota: "))
    notas.pop(a)
    return notas

def mod_notas(notas):
    a=int(input("Ingrese índice a modificar: "))
    b=float(input(f"Ingrese el número a modificar: {a}"))
    notas[a]=b
    return

def mos_notas(notas):
    print("Notas actuales: ")
    for i, nota in enumerate(notas):
        print(f"Indice {i}: {nota}")

def cal_promedio(notas):
    promedio=sum(notas)/len(notas)
    print(f"El promedio de las notas es: {promedio:.2f}")

def max_min_notas(notas):
    maximo=max(notas)
    minimo=min(notas)
    return maximo,minimo
