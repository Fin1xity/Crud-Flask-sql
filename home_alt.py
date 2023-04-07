
from flask import Flask,request,render_template
from connect import *



class Home:
    #@app.route("/read")
    def index(self):
        return render_template('home.html')
    
    
