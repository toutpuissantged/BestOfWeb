from autoloader import *
from tkinter import scrolledtext
import os

class TabContronller(object):

    def __init__(self,props ):
        self.props=props
        self.tab_control = Notebook(props['root'])
        self.tabLen=0
        self.curentTab=1
        self.props['tab_control']=self.tab_control

    def New(self,title='',dir=""):
        self.tabLen+=1
        tabNum=self.tabLen
        TabFrame=Frame(self.tab_control)
        temp1=title.split('/')
        if (len(title)<1): titre = ' Untitled-'+str(tabNum)
        else : titre=temp1[-1]
        self.tab_control.add(TabFrame, text=titre)
        textarea = scrolledtext.ScrolledText(TabFrame,border=0,fg="black",bg="white",width=60,height=20)
        textarea.grid(column=0, row=0)
        
        
        self.tab_control.grid()
        info={
            'titre':titre,
            'filedir':title,
            'textarea':textarea,
            'id':tabNum,
            'TabFrame':TabFrame,
        }
        self.props['Store'].TabState.append(info)
        textarea.bind("<Control-N>",lambda:self.test())
        return textarea

    def test(self):
        print('racourci marche ')

    def Delete(self,Tabnum):

        self.tab_control.forget(Tabnum)
        self.props['Store'].TabState.pop(Tabnum-1)
        print('close successful')

