
<<<<<<< HEAD
import os
=======
>>>>>>> 8f8d2aa1243999cfa2fae0c63ef0d73eaf176a96
from flask import Flask,request, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import requests
import json

<<<<<<< HEAD
app = Flask(__name__)

from werkzeug.utils import redirect
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'hellosecret')
from setting import API_SECRET_KEY 


=======
from werkzeug.utils import redirect

from setting import API_SECRET_KEY 

app = Flask(__name__)
>>>>>>> 8f8d2aa1243999cfa2fae0c63ef0d73eaf176a96

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/movie' , methods=['POST'])
def movie():
    
    name=request.form.get("name")
    movie_request =requests.get("http://www.omdbapi.com/?tapikey=API_SECRET_KEY",
               params={'apikey': API_SECRET_KEY , 't':{name}  })
    print( movie_request.content) 
    # import pdb; pdb.set_trace()          
    movie=json.loads( movie_request.content) 
    return render_template ('movie.html',  movie=movie)