import math 

"""
     Resuelve ecuaciones cuadratica  de la forma:
         a*x^2 + b*x + c = 0
    usando la formula General:
         x = (-b ± sprt(b^2 - 4*a*c)) / (2*a)     
"""
def resolver_ecuacion_cuadratica():
    
    #1. Ingresar coeficiente a, b, c
    print("programar para resolver la ecuacion a*x^2 + b*x + c = 0")
    print("utilizando la formula general")
    
    a = float(input("ingresa el valor de a:"))
    b = float(input("ingresa el valor de b:"))
    c = float(input("ingresa el valor de c:"))
    
    # V erificar si a == 0, pues no es una ecuacion de segundo grado 
    if a == 0:
        print("\nERROR: a = 0, la ecuacion no es de segundo grado")
        return
    
    #2. Calcular el discriminante (b^2 - 4ac)
    discriminante = b**2 - 4*a*c
    
    #3. Verificar la naturaleza de las raices segun el discriminate
    if discriminante > 0:
        # Dos soluciones reales y distintas 
        x1 = (-b + math.sqrt(discriminante)) / (2 * a) 
        x2 = (-b + math.sqrt(discriminante)) / (2 * a)
        print(f"\nLa ecuacion tiene dos soluciones reales distintas:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
        
    elif discriminante == 0:
        # Una solucion real (raiz doble)
        x_unica = -b / (2 * a)
        print("\nLa ecuacion tiene una solucion (raiz doble):")
        print(f"x = {x_unica}")
        
    else: 
        # Soluciones complejas (discriminantes < 0)
        # Usamos la parte real e imaginaria:
        # x = (-b / 2a) ± (sqrt ( !discriminantes!) / 2a)*i
        parte_real = -b / (2 * a )
        parte_imaginaria = math.sqrt(abs(discriminante)) /(2 * a)
        print("\nLa ecuacion tiene dos soluciones complejas conjugadas:")
        print(f"x1 = {parte_real} + {parte_imaginaria}i")
        print(f"x2 = {parte_real} - {parte_imaginaria}i")
        
#Ejecutar la funcion (descomentar para probar en tu entorno):
resolver_ecuacion_cuadratica()