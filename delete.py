
from flask import Flask,request,render_template
from connect import *



class Delete:
    
    def deleteout(self):
        a=aconnect()
        conn = a.ret_con()
        cur=conn.cursor()
        tname = request.args.get('tname')
        
        
        ca1 = request.args.get('c1')
        val = request.args.get('val')

          
        query = "delete from {} where {} = {};".format(tname,val,ca1)
        try:
            cur.execute(query)
            conn.commit()
            return render_template('delete.html',done=tname)
        except Exception as r:
            return render_template('delete.html',error=tname)
        
    
    #@app.route("/read")
    def delete(self):
        return render_template('delete.html')