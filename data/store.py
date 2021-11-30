
class Store():
    '''
      sert a enregistrer les etats 

    '''
    def __init__(self,id: int):
        data={
            'filedir': '',
        }
        self.id : int = id
        self.data=data
        self.TabState=[]

    def get_data(self):
        return self.data

    def set_data(self,newdata):
        self.data=newdata
        return 0
