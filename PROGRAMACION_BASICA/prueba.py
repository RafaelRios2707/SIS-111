
numero=int(input("Introduce un numero con varias cifras: "))
suma_par=0
suma_impar=0
while (numero>0):
    numero%10
    numero=numero//10
    if (numero%2==0):
        suma_par=suma_par+1
    else:
        suma_impar=suma_impar+1

print(suma_par,suma_impar)






