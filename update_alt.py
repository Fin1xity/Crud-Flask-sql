  
from flask import Flask,request,render_template
from connect import *



class Update:
    #@app.route("/readout")
    def data(self):
        id_reg=request.args.get('id')
        id_val=request.args.get('id_val')
        table =request.args.get('table')
        col1  =request.args.get('col1')
        val1  =request.args.get('val1')
        col2  =request.args.get('col2')
        val2  =request.args.get('val2')
        a=aconnect()
        conn = a.ret_con()
        cur=a.ret_con().cursor()
        if col1 == '':
            query="Update {} set {}= {} where {} = {};".format(table,col2,val2,id_reg,id_val)
        elif col2 == '':
            query="Update {} set {}= {} where {} = {};".format(table,col1,val1,id_reg,id_val)
        else:
            query="Update {} set name= {}, game= {} where ID = {};".format(table,val1,val2,id_val)
        try:
            cur.execute(query)
            conn.commit()
            return render_template('update.html',done = id_reg)
        except Exception as r:
            conn.rollback()
            return render_template('update.html',error = id_reg)
        
    
    #@app.route("/read")
    def index(self):
        return render_template('update.html')
            
                
        