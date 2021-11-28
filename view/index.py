from autoloader import *

class Index():
    ''' entry class for organize user interface '''

    def __init__(self,props):
        self.props=props
        self.props['Views']['windows']=Frame(self.props['root'])

    def main(self):

        root=self.props['root']
        menubar = Menu(root)
        props=self.props
        self.props['Views']['Menu']=menubar
        root.config(menu=menubar)
        
        File=FileMenu(props=props).monted()
        Edit=EditMenu(props=props).monted()
        Help=HelpMenu(props).monted()

        menubar.add_cascade(label='File', menu=File)
        menubar.add_cascade(label='Edit', menu=Edit)
        menubar.add_cascade(label='Help', menu=Help)

        BaseTheme(props=props).Main()

        return 0