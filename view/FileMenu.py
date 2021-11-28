from autoloader import *

class FileMenu():

    def __init__(self,props):
           
        self.props=props
        self.windows=self.props['Views']['windows']
        self.FileInt=FileInterface(self.props)
        self.props['FileInt']=self.FileInt
        self.shortcut()

    def shortcut(self):
        self.NewFile="Ctrl+N"
        self.Openfile="Ctrl+O"
        self.SaveFile="Ctrl+S"
        self.SaveFileAs="Ctrl+Shift+S"
        self.CloseFile="Ctrl+Q"
        self.Exit=""


    def monted(self):

        FileInt=self.FileInt
        MainRoot=self.props['root']
        root=self.windows
        Tab=self.props['Tabs']
        NavBarFrame=Frame(root)
        menu = Menu(NavBarFrame)
        FileBox = Menu(menu)
        Tabnum=0
        FileBox.add_command(label='New File',command=lambda:FileInt.newfile(),accelerator=self.NewFile)
        FileBox.add_command(label='Open File',command=lambda:FileInt.openfile(),accelerator=self.Openfile)
        FileBox.add_command(label='Save',command=lambda:FileInt.savefile(),accelerator=self.SaveFile)
        FileBox.add_command(label='Save As',command=lambda:FileInt.savefileas(),accelerator=self.SaveFileAs)
        FileBox.add_command(label='close file',command=lambda:Tab.Delete(FileInt.getActiveTab()),accelerator=self.CloseFile)
        FileBox.add_command(label='Exit',command=root.quit,accelerator=self.Exit)

        MainRoot.bind("<Control-n>",lambda x :FileInt.newfile())
        MainRoot.bind("<Control-o>",lambda x :FileInt.openfile())
        MainRoot.bind("<Control-s>",lambda x :FileInt.savefile())
        MainRoot.bind("<Control-S>",lambda x :FileInt.savefileas())
        MainRoot.bind("<Control-q>",lambda x :Tab.Delete(FileInt.getActiveTab()))
        
        return FileBox