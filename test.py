import json, os, random
from flask import Flask, request, render_template, redirect,send_from_directory

template_dir = os.path.abspath('./Templates')
app = Flask(__name__,template_folder=template_dir)



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
