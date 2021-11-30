from tkinter import Label , Button , Frame , StringVar , Radiobutton
from tkinter.constants import TOP  , RIGHT , YES 
from typing import Any
import webbrowser as wb
from random import randint as rd
from typing import TypedDict

class State(TypedDict):
    text: str
    error : str 

class Home():
    '''
        initial theme from app 
    '''

    def __init__(self,props):
        self.props=props
        self.root=props['root']
        self.back= props['Info'].Design['Color']['Background']
        self.TextColor : str = props['Info'].Design['Color']['Text']
        self.ButtonColor : str  = props['Info'].Design['Color']['Button']
        self.ButtonTextColor: str   = props['Info'].Design['Color']['ButtonText']
        self.ButtonHoverColor: str   = props['Info'].Design['Color']['ButtonHover']
        self.BackgroundColor : str  = props['Info'].Design['Color']['Background']
        self.EntryColor : str   = props['Info'].Design['Color']['Entry']
        self.EntryTextColor : str   = props['Info'].Design['Color']['EntryText']
        self.MainFrame : Frame = Frame(self.root,bg=self.back)
        self.TitleFrame : Frame = Frame(self.root,bg=self.back)
        self.ChoiseFrame : Frame = Frame(self.root,bg=self.back)
        self.BodyFrame : Frame = Frame(self.root,bg=self.back)
        self.choix : StringVar = StringVar()
        self.choix.set("Serie")
        self.rech : StringVar = StringVar()
        self.rech.set("")
        self.source_file : str = "s.url"
        self.State : State = {
            "text":"Serie",
            "error":""
        }
        self.monted()

    def Main(self) -> bool :
        self.view()
        return 0

    def monted(self)->bool:
        """ 
            monted all frame
        """

        self.MainFrame.pack(expand=YES)
        self.TitleFrame.pack(side=TOP)
        self.ChoiseFrame.pack(side=RIGHT)
        self.BodyFrame.pack(expand=YES)

        return 0

    def Button (self,text : str ,command , padx : int = 0 , pady : int = 0 ) -> bool :
        """
            create button
            keyword arguments:
            text -- the text of the button
            command -- the command of the button
            padx -- the padx of the button (default 0)
            pady -- the pady of the button (default 0)
            
        """

        haz=Button(self.BodyFrame,highlightbackground=self.TextColor,text=text,width=30,border=0,relief="flat",font=("Courrier",9),bg=self.ButtonColor,fg=self.ButtonTextColor,command=command)
        haz.pack(padx=padx,pady=pady)
        return 0

    def openWebBrowser(self,url):
        """
            open web browser
            keyword arguments:
            url -- the url of the site
        """

        wb.open_new_tab(url)

    def RadioButton(self, text : str, anchor : str ="w") -> bool : 
        """
            create radio button
            keyword arguments:
            text -- the text of the button
            anchor -- the anchor of the button (default "w")
        """

        b1=Radiobutton(self.ChoiseFrame,text=text,variable=self.choix,value=text,font=("Courrier",9),bg=self.back,fg=self.TextColor,anchor=anchor)
        b1.pack(anchor = anchor)
        return 0

    def site (self) -> bool :
        """
            open the site
        """

        val = self.choix.get()
        dir : str = 'config/url/'
        stateFull : str = ["Serie","Film","Manga","Torrent"]
        for i in stateFull:
            if i == val:
                self.State["text"] = i
                self.source_file = dir + i + ".url"
                break
        try:
            with open(self.source_file,"r") as f:
                urls = f.readlines()
                urlsLength=len(urls) 
                self.openWebBrowser(urls[rd(0,urlsLength-2)])
                self.State["error"]=" correctement rendu"

        except FileNotFoundError :
            self.State["error"]=" un probleme est survenu !"
        return 0	

    def Title(self) -> bool :
        """
            create the title of the app
        """
        Titre=Label(self.TitleFrame,text="Best Of Web",font=("Courrier",20),bg=self.BackgroundColor,fg=self.TextColor)
        Titre.pack()
        SousTitre=Label(self.TitleFrame,text="Le Meilleur Du Web En Un Clique",font=("Courrier",9),bg=self.BackgroundColor,fg=self.TextColor)
        SousTitre.pack()
        return 0

    def Label(self,text : str) -> bool :
        """
            create a label

            Keyword arguments:
            text -- the text of the label
        """

        label=Label(self.ChoiseFrame,text=text,font=("Italic",13),bg=self.BackgroundColor,fg=self.TextColor)
        label.pack()
        return 0

    def view (self):
        """
        design the interface
        """

        self.Title()        
        self.Label("Categorie de site")
        self.RadioButton("Serie","w")
        self.RadioButton("Film","w")
        self.RadioButton("Manga","w")
        self.RadioButton("Torrent","w")
        self.Button("Lancer un site au hazard" ,self.site)
        
        
