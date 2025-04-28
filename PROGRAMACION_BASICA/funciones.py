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

def nombre_funcion1():
    print("salida de funcion 1")

def nombre_funcion2():
    print("salida de funcion 2")

#salida
nombre_funcion1()

def funcion_retorno():
    return 123

var_salida=funcion_retorno()
print(var_salida)

def obtener_edad():
    edad=int(input("indique su edad:"))
    if (edad>0):
        return edad
    else:
        return 0

def habilitado_brevet(hedad):
    if (hedad>=18):
        return "verdadero"
    else:
        return "falso"
    
var_edad=obtener_edad()
var_habilitado=habilitado_brevet(var_edad)
print(var_habilitado)

def calcular_descuento():
    precio_original=100
    descuento=20
    precio_descuento=(precio_original*descuento)/100
    precio_final=precio_original-precio_descuento
    return precio_final
    
def calcular_descuento2(precio_original,descuento):
    precio_original=int(input("precio original:"))
    descuento=int(input("porcentaje de descuento:"))
    precio_final=precio_original-descuento
    return precio_final
    
def calcular_descuento3(precio_original,descuento):
    return precio_original*(1-descuento/100)

var_precio_f=calcular_descuento()
print(var_precio_f)



def comparar_numeros(A,B):
    if A==B:
        return "iguales"
    if (A>B):
        return A
    else:
        return B

def comparar_numeros2(A,B):
    if A==B:return "iguales"
    
    return A if(A>B)else B 

    
var_A=int(input("Ingrese A: "))
var_B=int(input("Ingrese B: ")) 
var_num_mayor=comparar_numeros2(var_A,var_B)
print(var_num_mayor)  


def recorrer(A):
    while(A>0):
        dig=A%10
        print(dig)
        A=A//10

def par_impar(A):  
    while (A>0):
        dig=A%10
        print(dig)

        var_tem="par" if(dig%2==0)else "impar"
        print(var_tem)
        A=A//10

def suma_valores(A):
    suma=0
    while(A>0):
        dig=A%10
        suma=suma+dig
        A=A//10
    return suma

var_suma=suma_valores(1534)
print(var_suma)

    

    
    

