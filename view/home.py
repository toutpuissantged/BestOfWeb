from tkinter import Label , Button , Frame , StringVar , Entry , Radiobutton
from tkinter.constants import TOP  , RIGHT , YES
import webbrowser as wb
from random import randint as rd

class Home():
    '''
        initial theme from app 
    '''

    def __init__(self,props):
        self.props=props
        self.root=props['root']
        self.var={
            "curtextvar":StringVar()
        }
        self.back='#41B77F'
        self.hm=Frame(self.root,bg=self.back)
        self.fr=Frame(self.root,bg=self.back)
        self.fr2=Frame(self.root,bg=self.back)
        self.fr3=Frame(self.root,bg=self.back)
        self.choix=StringVar()
        self.choix.set("serie")
        self.rech=StringVar()

    def Main(self):

        self.view()
        return 0

    def site(self):

        val = self.choix.get()
        dir = 'config/url/'
        if val=="serie":
            self.cw2["text"]="serie appuiyer"
            source_file="s.url"
        elif val=="film":
            self.cw2["text"]="film appuiyer"
            source_file="f.url"
        elif val=="manga":
            self.cw2["text"]="manga appuiyer"
            source_file="m.url"
        elif val=="torrent":
            self.cw2["text"]="torrent appuiyer"
            source_file="t.url"

        source_file = dir + source_file
        try:
            fd=open(source_file,'r')
            liste1=fd.readlines()
            lon=len(liste1)
            print(liste1)
            wb.open_new_tab(liste1[rd(0,lon-2)])
            self.cw3["text"]=""
            fd.close()
        except :
            self.cw3["text"]=" un probleme est survenu ! vous utilisez une version beta"
        val2 = self.rech.get()
        print(val2)	

    def view (self):
        fr = self.fr
        fr2 = self.fr2
        fr3 = self.fr3
        back = self.back
        choix  = self.choix
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
        self.cw2=Label(fr2,text=choix,font=("Italic",13),bg=back,fg='white')
        self.cw2.pack()
        fr2.pack(side=RIGHT)
        sh=Entry(fr3,width=30,font=("Courrier",9))
        sh.pack()
        sh2=Button(fr3,text="rechercher",width=20,font=("Courrier",9),bg="black",fg="white")
        sh2.pack(padx=2,pady=10)
        haz=Button(fr3,text="lancer un site au hazard",width=30,font=("Courrier",9),bg="white",fg=back,command=self.site)
        haz.pack(padx=2,pady=20)
        fr3.pack(expand=YES)
        self.cw3=Label(self.hm,text="",width=100,font=("Italic",8),bg=back,fg='red')
        self.cw3.pack()
