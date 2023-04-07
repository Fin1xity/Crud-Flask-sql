from flask import Flask
from create_alt import *
from read_alt import *
from home_alt import *
from delete import *
from update_alt import *


app = Flask(__name__)

b = Create()
c = Read()
h = Home()
d = Delete()
u = Update()

app.add_url_rule('/','a',h.index)
app.add_url_rule('/home','h',h.index)
app.add_url_rule('/create','f',b.index)
app.add_url_rule('/table','d',b.table)
app.add_url_rule('/tableout','e',b.tableout)
app.add_url_rule('/input','i',b.input)
app.add_url_rule('/inputout','j',b.inputout)
app.add_url_rule('/readout','o',c.data)
app.add_url_rule('/read','n',c.index)
app.add_url_rule('/delete','w',d.delete)
app.add_url_rule('/deleteout','y',d.deleteout)
app.add_url_rule('/up','z',u.index)
app.add_url_rule('/upout','m',u.data)


if __name__ == '__main__':
    app.run(debug=True)