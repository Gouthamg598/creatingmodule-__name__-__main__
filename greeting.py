print(__name__)
def gree():
    print( 'welcome to module')
    print('imported module greeting')

'''this fuction runs when below statement is true so it is  runs in this folder only 
if we import this module to another program __name__ converted to greeting  so it works only in this program'''
if __name__=="__main__":
    gree()