import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import sqlite3
from tkinter import *


name = []
stu = []
gro = []

class Work:

	def gui(self,master):

		self.head = Label(master,
						  text="Highest Grossing Movies",
						  font=('Algerian', 20),
						  fg='white',
						  bg='black',
						  padx=30,
						  pady=15
						  )

		self.head.grid(column=0,
					  row=0,
					  columnspan=4)

		self.nu = Label(master,
						text="No.",
						font=('Bahnschrift SemiBold', 15),
						fg='white',
						 bg='black',
						 pady=8,
						 padx=8
						)

		self.nu.grid(column=0,
					row=1
					)

		self.mov = Label(master,
						text="Movie",
						font=('Bahnschrift SemiBold', 15),
						fg='white',
						  bg='black',
						 pady=8,
						 padx=8
						)

		self.mov.grid(column=1,
					  row=1
					  )

		self.stu = Label(master,
						text="Studio",
						font=('Bahnschrift SemiBold', 15),
						fg='white',
						  bg='black',
						 pady=8,
						 padx=8
						)

		self.stu.grid(column=2,
					  row=1
					  )

		self.gro = Label(master,
						text="Grossed",
						font=('Bahnschrift SemiBold', 15),
						fg='white',
						  bg='black',  
						 pady=8,
						 padx=8
						)

		self.gro.grid(column=3,
					  row=1
					)

		self.nu1 = Label(master,
						text="1",
						font=('Lato 10'),
						 fg='white',
						 bg='black'
						)

		self.nu1.grid(column=0,
					  row=2
					  )

		self.mov1 = Label(master,
						  text=name[0],
						  font=('Lato 10'),
						  fg='white',
						  bg='black'
						  )

		self.mov1.grid(column=1,
						row=2
						)

		self.stu1 = Label(master,
						  text=stu[0],
						  font=('Lato 10'),
						  fg='white',
						  bg='black'
						  )

		self.stu1.grid(column=2,
					row=2
					)

		self.gro1 = Label(master,
						 text=gro[0],
						 font=('Lato 10'),
						  fg='white',
						  bg='black'
						 )

		self.gro1.grid(column=3,
						row=2)

		######################################################2nd

		self.nu2 = Label(master,
						text="2",
						font=('Lato 10'),
						  fg='white',
						  bg='black'
						)

		self.nu2.grid(column=0,
					  row=3)

		self.mov2 = Label(master,
						  text=name[1],
						  font=('Lato 10'),
						  fg='white',
						  bg='black'
						  )

		self.mov2.grid(column=1,
						row=3)

		self.stu2 = Label(master,
						  text=stu[1],
						  font=('Lato 10'),
						  fg='white',
						  bg='black'
						  )

		self.stu2.grid(column=2,
					row=3)

		self.gro2 = Label(master,
						 text=gro[1],
						 font=('Lato 10'),
						  fg='white',
						  bg='black'
						 )

		self.gro2.grid(column=3,
						row=3)

		###################################################3rd

		self.nu3 = Label(master,
						text="3",
						font=('Lato 10'),
						  fg='white',
						  bg='black'
						)

		self.nu3.grid(column=0,
					  row=4)

		self.mov3 = Label(master,
						  text=name[2],
						  font=('Lato 10'),
						  fg='white',
						  bg='black'
						  )

		self.mov3.grid(column=1,
						row=4)

		self.stu3 = Label(master,
						  text=stu[2],
						  font=('Lato 10'),
						  fg='white',
						  bg='black'
						  )

		self.stu3.grid(column=2,
					row=4)

		self.gro3 = Label(master,
						 text=gro[2],
						 font=('Lato 10'),
						  fg='white',
						  bg='black'
						 )

		self.gro3.grid(column=3,
						row=4)

		###################################################4th

		self.nu4 = Label(master,
						text="4",
						font=('Lato 10'),
						  fg='white',
						  bg='black'
						)

		self.nu4.grid(column=0,
					  row=5)

		self.mov4 = Label(master,
						  text=name[3],
						  font=('Lato 10'),
						  fg='white',
						  bg='black'
						  )

		self.mov4.grid(column=1,
						row=5)

		self.stu4 = Label(master,
						  text=stu[3],
						  font=('Lato 10'),
						  fg='white',
						  bg='black'
						  )

		self.stu4.grid(column=2,
					row=5)

		self.gro4 = Label(master,
						 text=gro[3],
						 font=('Lato 10'),
						  fg='white',
						  bg='black'
						 )

		self.gro4.grid(column=3,
						row=5)

		###################################################5th

		self.nu5 = Label(master,
						text="5",
						font=('Lato 10'),
						  fg='white',
						  bg='black'
						)

		self.nu5.grid(column=0,
					  row=6)

		self.mov5 = Label(master,
						  text=name[4],
						  font=('Lato 10'),
						  fg='white',
						  bg='black'
						  )

		self.mov5.grid(column=1,
						row=6)

		self.stu5 = Label(master,
						  text=stu[4],
						  font=('Lato 10'),
						  fg='white',
						  bg='black'
						  )

		self.stu5.grid(column=2,
					row=6)

		self.gro5 = Label(master,
						 text=gro[4],
						 font=('Lato 10'),
						  fg='white',
						  bg='black'
						 )

		self.gro5.grid(column=3,
						row=6)

		###################################################6th

		self.nu6 = Label(master,
						text="6",
						font=('Lato 10'),
						  fg='white',
						  bg='black'
						)

		self.nu6.grid(column=0,
					  row=7)

		self.mov6 = Label(master,
						  text=name[5],
						  font=('Lato 10'),
						  fg='white',
						  bg='black'
						  )

		self.mov6.grid(column=1,
						row=7)

		self.stu6 = Label(master,
						  text=stu[5],
						  font=('Lato 10'),
						  fg='white',
						  bg='black'
						  )

		self.stu6.grid(column=2,
					row=7)

		self.gro6 = Label(master,
						 text=gro[5],
						 font=('Lato 10'),
						  fg='white',
						  bg='black'
						 )

		self.gro6.grid(column=3,
						row=7)

		###################################################7th

		self.nu7 = Label(master,
						text="7",
						font=('Lato 10'),
						  fg='white',
						  bg='black'
						)

		self.nu7.grid(column=0,
					  row=8)

		self.mov7 = Label(master,
						  text=name[6],
						  font=('Lato 10'),
						  fg='white',
						  bg='black'
						  )

		self.mov7.grid(column=1,
						row=8)

		self.stu7 = Label(master,
						  text=stu[6],
						  font=('Lato 10'),
						  fg='white',
						  bg='black'
						  )

		self.stu7.grid(column=2,
					row=8)

		self.gro7 = Label(master,
						 text=gro[6],
						 font=('Lato 10'),
						  fg='white',
						  bg='black'
						 )

		self.gro7.grid(column=3,
						row=8)

		###################################################8th

		self.nu8 = Label(master,
						text="8",
						font=('Lato 10'),
						  fg='white',
						  bg='black'
						)

		self.nu8.grid(column=0,
					  row=9)

		self.mov8 = Label(master,
						  text=name[7],
						  font=('Lato 10'),
						  fg='white',
						  bg='black'
						  )

		self.mov8.grid(column=1,
						row=9)

		self.stu8 = Label(master,
						  text=stu[7],
						  font=('Lato 10'),
						  fg='white',
						  bg='black'
						  )

		self.stu8.grid(column=2,
					row=9)

		self.gro8 = Label(master,
						 text=gro[7],
						 font=('Lato 10'),
						  fg='white',
						  bg='black'
						 )

		self.gro8.grid(column=3,
						row=9)

		###################################################9th

		self.nu9 = Label(master,
						text="9",
						font=('Lato 10'),
						  fg='white',
						  bg='black'
						)

		self.nu9.grid(column=0,
					  row=10)

		self.mov9 = Label(master,
						  text=name[8],
						  font=('Lato 10'),
						  fg='white',
						  bg='black'
						  )

		self.mov9.grid(column=1,
						row=10)

		self.stu9 = Label(master,
						  text=stu[8],
						  font=('Lato 10'),
						  fg='white',
						  bg='black'
						  )

		self.stu9.grid(column=2,
					row=10)

		self.gro9 = Label(master,
						 text=gro[8],
						 font=('Lato 10'),
						  fg='white',
						  bg='black'
						 )

		self.gro9.grid(column=3,
						row=10)

		###################################################10th

		self.nu10 = Label(master,
						text="10",
						font=('Lato 10'),
						  fg='white',
						  bg='black'
						)

		self.nu10.grid(column=0,
					  row=11)

		self.mov10 = Label(master,
						  text=name[9],
						  font=('Lato 10'),
						  fg='white',
						  bg='black'
						  )

		self.mov10.grid(column=1,
						row=11)

		self.stu10 = Label(master,
						  text=stu[9],
						  font=('Lato 10'),
						  fg='white',
						  bg='black'
						  )

		self.stu10.grid(column=2,
					row=11)

		self.gro10 = Label(master,
						 text=gro[9],
						 font=('Lato 10'),
						  fg='white',
						  bg='black'
						 )

		self.gro10.grid(column=3,
						row=11)

		###################################################9th


	def wikidat(self):
		self.url = requests.get("https://en.wikipedia.org/wiki/2020_in_film").text

		self.soup = BeautifulSoup(self.url , 'lxml')

		self.table = self.soup.find('table',{'class':'wikitable sortable'})

		self.fa = self.table.findAll('td')

		allten = []

		for i in self.fa:
			oye = i.get_text()
			allten.append(oye)
		
		for i in range(0,len(allten),3):
			name.append(allten[i])


		for i in range(1,len(allten),3):
			stu.append(allten[i])


		for i in range(2,len(allten),3):
			gro.append(allten[i])

	"""
	def sqdata(self):

		con = sqlite3.connect('gross_data.db')
		cobj = con.cursor()
		ajj = self.day

		for i in range(10):
			qu = "INSERT INTO gross_data VALUES(%s,%s,%s,%s)"
			val = (name[i],stu[i],gro[i],ajj)
			cobj.execute(qu,val)
			con.commit()

		cobj.close()
		con.close()
	"""
	def dframe(self):
		
		self.day = date.today()

		self.df = pd.DataFrame()
		self.df['Movie'] = name
		self.df['Studio'] = stu
		self.df['Grossed'] = gro
		self.df['Date'] = self.day

	def csvf(self):

		file = self.df.to_csv("stats.csv",mode='a',index=None,header=True)



root = Tk()
root.title("Hello")
b = Work()
b.wikidat()
b.dframe()
root.configure(background='black')
b.gui(root)
root.mainloop()