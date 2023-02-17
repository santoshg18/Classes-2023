# Frameworks of Python - Flask, Django(D is silent), FastAPI
# Web Framework

# MVT - MVC Architecture

"""
Models - Tables
View - Main logic / Controller - Controls the flow btwn model and template. - SQL<>
Template - Showcase to outer world - html, css, bootstrap, javascript

urls - <>/home

# Virtual environments
# Seperate space to handle packages
C:/
D:/ Facebook - flask, requests, json
E:/ Microsoft - mysql.connector, django

"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def first_method():
    return 'Today Flask Class'

@app.route('/about')
def about():
    return 'About our class'


if __name__ == '__main__':
    # port - 5000 default
    # localhost - 127.0.0.1
    app.run(port=5555)
