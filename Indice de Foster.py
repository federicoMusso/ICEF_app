# Indice de Foster RPE X VOLUMEN DE LA SESION 

# pse = Persepción subjetiva del esfuerzo 

pse = int(input("Ingrese el RPE de la sesión de entrenamiento: "))

# Bucle while

while pse <0 or pse >= 11:
    
    print("Error -> El número igresado deberia de estar entre 0 y 10")
    
    pse = float(input("Ingrese el RPE de la sesión de entrenamiento:"))  
    
    print() # Salto de linea 

time = float(input("Ingrese el tiempo de la sesión de entrenamiento: "))
    
print() # Salto de linea

# uni = Unidad de Carga 

uni = (time * pse)

print("Su unidad de carga es: ", uni, "UC")

print() # Salto de linea 

# Intensidad por sesión de entrenamiento 

# intensidad Baja  1 - 300 UC unidades de carga 

# Intensidad Moderada 300 - 600 UC unidades de carga 

# Intensidad alta 600 - 900 UC unidades de carga 

if uni >= 1 and uni <= 300:
    
    print("La sesión de entrenamiento se considera de intensidad baja. ")
    
    print() # Salto de linea 

elif uni >= 301 and uni <= 600: 
    
    print("La sesión de entrenamiento se considera de intensidad moderada. ")
    
    print() # Salto de linea 
    
elif uni >= 601 and uni <= 900:
    
    print("La sesión de entrenamiento se considera de intensidad alta. ")
    
    print() # Salto de linea 
    
# Suma total para saber parametros de lesión 

print("Para calcular la Carga de entrenamiento semanal y saber si se encuentra con mayor probalilidad de lesión: ")

print() # Salto de linea 

print("Ingrese los siguientes datos: ")

print() # Salto de linea 

n = int(input("Cuantas unidades de carga son: "))

# Bucle while:

sum_a = 0

i = 1

while (i <= n):
    
    print(("Ingrese las UC obtenidos de cada sesión de entrenamiento de la semana: ", i))
    
    numer_o = float(input())
    
    sum_a = sum_a + numer_o
    
    i += 1

print("La unidad de carga semanal es: ", sum_a, "UC")



###############################################################################
# Altos indice de UC generan probabilidad de lesión y depende si esta en un periodo precompetitio o competitivo

# En un periodo PRE COMPETITIVO los indices estan entre 3000 a 5000 UC y aumenta la probabalidad entre 50 a 80 %

# En un periodo COMPETITIVO los indices estan entre 1700 a 3000 UC y aumenta la probabalidad entre 50 a 80 %

