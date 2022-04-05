# Percepción Subjetiva del Esfuerzo o siglas en inlges RPE 

# Carga de entrenamiento = RPE de sesión X Duración (Minutos)

print("Para calcular la Carga de entrenamiento ingrese los siguientes datos: ")

print() # Salto de linea 

print("L U N E S")

lun = int(input("Ingrese el RPE asignado a la sesión de entrenamiento: "))

while lun <0 or lun >= 11:
    
    print("Error -> El número igresado deberia de estar entre 0 y 10")
    
    lun = float(input("Ingrese nuevamente el RPE que usted le asigna al entrenamiento: "))
#

tie_lu = int(input("Ingrese el tiempo de la sesión de entrenamiento en minutos: "))

###############################################################################
print() # Salto de linea 

print("M A R T E S")

mar = int(input("Ingrese el RPE asignado a la sesión de entrenamiento: "))

while mar <0 or mar >= 11:
    
    print("Error -> El número igresado deberia de estar entre 0 y 10")
    
    mar = float(input("Ingrese nuevamente el RPE que usted le asigna al entrenamiento: "))

tie_ma = int(input("Ingrese el tiempo de la sesión de entrenamiento en minutos: "))

###############################################################################
print() # Salto de linea 

print("M I E R C O L E S")

mier = int(input("Ingrese el RPE asignado a la sesión de entrenamiento: "))

while mier <0 or mier >= 11:
    
    print("Error -> El número igresado deberia de estar entre 0 y 10")
    
    mier = float(input("Ingrese nuevamente el RPE que usted le asigna al entrenamiento: "))

tie_mie = int(input("Ingrese el tiempo de la sesión de entrenamiento en minutos: "))

###############################################################################
print() # Salto de linea 

print("J U E V E S")

jue = int(input("Ingrese el RPE asignado a la sesión de entrenamiento: "))

while jue <0 or jue >= 11:
    
    print("Error -> El número igresado deberia de estar entre 0 y 10")
    
    jue = float(input("Ingrese nuevamente el RPE que usted le asigna al entrenamiento: "))

tie_jue = int(input("Ingrese el tiempo de la sesión de entrenamiento en minutos: "))

###############################################################################
print() # Salto de linea 

print("V I E R N E S")

vie = int(input("Ingrese el RPE asignado a la sesión de entrenamiento: "))

while vie <0 or vie>= 11:
    
    print("Error -> El número igresado deberia de estar entre 0 y 10")
    
    vie = float(input("Ingrese nuevamente el RPE que usted le asigna al entrenamiento: "))

tie_vie = int(input("Ingrese el tiempo de la sesión de entrenamiento en minutos: "))

###############################################################################
print() # Salto de linea 

print("S A B A D O")

sab = int(input("Ingrese el RPE asignado a la sesión de entrenamiento: "))

while sab <0 or sab >= 11:
    
    print("Error -> El número igresado deberia de estar entre 0 y 10")
    
    sab = float(input("Ingrese nuevamente el RPE que usted le asigna al entrenamiento: "))

tie_sab = int(input("Ingrese el tiempo de la sesión de entrenamiento en minutos: "))

###############################################################################
print() # Salto de linea 

print("D O M I N G O")

dom = int(input("Ingrese el RPE asignado a la sesión de entrenamiento: "))

while dom <0 or dom >= 11:
    
    print("Error -> El número igresado deberia de estar entre 0 y 10")
    
    dom = float(input("Ingrese nuevamente el RPE que usted le asigna al entrenamiento: "))

tie_dom = int(input("Ingrese el tiempo de la sesión de entrenamiento en minutos: "))

###############################################################################

# Resultados de la carga de entrenamientos 

car_lu = lun * tie_lu

print() # Salto de linea 

print("La carga de entrenamiento de los dias correspondientes son: ")

print(car_lu, "Lunes")

car_mar = mar * tie_ma

print( car_mar, "Martes")

car_mie = mier * tie_mie

print(car_mie, "Miercoles")

car_jue = jue * tie_jue

print(car_jue, "Jueves")

car_vier = vie * tie_vie 

print(car_vier, "Viernes")

car_sab = sab * tie_sab

print(car_sab, "Sabado")

car_dom = dom * tie_dom

print(car_dom, "Domingo")

# INDICE DE MONOTONIA #########################################################

print() # Salto de linea 

#print("Para calcular el indice de monotoni­a, ingrese los siguientes datos: ")

media = round ((car_lu + car_mar + car_mie + car_jue + car_vier + car_sab + car_dom) /7)

print() # Salto de linea 

# CARGA MEDIA DE LA SEMANA ####################################################

print("                              D  A  T  O  S")

print(f"La carga media diaria de entrenamiento de la semana es: {media}")

print() # Salto de linea 

# DESVIACIÓN ESTANDARD

import statistics

datos = [car_lu, car_mar, car_mie, car_jue, car_vier, car_sab, car_dom]

desviacion = round (statistics.stdev (datos),2)

print(f"Su desviación estandar es: {desviacion}")

print() # Salto de linea 

# idem = Indice de monotonia 

idem = round (float(media/desviacion),2)

print(f"Su indice de monotonia es: {idem}")

print() # Salto de linea 
    
# FATIGA DEL ENTRENAMIENTO ####################################################

# Fatiga aguda (Carga semanal x indice de monotonia) 

#Esta relacionado con adaptaciones negativas al entrenamiento, y cuanto mayor sea este, mayor riesgo de sobreentrenamiento

total = float(car_lu + car_mar + car_mie + car_jue + car_vier + car_sab + car_dom)

fa = round( (float(total)*idem))

print(f"La fatiga aguda semanal de entrenamiento es: {fa}")

print() # Salto de linea 

# CARGA DE LA SEMANA ##########################################################

print("La carga de la semana es:", total)

print() # Salto de linea 

# Ratio A:C  Carga del ultimo microciclo / Carga promedio de los ultimos 4 microciclos

print("Para calcular el ratio de carga aguda:cronica es necesario ingresar los siguientes datos: ")

print() # Salto de linea 

#carga_sem = carga semanal 

carga_sem = total

# Ingresa el total de la carga de los ultimos 4 microciclo 

print("Ingrese la carga total de los ultimos 4 microciclos ")

n = int(input("Ingrese la cantidad de datos a promediar: "))

# Promedio 

suma = 0

i = 1

while (i <= n):
    
    print(("Ingrese la carga correspondiente: ", i))
    
    numero = float(input())
    
    suma = suma + numero
    
    i += 1
    
promedio = suma / n

print()

print("El promedio de los ultimos 4 microciclo es: ", promedio)

print() # Salto de linea 

# Cálculo Ratio A:C ########################################################### 

ac = round ((carga_sem / promedio),2)

print(f"Su ratio de carga aguda:cronica es: {ac}")

print() # Salto de linea 

# Rangos de carga 

if ac <= 0.7: 
    
    print(("Estos son parametros bajos del Ratio A:C y se considera que tiene efectos de desentrenamientos. "))
    
elif ac >= 0.8 and ac <= 1.3:
 
    print("Estos son parametros normales del Ratio A:C y se considera que tiene bajo riesgo de lesiones. ")
    
elif ac >= 1.4:
    
    print("Estos son parametros altos del Ratio A:C y se concidera que tiene riesgo de lesiones.")
    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    