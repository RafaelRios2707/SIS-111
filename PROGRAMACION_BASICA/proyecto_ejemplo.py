# Chat de Recomendación de Lugares Turísticos Según el País de Interés

# Función que recomienda lugares turísticos según el país seleccionado
def recomendar_lugares(pais):
    # Diccionario donde las claves son los números de los países
    # y los valores son listas con lugares turísticos de cada país
    lugares = {
        "1": ["Machu Picchu - Perú", "Lago Titicaca - Perú", "Líneas de Nazca - Perú"],
        "2": ["Torre Eiffel - Francia", "Museo del Louvre - Francia", "Castillo de Versalles - Francia"],
        "3": ["Gran Muralla - China", "Ciudad Prohibida - China", "Guillin y sus paisajes - China"],
        "4": ["Cristo Redentor - Brasil", "Cataratas de Iguazú - Brasil", "Pan de Azúcar - Brasil"],
        "5": ["Estatua de la Libertad - EE.UU.", "Gran Cañón - EE.UU.", "Parque Nacional Yellowstone - EE.UU."],
        "6": ["Salar de Uyuni - Bolivia", "Copacabana y el Lago Titicaca - Bolivia", "Misión Jesuita de Chiquitos - Bolivia"],
        "7": ["Cataratas del Iguazú - Argentina", "Perito Moreno - Argentina", "La Boca y Caminito - Argentina"]
    }
    
    # Verificar si la opción ingresada por el usuario está en el diccionario
    if pais in lugares:
        print("\n===========================================")
        print("| Recomendaciones de lugares turísticos")
        print("===========================================")
        print(f"| País seleccionado: {pais}                    ")
        print("-------------------------------------------")
        
        # Inicializar un índice para recorrer la lista de lugares turísticos
        index = 0
        while index < len(lugares[pais]):
            print(f"| {index + 1}. {lugares[pais][index]:<30}")
            index += 1  # Incrementar el índice en cada iteración
        
        print("===========================================\n")
    else:
        # Mensaje de error si el usuario ingresa una opción inválida
        print("\nOpción no válida, por favor selecciona una de las opciones disponibles.")



      

# Introducción al usuario
print("Bienvenido al Chat de Recomendación de Lugares Turísticos")
print("Selecciona un país para conocer lugares turísticos:")
print("1. Perú")
print("2. Francia")
print("3. China")
print("4. Brasil")
print("5. Estados Unidos")
print("6. Bolivia")
print("7. Argentina")

# Bucle infinito para que el usuario pueda consultar varias veces
while True:
    # Pedir al usuario que ingrese el número del país o 0 para salir
    pais = input("Ingresa el número correspondiente al país que deseas visitar (o escribe '0' para terminar): ").strip()
    
    # Si el usuario ingresa 0, se termina el programa
    if pais == "0":
        print("Gracias por usar el Chat de recomendación. ¡Hasta luego!")
        break
    
    # Llamar a la función de recomendación de lugares turísticos
    recomendar_lugares(pais)
    
    # Volver a mostrar las opciones disponibles para que el usuario consulte de nuevo
    print("\nSelecciona un país para conocer lugares turísticos:")
    print("1. Perú")
    print("2. Francia")
    print("3. China")
    print("4. Brasil")
    print("5. Estados Unidos")
    print("6. Bolivia")
    print("7. Argentina")
