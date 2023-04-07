
from flask import Flask,request,render_template
from connect import *



class Read:
    #@app.route("/readout")
    def data(self):
        name=request.args.get('t1')
        a=aconnect()
        cur=a.ret_con().cursor()
        query="Select * from {};".format(name)
        try:
            cur.execute(query)
            rows=cur.fetchall()
            return render_template('read.html',rows=rows)
        except Exception as r:
            return render_template('read.html',error=name)
        
    
    #@app.route("/read")
    def index(self):
        return render_template('read.html')
