def recomendar_musica(estado):
    recomendaciones = {
        "1": ["Happy – Pharrell Williams", "Bailando – Enrique Iglesias ft. Gente de Zona", "Uptown Funk – Bruno Mars"],
        "2": ["Someone Like You – Adele", "Too Good At Goodbyes – Sam Smith", "The Scientist – Coldplay"],
        "3": ["Tek it – Cafune", "Eye of the Tiger – Survivor", "Radioactive – Imagine Dragons"], 
        "4": ["Titanium – David Guetta Ft. Sia", "Demons – Imagine Dragons", "Moonlight on the River – Mac DeMarco"],
        "5": ["Enter Sandman - Metallica", "Given Up – Linkin Park", "Change – Deftones"],
        "6": ["Die With A Smile - Bruno Mars, Lady Gaga", "Lover Is A Day - Cuco", "All of Me - John Legend", "I Was Made for Loving You - Kiss"],
        "7": ["Bossa No Sé - Cuco Ft. Jean Carter", "Do I Wanna Know? - Arctic Monkeys", "Those Eyes - New West"]
    }
    
    return recomendaciones.get(estado, ["No tengo recomendaciones para ese estado de ánimo. Prueba otro."])

# Función para mostrar el menú
def mostrar_menu():
    print("\nSelecciona un estado para recibir recomendaciones:")
    print("1. Feliz")
    print("2. Triste")
    print("3. Motivado")
    print("4. Relajado")
    print("5. Enojado")
    print("6. Enamorado")
    print("7. Emocionalmente Afectado")
    print("0. Salir")

# Introducción al usuario
print("Bienvenido al Chat de Recomendación de Canciones")
mostrar_menu()

# Bucle infinito para permitir múltiples consultas
while True:
    estado = input("\nIngresa el número correspondiente a tu estado de ánimo (o escribe '0' para salir): ").strip()
    
    if estado == "0":
        print("Gracias por usar el Chat de Recomendación. ¡Hasta luego!")
        break

    # Obtener y mostrar las recomendaciones
    canciones = recomendar_musica(estado)

    print("\nCanciones recomendadas:")
    for cancion in canciones:
        print(f"- {cancion}")

    # Volver a mostrar el menú
    mostrar_menu()