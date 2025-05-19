
numero=int(input("Introduce un numero con varias cifras: "))
suma_par=0
suma_impar=0
while (numero>0):
    numero%10
    if numero==0:
        suma_par=suma_par
        suma_impar=suma_impar     
    elif (numero%2==0):
        suma_par=suma_par+1
    else:
        suma_impar=suma_impar+1
    numero=numero//10

print(suma_par,"son pares y",suma_impar, "son impares (el 0 cuenta como par)")





