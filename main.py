from autoloader import *

Info = JsonParser('config/info.json').parse()
AppInfo = Info.AppInfo()
Design = Info.design()
root = Tk()
root.geometry(AppInfo['AppScreen'])
root.title(AppInfo['AppName'])
root.resizable=False
#couleur de fond
root.configure(background=Design['Color']['Background'])

#root.iconphoto(False, PhotoImage(file = 'assets/icon.png'))

NewStore= Store(1)

props={
    'root':root,
    'textarea':[],
    'Store':NewStore,
    'Tabs':'',
    'CurrentActiveTabIndice':0,
    'Views':{},
    'Info':Info
}

FileInt=FileInterface(props)

ViewsEntry=Index(props=props)
ViewsEntry.main()

ArgsParse.parse(props=props)

root.mainloop()