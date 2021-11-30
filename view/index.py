from autoloader import  Frame , Menu , FileMenu , EditMenu , HelpMenu
from .home import Home

class Index():
    ''' entry class for organize user interface '''

    def __init__(self,props):
        self.props=props
        self.props['Views']['windows']=Frame(self.props['root'])

    def main(self):

        root=self.props['root']
        menubar = Menu(root)
        self.props['Views']['Menu']=menubar
        root.config(menu=menubar)
        
        File=FileMenu(props=self.props).monted()
        Edit=EditMenu(props=self.props).monted()
        Help=HelpMenu(self.props).monted()

        menubar.add_cascade(label='File', menu=File)
        menubar.add_cascade(label='Edit', menu=Edit)
        menubar.add_cascade(label='Help', menu=Help)

        Home(props=self.props).Main()

        return 0