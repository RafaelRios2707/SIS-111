def recomendar_musica(estado):
    recomendaciones = {
        "feliz": ["Happy – Pharrell Williams", "Bailando – Enrique Iglesias ft. Gente de Zona", "Uptown Funk – Bruno Mars"],
        "triste": ["Someone Like You – Adele", "Too Good At Goodbyes – Sam Smith", "The Scienctist – Coldplay"],
        "motivado": ["Tek it – Cafune", "Eye of the Tiger – Survivor", "Radioactive – Imagine Dragons"],
        "relajado": ["Titanium – David Guetta Ft. Sia", "Demons – Imagine Dragons", " Moonlight on the River – Mac de Marco"],
        "enojado": ["Enter Sandman - Metallica", "Given Up – Linkin Park", "Change – Deftones"],
        "enamorado": ["Die With A Smile - Bruno Mars,Lady Gaga", "Lover Is A Day - Cuco", "All of me - John Legend", "I Was Made For Loving You Baby - Kiss"],
        "emocianalmente afectado": ["Bossa No se - Cuco Ft. Jean Carter", "Do I Wanna Know? - Artic Monkeys", "Those Eyes - New West"]
    }
    
    return recomendaciones.get(estado.lower(), ["No tengo recomendaciones para ese estado de ánimo. Prueba otro."])

# Interfaz de usuario
while True:
    estado = input("¿Cómo te sientes? (feliz, triste, motivado, relajado, enojado, enamorado, emocionalmente afectado) o escribe 'salir' para terminar: ").strip().lower()
    if estado == "salir":
        print("¡Hasta luego! Disfruta tu música.")
        break
    print("Te recomiendo escuchar:")
    for cancion in recomendar_musica(estado):
        print(f"- {cancion}")