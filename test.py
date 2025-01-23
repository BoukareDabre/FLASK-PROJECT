import json, os, random, json
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
    return render_template('Index.html')


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

DB_utenti = "./DataBase/utenti.json"

class User:
    """
    Classe che rappresenta un utente con attributi personali e di ruolo.
    """
    def __init__(
        self,
        id_user: int,
        name_user: str,
        mail: str,
        password: str,
        phone_number: str,
        data_member: str = "",
        profile_image_url: str = "",
        reservations: list[str] = None,
        role: str = "user"
    ):
        self.id_user = id_user
        self.name_user = name_user
        self.mail = mail
        self.password = password
        self.phone_number = phone_number
        self.data_member = data_member
        self.profile_image_url = profile_image_url
        self.reservations = reservations 
        self.role = role

    def get_id_user(self) -> int:
        """Ritorna l'ID dell'utente."""
        return self.id_user

    def get_name_user(self) -> str:
        """Ritorna il nome dell'utente."""
        return self.name_user

    def get_mail(self) -> str:
        """Ritorna l'indirizzo email dell'utente."""
        return self.mail

    def get_password(self) -> str:
        """Ritorna la password dell'utente."""
        return self.password

    def get_phone_number(self) -> str:
        """Ritorna il numero di telefono dell'utente."""
        return self.phone_number

    def get_role(self) -> str:
        """Ritorna il ruolo dell'utente."""
        return self.role

    def get_reservations(self) -> list[str]:
        """Ritorna le prenotazioni dell'utente."""
        return self.reservations

    def get_profile_image_url(self) -> str:
        """Ritorna l'URL dell'immagine di profilo dell'utente."""
        return self.profile_image_url



@app.route('/account')
def utenti():
    # Retrieve the 'id' parameter from the query string
    id_user = request.args.get('id')

    # Load the user data from the JSON file
    with open(DB_utenti, "r") as file:
        dizionario_user = json.load(file)

    user_list = []

    # Iterate over the user dictionary and create User objects
    for jsonFile in dizionario_user:
        # Skip entries missing 'id_user'
        if 'id_user' not in jsonFile:
            continue

        # Create a User object for each valid entry
        user = User(
            int(jsonFile['id_user']),
            jsonFile['name_user'],
            jsonFile['mail'],
            jsonFile['password'],
            jsonFile['phone_number'],
            jsonFile['data_member'],
            jsonFile['Profileimage_url'],
            jsonFile['reservations'],
            jsonFile['role']
        )
        user_list.append(user)
        

    # Find the user with the specified ID
    user_selezionato = None
    for user in user_list:
        if id_user == str(user.get_id_user()):  # Compare IDs as strings
            user_selezionato = user
            break

    # Handle case where user is not found
    if user_selezionato is None:
        return render_template('account.html', message="Utente non trovato")

    # Pass the selected user to the template
    return render_template('account.html', user_selezionato=user_selezionato)






@app.route('/story_cinema')
def story_cinema():
    return render_template('story_cinema.html')

@app.route('/luogo_cinema')
def luogo_cinema():
    return render_template('luogo_cinema.html')

@app.route('/registration')
def registration():
    tipo = request.args.get('tipo')
    return render_template('registration.html',tipo=tipo)

@app.route('/user', methods=['POST'])
def user():
    tipo = request.args.get('tipo')
    user = None

    if(tipo == "S"):

        with open(DB_utenti, "r") as file:
            users = json.load(file)
            print(f"Utenti caricati: {users}") 

        new_user = {
            "id_user": users[-1]["id_user"] + 1 if users else 1,
            "name_user": request.form.get('name'),
            "mail": request.form.get('email'),
            "password": request.form.get('password'),
            "phone_number": request.form.get('phone'),
            "Profileimage_url": "https://example.com/buba.jpg", 
            "reservations": ["Reservation1", "Reservation2"], 
            "role": "user"            
        }

        print(f"Nuovo utente: {new_user}")

        users.append(new_user)

        with open(DB_utenti, "w") as file:
            json.dump(users, file, indent=4)

        user = new_user
        
    return render_template('account.html', user=user)




if __name__ == '__main__':
    app.run(debug=True)


