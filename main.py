from tkinter import *
import webbrowser as wb
from random import randint as rd

back='#41B77F'
def site():
	val=choix.get()
	dir = 'config/'
	if val=="serie":
		cw2["text"]="serie appuiyer"
		source_file="s.config"
	elif val=="film":
		cw2["text"]="film appuiyer"
		source_file="f.config"
	elif val=="manga":
		cw2["text"]="manga appuiyer"
		source_file="m.config"
	elif val=="torrent":
		cw2["text"]="torrent appuiyer"
		source_file="t.config"

	source_file = dir + source_file
	try:
		fd=open(source_file,'r')
		liste1=fd.readlines()
		lon=len(liste1)
		print(liste1)
		wb.open_new_tab(liste1[rd(0,lon-2)])
		cw3["text"]=""
		fd.close()
	except :
		cw3["text"]=" un probleme est survenu ! vous utilisez une version beta"
	val2=rech.get()
	print(val2)	

#

hm=Tk()
hm.geometry("500x400")
hm.title("BestOfWeb__BETA")
hm.config(background=back)
fr=Frame(hm,bg=back)
fr2=Frame(hm,bg=back)
fr3=Frame(hm,bg=back)
hm.resizable(False,False)
choix=StringVar()
choix.set("serie")
rech=StringVar()

#

Titre=Label(fr,text="Best Of Web",font=("Courrier",20),bg=back,fg='white')
Titre.pack()
SousTitre=Label(fr,text="Le Meilleur Du Web En Un Clique",font=("Courrier",9),bg=back,fg='white')
SousTitre.pack()
fr.pack(side=TOP)
cw=Label(fr2,text="Categorie de site",font=("Italic",13),bg=back,fg='white')
cw.pack()
b1=Radiobutton(fr2,text="serie en stream",variable=choix,value="serie",font=("Courrier",9),bg=back,fg='black')
b1.pack(anchor="w")
b1=Radiobutton(fr2,text="film en stream",variable=choix,value="film",font=("Courrier",9),bg=back,fg='black')
b1.pack(anchor="w")
b1=Radiobutton(fr2,text="manga en stream ",variable=choix,value="manga",font=("Courrier",9),bg=back,fg='black')
b1.pack(anchor="w")
b1=Radiobutton(fr2,text="site Torrent ",variable=choix,value="torrent",font=("Courrier",9),bg=back,fg='black')
b1.pack(anchor="w")
cw2=Label(fr2,text=choix,font=("Italic",13),bg=back,fg='white')
cw2.pack()
fr2.pack(side=RIGHT)
sh=Entry(fr3,width=30,font=("Courrier",9))
sh.pack()
sh2=Button(fr3,text="rechercher",width=20,font=("Courrier",9),bg="black",fg="white")
sh2.pack(padx=2,pady=10)
haz=Button(fr3,text="lancer un site au hazard",width=30,font=("Courrier",9),bg="white",fg=back,command=site)
haz.pack(padx=2,pady=20)
fr3.pack(expand=YES)
cw3=Label(hm,text="",width=100,font=("Italic",8),bg=back,fg='red')
cw3.pack()

#

hm.mainloop()