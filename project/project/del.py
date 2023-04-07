from flask import Flask,request,render_template
import sqlite3 as w

app=Flask(__name__)

def connect():
   con=w.connect('H:/flashproject/sqlite/rituparna.db')
   cur=con.cursor()
   return con,cur

@app.route('/',methods=['GET','POST'])
def talk():
    if request.method == 'POST':
        n=int(request.form.get('n1'))
        q='DELETE FROM PRODUCTS WHERE PID = ?'
        try:
            connec,cursor=connect()
            cursor.execute(q,(n,))
            print ("Data deleted")
            connec.commit()
    
        except Exception as s: 
            print ('Error',s)   
            connec.rollback() 
            connec.close()    
     
    return render_template('index.html')  


if __name__=='__main__':
    app.run()
            
                
        