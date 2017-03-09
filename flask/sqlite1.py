import sqlite3

conn = sqlite3.connect('lionEagle.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, username TEXT, password TEXT)')

def data_entry():
	c.execute("INSERT INTO stuffToPlot VALUES('lex', 'passw')")
	conn.commit()
	c.close()
	conn.close()

create_table()
data_entry