from animeflv import AnimeFLV

# Crear una instancia de la clase AnimeFLV
animeflv = AnimeFLV()


def buscar_anime(nombre):
    resultados = animeflv.search(nombre)
    return resultados


def mostrar_resultados(resultados):
    for idx, anime in enumerate(resultados):
        print(f"{idx + 1}. {anime.title}")


def seleccionar_anime(resultados, seleccion):
    anime_seleccionado = resultados[seleccion - 1]
    return anime_seleccionado


def mostrar_episodios(info):
    for idx, episodio in enumerate(info.episodes):
        print(f"Episodio {idx + 1}")


if __name__ == "__main__":
    nombre_anime = input("Escribe el nombre del anime: ")
    resultados = buscar_anime(nombre_anime)

    if resultados:
        print("Resultados de la búsqueda:")
        mostrar_resultados(resultados)

        seleccion_anime = int(input("Selecciona un anime por número: "))
        anime_seleccionado = seleccionar_anime(resultados, seleccion_anime)

        print(f"Has seleccionado: {anime_seleccionado.title}")
        info = animeflv.get_anime_info(anime_seleccionado.id)
        info.episodes.reverse()
        print("Episodios disponibles:")
        mostrar_episodios(info)

        index_episodio = int(input("Selecciona un episodio por número: "))

        capitulo = info.episodes[index_episodio - 1].id
        # Coseguir el link del episodio seleccionado
        links = animeflv.get_links(anime_seleccionado.id, capitulo)
        for link in links:
            print(f" {link}")

    else:
        print("No se encontraron resultados.")