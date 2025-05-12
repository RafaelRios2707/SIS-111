#precios=[400,250,310,280]
#menor=precios[0]  #Supone que el 1er elemento es el menor
#for precio in precios:
    #if precio<menor:
        #menor=precio
 #print(menor)


def lista_precios(precios):
    menor=precios[0]
    for precio in precios:
        if precio<menor:
            menor=precio
    return menor
        
precios=[400,250,310,280]
print(lista_precios(precios))





#Busqueda binaria
def busqueda_binaria(lista,objetivo):
    izquierda=0
    derecha=len(lista)-1
    while izquierda<=derecha:
        medio=(izquierda+derecha)//2
        if lista[medio]==objetivo:
            return medio
        elif lista[medio]<objetivo:
            izquierda=medio+1
        else:
            derecha=medio-1
    return -1

lista=[12,23,34,45,67]
objetivo=45

posicion=busqueda_binaria(lista, objetivo)
if posicion !=-1:
    print(f"Elementos encontrado en posicion {posicion}")
else:
    print("404 not found")





#Busqueda lineal
def busqueda_lineal(lista,objetivo):
    for i in range(len(lista)):
        if lista[i]==objetivo:
            return i
    return -1




datos=[23,45,12,67,34]
buscado=67

posicion=busqueda_lineal(datos, buscado)
if posicion !=-1:
    print(f"Elementos encontrado en posicion {posicion}")
else:
    print("404 not found")