import sys

class ArgsParse(object):
    ''' 
     Class to parse cli arguments given 
    '''
    
    def __init__(self):
        pass

    @staticmethod
    def parse(props):
        #FirstTab=props['Tabs'].New()
        args=sys.argv
        print(args)
        if (len(args)<2):  
            return 0
        #props['FileInt'].openfile(dir=args[1])
        #props['Tabs'].Delete(Tabnum=0)
        return 0
        
        