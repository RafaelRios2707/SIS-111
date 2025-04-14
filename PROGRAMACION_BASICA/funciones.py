def sumar_dos_numeros(numA,numB):
    # Sumar numA + numB
    resultadoSuma = numA + numB
    return resultadoSuma

resultadoFuncion=sumar_dos_numeros(5,20)
print(resultadoFuncion) #el return es opcional

#Mostrar el mes actual
def mes_actual():
    print("Enero")

    #Funciones con valores por defecto
def saludar(nombre = "estimado"):
     print(f"Hola, {nombre}")

def calcular_edad(anio_nacimiento=2001):
    if anio_nacimiento > 1875:
        edad=2025 - anio_nacimiento
    else:
        print("No se permiten años menores a 1875")
        edad=anio_nacimiento  

    return edad 

#Llamar a las funciones

#resultadoFuncion = sumar_dos_numeros(5,20)
#print(resultadoFuncion)

#mes_actual()

#saludar("Juan")


my_edad=calcular_edad()
print(my_edad)

def saludar(nombre="amigo"):
"""Esta funcion saluda al usuartio
Si no se proporciona nombre, usa "amigo"por defecto."""

print(f"!Hola, (nombre)¡")
