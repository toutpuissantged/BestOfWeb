from autoloader import *

class HelpMenu(FileMenu):

    def __init__(self,props):
        self.props=props
        self.windows=self.props['Views']['windows']    
        self.MyMenu=self.props['Views']['Menu'] 

        self.shortcut()

    def shortcut(self):
        self.About="" 
        self.Release=""

    def monted(self):
        root=self.windows
        Tab=self.props['Tabs']
        NavBarFrame=Frame(root)
        menu = Menu(NavBarFrame)
        HelpBox = Menu(menu)
        
        Tabnum=0
        HelpBox.add_command(label='About',command=lambda:print(),accelerator=self.About)
        HelpBox.add_command(label='Release',command=lambda:print(),accelerator=self.Release)

        return HelpBox