# CAMBIO EN LA CARGA DE ENTRENAMIENTO ENTRE SEMANAS CONSECUTIVAS 

# Se asocio que el 40% de las lesiones se debe al cambio brusco de la carga de entrenamiento 

# Un aumento de la carga de un 15% puede generar un aumento de lesiones entre 21 % a 49 %

car_ante = int(input("Ingrese la carga de entrenamiento de la semana anterior: "))

# Calculo 

regla = car_ante / 10 

# Carga ideal 

car_ide = car_ante + regla 

print() # Salto de linea

print("Su carga de entrenamiento debería de no sobrepasar el siguiente parametro:", car_ide)

print() # Salto de linea

print("Un aumento de este parámetro aumentará la pobabilidad de lesiones entre un 21 a 49 %")





