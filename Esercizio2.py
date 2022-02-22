from datetime import datetime

class CSVFile():

    def __init__(self,name):
        self.name=name
    
    def get_data(self):
        Lista=[]
        file=open(self.name,'r')
        
       
        
        for line in file:
            
            Listino=line.split(',')
             
            if(Listino[0] != 'Date'):
              
                my_date=datetime.strptime(Listino[0],'%d-%m-%Y')
                Lista.append(Listino[0])
            
        print(Lista)
        
        for element in Lista:
    
            if element!=datetime.strptime(element,'%d-%m-%Y'):
                print('False')
            else:
                print('True')
        
        

file1=CSVFile('shampoo_sales.csv')

file1.get_data()

