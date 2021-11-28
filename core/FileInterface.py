from autoloader import *

class FileInterface():
    
    def __init__(self,props):
       self.props=props
       #self.TabNum=TabNum
       #self.get_TabState= self.props['Store'].get_TabState
       #self.set_TabState=self.props['Store'].set_TabState
       self.TabState=self.props['Store'].TabState

    def newfile(self):
        
        self.props['Tabs'].New()
        self.getActiveTab()

    def getActiveTab(self):

        selected=self.props['tab_control'].select()
        index=self.props['tab_control'].index(selected)
        #nb.index(nb.select())
        print(index)
        return index

    def openfile(self,dir=''):
        '''  openfile in binarie mode and return content '''
        props=self.props   
        Tabnum=self.getActiveTab()
        if (len(dir)<1):
            filedir=filedialog.askopenfile(title="select folder")
            try : temp1=filedir.name 
            except:  return 0
            TabName=temp1
        else :
            temp1=dir
            TabName=dir.split('\\')[-1]
        ff=open(temp1,'r')
        data=ff.read()
        ff.close()
        #props['textarea'].insert(INSERT,data)
        #props['Store'].set_data(temp1)
        self.props['Tabs'].New(title=TabName)
        print(self.TabState)
        curTab=self.TabState[len(self.TabState)-1]
        curTab['textarea'].insert(INSERT,data)
        curTab['fildir']=temp1
        props['Store'].set_data(temp1)
        self.TabState[Tabnum]['filedir']=temp1
        return 0

    def savefileas(self):
        '''    save file in new directory   '''
        Tabnum=self.getActiveTab()
        data=self.TabState[Tabnum]['textarea'].get(1.0,END)
        fildir=self.filefactory(data=data)
        self.TabState[Tabnum]['filedir']=fildir
        self.changetabname(titre=fildir)


    def changetabname(self,titre):
        Tabnum=self.getActiveTab()
        self.TabState[Tabnum]['titre']=titre
        print(self.TabState[Tabnum]['titre'])
        self.TabState[Tabnum]['TabFrame'].configure(text = titre)
        print('success renamed')
        return 0

    def savefile(self):
        '''    save file in new directory   '''
        Tabnum=self.getActiveTab()
        props=self.props
        if len(self.TabState[Tabnum]['filedir'])<1: 
            self.savefileas()
            return 0
        #self.TabState[Tabnum]['filedir']=filedir
        curTab=self.TabState[Tabnum]['textarea']
        filedir=props['Store'].get_data()
        if (len(filedir)<1): return 0
        print(filedir)
        data=self.TabState[Tabnum]['textarea'].get(1.0,END)
        ff=open(filedir,'w');ff.write(data);ff.close()
        print('done')
        return 0

   
    def filefactory(self,data=''):
        filedir=filedialog.asksaveasfilename(title="choose destination")
        if (len(filedir)<1): return 0
        print(filedir)
        ff=open(filedir,'w');ff.write(data);ff.close()
        self.props['Store'].set_data(filedir)
        print('done')
        return filedir