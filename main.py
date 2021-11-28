from autoloader import *

info=JsonParser('config/info.json').parse()

root = Tk()
root.geometry(info['AppScreen'])
root.title(info['AppName'])
root.resizable=False

#root.iconphoto(False, PhotoImage(file = 'assets/icon.png'))

NewStore= Store(1)

props={
    'root':root,
    'textarea':[],
    'Store':NewStore,
    'Tabs':'',
    'CurrentActiveTabIndice':0,
    'Views':{}
}

FileInt=FileInterface(props)

ViewsEntry=Index(props=props)
ViewsEntry.main()

ArgsParse.parse(props=props)

root.mainloop()