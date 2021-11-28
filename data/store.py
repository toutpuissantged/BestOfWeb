
class Store():
    '''
      sert a enregistrer les etats 

    '''
    def __init__(self,id):
        data={
            'filedir': '',
        }
        self.id=id
        self.data=data
        self.TabState=[]

    def get_data(self):
        print(" return self.data")
        return self.data

    def set_data(self,newdata):
        print("self.data=newdata")
        self.data=newdata
