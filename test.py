import json, os, random
from flask import Flask, request, render_template, redirect

template_dir = os.path.abspath('./Templates')
app = Flask(__name__,template_folder=template_dir)

DB = "./DataBase/db.json"

#mi creao la mia classe film
class Film:
    def __init__(
        self,
        id: int,  # id del film, un intero
        title: str,  # titolo del film, una stringa
        director: str,  # regista, una stringa
        genre: str,  # genere del film, una stringa
        year: int,  # anno di uscita, un intero
        actors: list[str],  # elenco degli attori, una lista di stringhe
        release_date: str,  # data di uscita, una stringa (es. 'YYYY-MM-DD')
        duration_minutes: int,  # durata in minuti, un intero
        distribution: str,  # distribuzione, una stringa
        synopsis: str,  # sinossi, una stringa
        trailer_url: str,  # URL del trailer, una stringa
        poster_url: str,  # URL del poster, una stringa
        screenings: list[str]  # screening del film, una lista di stringhe (date o luoghi)
    ):
        self.id = id
        self.title = title
        self.director = director
        self.genre = genre
        self.year = year
        self.actors = actors
        self.release_date = release_date
        self.duration_minutes = duration_minutes
        self.distribution = distribution
        self.synopsis = synopsis
        self.trailer_url = trailer_url
        self.poster_url = poster_url
        self.screenings = screenings



    #aggiungo tutti i metodi get
    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_director(self):
        return self.director

    def get_genre(self):
        return self.genre

    def get_year(self):
        return self.year

    def get_actors(self):
        return self.actors

    def get_release_date(self):
        return self.release_date

    def get_duration_minutes(self):
        return self.duration_minutes

    def get_distribution(self):
        return self.distribution

    def get_synopsis(self):
        return self.synopsis

    def get_trailer_url(self):
        return self.trailer_url

    def get_poster_url(self):
        return self.poster_url

    def get_screenings(self):
        return self.screenings


@app.route('/', methods=['GET'])
def index():
    return render_template('account.html')


@app.route('/film')
def film():
    # Recupera il parametro 'film' dalla query string
    id_film = request.args.get('id')
    with open(DB, "r") as file:
        dizionario_film = json.load(file)

    film_list = []
   
    for jsonFile in dizionario_film:
        film = Film(int(jsonFile['id']), 
                    jsonFile['title'], 
                    jsonFile['director'], 
                    jsonFile['genre'], 
                    jsonFile['year'], 
                    jsonFile['actors'], 
                    jsonFile['release_date'], 
                    jsonFile['duration_minutes'], 
                    jsonFile['distribution'], 
                    jsonFile['synopsis'], 
                    jsonFile['trailer_url'], 
                    jsonFile['poster_url'], 
                    jsonFile['screenings'])

        film_list.append(film)

    film_selezionato = None  # Inizializza la variabile
    for film_ricercato in film_list:  # Itera su film_list
        if id_film == str(film_ricercato.get_id()):  # Confronta gli id come stringhe
            film_selezionato = film_ricercato
            break

    # Gestione caso in cui il film non è trovato
    if film_selezionato is None:
        return render_template('base_film.html', message="Film non trovato")
    
    # Passa il film trovato alla template
    return render_template('base_film.html', film_ricercato=film_selezionato)

class User:
    def __init__(
        self,
        id_user: int,
        name_user: str,
        mail: str,
        password: str,
        phone_number: str,
        role: str       
    ):
        self.id_user = id_user
        self.name_user = name_user
        self.mail = mail
        self.password = password
        self.phone_number = phone_number
        self.role = role

        def get_id_user(self):
            return self.id_user
        
        def get_name_user(self):
            return self.name_user
        
        def get_mail(self):
            return self.mail
        
        def get_password(self):
            return self.password
        
        def get_phone_number(self):
            return self.phone_number
        
        def get_role(self):
            return self.role





@app.route('/story_cinema')
def story_cinema():
    return render_template('story_cinema.html')

@app.route('/luogo_cinema')
def luogo_cinema():
    return render_template('luogo_cinema.html')

if __name__ == '__main__':
    app.run(debug=True)


