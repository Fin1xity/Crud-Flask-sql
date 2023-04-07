import sqlite3 as w

class connection:
    def __init__(self):
        self.conn=w.connect('H:/flashproject/sqlite/rituparna.db')
        
    def ret_con(self):
        return self.conn