
import sqlite3 as s

class aconnect:
    def __init__(self):
        self.conn=s.connect('.\sqlite\hehe.db')
        
    def ret_con(self):
        return self.conn