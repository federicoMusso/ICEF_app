#CUESTIONARIO 

# Bucle for 

# FATIGA ##########################################################################################################################

fatiga = "FATIGA"

# Salto de linea 
print()

for i in fatiga:
    
#Espacio entre letras
    
    print(f"{i}", end= " ")

# Salto de linea 

print()

fatiga = {"Muy recuperado": 5, "Recuperado": 4, "Normal": 3, "Mas fatigado de lo normal": 2, "Muy fatigado": 1}

for clave, valor in fatiga.items():
    
    print(f"{clave} -> {valor}")
    
fatiga = float(input("Ingrese el número corespondiente a su estado de fatiga: "))

# Bucle While

while fatiga <1 or fatiga >= 6:
    
    print("Error -> El número igresado deberia de estar entre 1 y 5.")
    
    fatiga = float(input("Ingrese el número corespondiente a su estado de fatiga:"))  

# Salto de linea 
print()

# CALIDAD DE SUEÑO   ##################################################################################################################

ca = "CALIDAD DE SUEÑO"

for a in ca:
    
    print(f"{a}", end= " ")

# Salto de linea 
print()

ca = {"Muy relajado": 5, "Bueno": 4, "Dificultad para conciliar el sueño ": 3, "Sueño inquieto": 2, "Insomnio": 1}

for clave, valor in ca.items():
    
    print(f"{clave} -> {valor}")
    
ca = float(input("Ingrese el número corespondiente a su calidad de sueño: "))

# Bucle While

while ca <1 or ca >= 6:
    
    print("Error -> El número igresado deberia de estar entre 1 y 5.")
    
    ca = float(input("Ingrese el número corespondiente a su calidad de sueño:"))  

# DAÑO MÚSCULAR GENERAL #############################################################################################################################

da = "DAÑO MÚSCULAR GENERAL"

# Salto de linea 
print()

for b in da:
    
    #Espacio entre letras
    
    print(f"{b}", end= " ")

# Salto de linea 
print()

da = {"Muy buena sensaciones": 5, "Buenas sensaiones": 4, "Normal": 3, "Aumento de dolor múscular": 2,"Muy dolorido": 1}

for clave, valor in da.items():
    
    print(f"{clave} -> {valor}")
    
da = float(input("Ingrese el número corespondiente a su estado de daño múscular general : "))

# Bucle While

while da <1 or da >= 6:
    
    print("Error -> El número igresado deberia de estar entre 1 y 5.")
    
    da = float(input("Ingrese el número corespondiente a su estado de daño múscular general :"))  

# Salto de linea 
print()

# NIVELES #######################################################################################################################################

ni = "NIVELES"

# Salto de linea 
print()

for c in ni:
    
    #Espacio entre letras
    
    print(f"{c}", end= " ")

# Salto de linea 
print()

ni = {"Muy relajado": 5, "Relajado": 4, "Normal": 3, "Estresado": 2,"Muy Estresado": 1}

for clave, valor in ni.items():
    
    print(f"{clave} -> {valor}")
    
ni = float(input("Ingrese el número corespondiente a su estado de niveles  : "))

# Bucle While

while ni <1 or ni >= 6:
    
    print("Error -> El número igresado deberia de estar entre 1 y 5.")
    
    ni = float(input("Ingrese el número corespondiente a su estado de niveles :"))  

# Salto de linea 
print()

# HUMOR ##########################################################################################################################

hu = "HUMOR"

# Salto de linea 
print()

for d in hu:
    
    #Espacio entre letras
    
    print(f"{d}", end= " ")

# Salto de linea 
print()

hu = {"Muy positivo": 5, "Buen humor": 4, "Menos interesado en otras actividades de lo normal ": 3, "Molesto": 2,"Muy molesto": 1}

for clave, valor in hu.items():
    
    print(f"{clave} -> {valor}")
    
hu = float(input("Ingrese el número corespondiente a su estado de daño múscular : "))

# Bucle While

while hu <1 or hu >= 6:
    
    print("Error -> El número igresado deberia de estar entre 1 y 5.")
    
    hu = float(input("Ingrese el número corespondiente a su estado de humor :"))  

# Salto de linea 
print()


total = (fatiga + ca + da + ni + hu)

print("El valor total del cuestionario es: ", total)























