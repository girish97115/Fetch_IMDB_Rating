import requests
import json

while True:
    print('--------------WELCOME-----------------------')
    api_key = "852159f0"
    base_url = 'http://www.omdbapi.com/?apikey=' + api_key

    print('Enter the Title of the movie: ')
    title = input("> ")
    final_url = base_url + '&t=' + title + '&plot=full'
    request = requests.get(final_url)
    data = request.json()
    print()

    try:
        print('Title: ',data['Title'])
        print()
        print('Release Date: ',data['Released'])
        print()
        print('Storyline: ',data['Plot'])
        print()
        print('Runtime: ',data['Runtime'])
        print()
        print('Genre: ',data['Genre'])
        print()
        print('Director: ',data['Director'])
        print()
        print('Actors: ',data['Actors'])
        print()
        print('Awards Won: ',data['Awards'])
        print()
        print('--------------IMDB RATING-----------------------')
        print()
        print('Imdb Rating: ',data['imdbRating'])
        print()
        print('------------------------------------------------')

        
    except:
        print('Movie Not Found')

    print('Want more movie info: (Yes/No)')

    option = input().lower()
    if option == 'no' or option[0] == 'n':
        print('Thank you for using ')
        break
    print()