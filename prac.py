import sqlite3

con = sqlite3.connect('gross_data.db')
cobj = con.cursor()

cobj.execute("CREATE TABLE topmovie(Movie TEXT,Studio TEXT,Grossed TEXT,Dates TEXT)")
con.commit()
cobj.close()
con.close()