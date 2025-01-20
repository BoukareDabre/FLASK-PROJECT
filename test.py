import json, os, random
from flask import Flask, request, render_template, redirect

template_dir = os.path.abspath('./templates')
app = Flask(__name__,template_folder=template_dir)



@app.route('/', methods=['GET'])
def index():
    return render_template('story_cinema.html')

if __name__ == '__main__':
    app.run(debug=True)
