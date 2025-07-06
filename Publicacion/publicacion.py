def crear_publicacion(titulo, contenido, autor):
    """
    Crea una nueva publicación y la guarda en el archivo JSON.
    """
    import json
    from datetime import datetime

    ruta = "Publicacion/publicacion.json"

    # Leer publicaciones existentes
    try:
        with open(ruta, "r") as file:
            publicaciones = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        publicaciones = []

    # Crear nueva publicación
    nueva_publicacion = {
        "titulo": titulo,
        "contenido": contenido,
        "autor": autor,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Agregar la nueva publicación a la lista
    publicaciones.append(nueva_publicacion)

    # Guardar la lista actualizada en el archivo JSON
    try:
        with open(ruta, "w") as file:
            json.dump(publicaciones, file, indent=4)
        print("Publicación creada exitosamente.")
    except Exception as e:
        print(f"Error al guardar la publicación: {e}")