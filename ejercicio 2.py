import requests


def bestInGenre(genre):
    url = "https://jsonmock.hackerrank.com/api/tvseries"
    page = 1
    highest_rated_show = None
    highest_rating = -1

    while True:
        # hago la petición a la API
        response = requests.get(f"{url}?page={page}")
        data = response.json()

        # recorro todas las series en la página actual
        for show in data['data']:
            if genre.lower() in show['genre'].lower():
                # si la serie tiene una mejor calificación, actualizo la mejor serie
                if show['imdb_rating'] > highest_rating:
                    highest_rated_show = show['name']
                    highest_rating = show['imdb_rating']
                # si hay un empate en la calificación, elijo la serie con el nombre alfabéticamente menor
                elif show['imdb_rating'] == highest_rating:
                    if show['name'] < highest_rated_show:
                        highest_rated_show = show['name']

        # si ya no hay más páginas, termino el bucle
        if page >= data['total_pages']:
            break

        # paso a la siguiente página
        page += 1

    return highest_rated_show


# ejemplo:
genre = "Drama"
rta = bestInGenre(genre)

if (rta == None):
    print('No hay resultados para esta busqueda, intenta cambiar el genero.')
else:
    print(rta)
