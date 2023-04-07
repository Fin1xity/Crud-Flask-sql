
from flask import Flask,request,render_template
from connect import *



class Create:
    
    #@app.route("/create")
    def index(self):
        
        return render_template('create.html')
    
    
    def tableout(self):
        a=aconnect()
        conn = a.ret_con()
        cur=a.ret_con().cursor()
        tname = request.args.get('tname')
        
        
        ca1 = request.args.get('c1')
        val = request.args.get('data1')
        
            
        ca2 = request.args.get('c2')
        va = request.args.get('data2')
        
            
        ca3 = request.args.get('c3')
        v = request.args.get('data3')
        
            
        query = " create table {} ({} {} PRIMARY KEY,{} {},{} {});".format(tname,ca1,val,ca2,va,ca3,v)
        try:
            cur.execute(query)
            conn.commit()
            return render_template('table.html',done=tname)
        except Exception as r:
            return render_template('table.html',error=tname)
    
    
    #@app.route("/table")
    def table(self):
        return render_template('table.html')
        

    
    #@app.route("/input")
    def input(self):
        return render_template('input.html')
    
    
    def inputout(self):
        a=aconnect()
        conn = a.ret_con()
        cur=a.ret_con().cursor()
        tname = request.args.get('tname')
        
        def sitre(val,ca):
            if val == "INTEGER":
                return ca
            else:
                c ="'{}'".format(ca)
                return  c
        
        
        c1 = request.args.get('c1')
        va1 = request.args.get('data1')
        ca1 = sitre(va1,c1)
        
            
        c2 = request.args.get('c2')
        va2 = request.args.get('data2')
        ca2 = sitre(va2,c2)
            
        c3 = request.args.get('c3')
        va3 = request.args.get('data3')
        ca3 = sitre(va3,c3)
        
         
        query = "insert into {} values({},{},{});".format(tname,ca1,ca2,ca3)
        try:
            cur.execute(query)
            conn.commit()
            return render_template('input.html',done=tname)
        except Exception as r:
            return render_template('input.html',error=tname)
        
