#2. Mayor
a=input("a=")
b=input("b=")
if a==b:
    print("los dos son iguales")
else:
    if a>b:
        print(a,"es el mayor")
    else:
        print(b,"es el mayor")


#4.PESO
peso=float(input("peso="))
if peso < 5:
    print("el producto es ligero")
elif (5 < peso and peso<20):
    print("el producto es de peso medio")
elif (peso > 20):
    print("el producto es pesado")


#6.MULTIPLO
a=float(input("a="))
b=float(input("b="))

if a%3==0 and b%3==0 and a%5==0 and b%5==0:
    print("ambos son divisibles entre 3 y 5")
elif a%3==0 and a%3==0 and b%5!=0 and b%5!=0:
    print("ambos son divisibles entre 3")
elif a%3!=0 and a%3!=0 and b%5==0 and b%5==0:
    print("ambos son  divisibles entre 5")
else:
    print("ninguno es divisible entre 3 o 5")

#8. triangulo
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))

if a==b and a==c and b==c:
    print("es equilatero")
elif a==b or a==c or b==c:
    print("es isoceles")
else:
    print("es escaleno")

#10.PESO impuesto
peso=float(input("peso="))
if peso < 5:
    precio=6
    print("el producto es ligero")
elif (5 < peso and peso<20):
    print("el producto es de peso medio")
elif (peso > 20):
    print("el producto es pesado")