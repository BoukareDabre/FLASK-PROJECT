import json, os, random
from flask import Flask, request, render_template, redirect

template_dir = os.path.abspath('./Templates')
app = Flask(__name__,template_folder=template_dir)

@app.route('/', methods=['GET'])
def index():
    return render_template('Index.html')

@app.route('/base_film')
def base_film():
    return render_template('base_film.html')

@app.route('/story_cinema')
def story_cinema():
    return render_template('story_cinema.html')

@app.route('/luogo_cinema')
def luogo_cinema():
    return render_template('luogo_cinema.html')

if __name__ == '__main__':
    app.run(debug=True)


#mi creao la mia classe film
class Film:
    def __init__(
        self,
        id,
        title,
        director,
        genre,
        year,
        actors,
        release_date,
        duration_minutes,
        distribution,
        synopsis,
        trailer_url,
        poster_url,
        screenings
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
