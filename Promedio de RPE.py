# Calculo para indentificar el promedio del RPE, semanal, mensual, anual, etc. 

print("Para calcular el promedio de su RPE, ingrese los siguientes datos: ")

n = int(input("Ingrese la cantidad de datos a promediar: "))

# PROMEDIO ####################################################################

# Bucle while

sum_a = 0

i = 1

while (i <= n):
    
    print(("Ingrese el número: ", i))
    
    numer_o = float(input())
    
    sum_a = sum_a + numer_o
    
    i += 1
    
promedi_o = round ((sum_a / n),2)

print ("Su RPE promedio es: ", promedi_o)

# Bucle while

rpe = promedi_o

while rpe <0 or rpe >= 11:
    
    print("Error -> El número igresado deberia de estar entre 0 y 10")
    
    rpe = float(input("Ingrese el RPE que usted le asigna al entrenamiento: "))  

if rpe == 0:
    
    print("Usted se encuentra en un entrenamiento de recuperación")
    
elif rpe == 1:
    
    print("Usted se encuentra en un entrenamiento de intensidad sumamente facil ")
    
elif rpe == 2:
    
    print("Usted se encuentra en un entrenamiento de intensidad facil")
    
elif rpe == 3:
    
    print("Usted se encuentra en un entrenamiento de intensidad moderada ")

elif rpe == 4:
    
    print("Usted se encuentra en un entrenamiento de intensidad algo dura")
    
elif rpe == 5 or rpe == 6:
    
    print("Usted se encuentra en un entrenamiento de intensidad dura ")

elif rpe == 7 or rpe == 8 or rpe == 9:
    
    print("Usted se encuentra en un entrenamiento de intensidad muy dura ")
    
elif rpe == 10:
    
    print("Usted se encuentra en un entrenamiento de maxima intensidad")