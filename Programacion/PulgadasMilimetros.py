def pulgadas_y_milimetros(milimetros):
    milimetros = milimetros / 10 
    pulgadas = milimetros / 25.4
    
    return  milimetros, pulgadas 

milimetros = float(input("Ingresa los milimetros que quieres convertir: "))
milimetros, pulgadas = pulgadas_y_milimetros(milimetros)

print("Los milimetros ingresados en Pulgadas son:  ", pulgadas )
print("Los milimetros ingresados en cm son:  ", milimetros )