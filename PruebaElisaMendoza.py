#Autor: Elisa Mendoza

from statistics import mean

weeks_may=[]
#Llena la lista bi-dimensional: 3 semanas con 7 días
for i in range(3):
    weeks_may.append([])
    print(f"Semana {i+1}")
    for j in range(7):
        day=int(input(f"Ingrese ml de lluvia del día {j+1}: "))
        weeks_may[i].append(day)
print(weeks_may)

print("RESULTADOS")

#Función que calcula promedio de ml por semana y el total, sin parámetros, que devuelve valor y que usa variables locales
def averages():
    sum=0
    i=0 #cuenta el número de semana
    for week in weeks_may:
        i+=1
        print(f"Promedio de ml por semana {i}: {mean(week):.1f} ml")
        sum+=mean(week)
    return sum/len(weeks_may)

total_avg= averages()#se guarda función en variable ya que será usada posteriormente
print(f"El promedio total es: {(total_avg):.1f}")

#Función que calcula número de días que hubo 25 ml de lluvia, sin parámetros, sin retorno, usa variable global
cont=0
def heavy_rain():
    global cont
    for week in weeks_may:
        for day in week:
            if day==25:
                cont+=1
    print(f"Número de días con 25 ml de lluvia: {cont} días")

heavy_rain()

#Número de días que superaron el promedio en total
cont=0
for week in weeks_may:
    for day in week:
        if day>total_avg:
            cont+=1
print(f"Número de días que superaron el promedio total ({(total_avg):.1f}ml) de lluvia: {cont} días")




