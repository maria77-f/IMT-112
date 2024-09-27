import Funciones.repaso as fun
notas=[]
while True:
    fun.menu()
    fun.add_notas(notas)
    fun.del_notas(notas)
    fun.mod_notas(notas)
    fun.mos_notas(notas)
    fun.cal_promedio(notas)
    fun.max_min_notas(notas)
    break

print("========\n",notas)
    