from tkinter import *
from controllers.search import Search

class BaseTheme():
    '''
        initial theme from app 
    '''

    def __init__(self,props):
        self.props=props
        self.root=props['root']
        props['BaseTheme']=''
        self.var={
            "curtextvar":StringVar()
        }

    def Main(self):
        props=self.props
        root=props['root']

        self.TheEntry().grid(row=0,column=0,padx=10,pady=10)
        self.TheButton().grid(row=1,column=0,padx=20,pady=20)

        Button()
        Entry()
        return 0

    def TheEntry(self):

        TheEntry=Entry(self.root, width='30',border=0,bg="white",fg='black',borderwidth=0,font="arial",textvariable=self.var['curtextvar'])
        return TheEntry

    def TheButton(self):

        TheButton=Button(self.root,text='lancer',width='10',border=0,bg="royalblue",activebackground='blue',fg='white',padx=10,pady=10,activeforeground='white',font="arial",command=lambda:Search().Test(self.var['curtextvar']))
        return TheButton

