from flask import Flask,request,render_template
import sqlite3 as w

app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def talk():
    if request.method == 'POST':
        n=request.form.get('n1')
        try:
            con=w.connect('H:\database(sqlite)\database_project\proj_1.db')
            cur=con.cursor();
            cur.execute('DELETE FROM PRODUCTS WHERE NAME = ?', (n,))
            print ("Data deleted")
    
        except Exception as s: 
            print ('Error',s)   
            con.rollback() 
            con.close()    
     
    return render_template('index.html')  


if __name__=='__main__':
    app.run()
            
                
        