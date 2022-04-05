# Percepción Subjetiva del Esfuerzo o siglas en inlges RPE 

# Carga de entrenamiento = RPE de sesión X Duración (Minutos)

print("Para calcular la Carga de entrenamiento ingrese los siguientes datos: ")

###############################################################################

print("L U N E S")

lun = int(input("Ingrese el RPE asignado a la sesión de entrenamiento: "))

while lun <0 or lun >= 11:
    
    print("Error -> El número igresado deberia de estar entre 0 y 10")
    
    lun = float(input("Ingrese nuevamente el RPE que usted le asigna al entrenamiento: "))
#

tie_lu = int(input("Ingrese el tiempo de la sesión de entrenamiento en minutos: "))

###############################################################################

print("M A R T E S")

mar = int(input("Ingrese el RPE asignado a la sesión de entrenamiento: "))

while mar <0 or mar >= 11:
    
    print("Error -> El número igresado deberia de estar entre 0 y 10")
    
    mar = float(input("Ingrese nuevamente el RPE que usted le asigna al entrenamiento: "))

tie_ma = int(input("Ingrese el tiempo de la sesión de entrenamiento en minutos: "))

###############################################################################

print("M I E R C O L E S")

mier = int(input("Ingrese el RPE asignado a la sesión de entrenamiento: "))

while mier <0 or mier >= 11:
    
    print("Error -> El número igresado deberia de estar entre 0 y 10")
    
    mier = float(input("Ingrese nuevamente el RPE que usted le asigna al entrenamiento: "))

tie_mie = int(input("Ingrese el tiempo de la sesión de entrenamiento en minutos: "))

###############################################################################

print("J U E V E S")

jue = int(input("Ingrese el RPE asignado a la sesión de entrenamiento: "))

while jue <0 or jue >= 11:
    
    print("Error -> El número igresado deberia de estar entre 0 y 10")
    
    jue = float(input("Ingrese nuevamente el RPE que usted le asigna al entrenamiento: "))

tie_jue = int(input("Ingrese el tiempo de la sesión de entrenamiento en minutos: "))

###############################################################################

print("V I E R N E S")

vie = int(input("Ingrese el RPE asignado a la sesión de entrenamiento: "))

while vie <0 or vie>= 11:
    
    print("Error -> El número igresado deberia de estar entre 0 y 10")
    
    vie = float(input("Ingrese nuevamente el RPE que usted le asigna al entrenamiento: "))

tie_vie = int(input("Ingrese el tiempo de la sesión de entrenamiento en minutos: "))

###############################################################################

print("S A B A D O")

sab = int(input("Ingrese el RPE asignado a la sesión de entrenamiento: "))

while sab <0 or sab >= 11:
    
    print("Error -> El número igresado deberia de estar entre 0 y 10")
    
    sab = float(input("Ingrese nuevamente el RPE que usted le asigna al entrenamiento: "))

tie_sab = int(input("Ingrese el tiempo de la sesión de entrenamiento en minutos: "))

###############################################################################

print("D O M I N G O")

dom = int(input("Ingrese el RPE asignado a la sesión de entrenamiento: "))

while dom <0 or dom >= 11:
    
    print("Error -> El número igresado deberia de estar entre 0 y 10")
    
    dom = float(input("Ingrese nuevamente el RPE que usted le asigna al entrenamiento: "))

tie_dom = int(input("Ingrese el tiempo de la sesión de entrenamiento en minutos: "))

###############################################################################

# Resultados de la carga de entrenamientos 

car_lu = lun * tie_lu

print()

print("Su UC del entrenamiento es: ")

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

















