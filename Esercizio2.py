

class CSVFile():

    def __init__(self,name):
        self.name=name
    
    def get_data(self):
        Lista=[]
        file=open(self.name,'r')
        
        from datetime import datetime
        
        for line in file:
            
            Listino=line.split(',')
             
            if(Listino[0] != 'Date'):
              
                Lista.append(Listino[0])
              

        for item in Lista:
            datetime.strptime(item,'%d-%m-%Y')

        for item in Lista:
            print(item)
        

file1=CSVFile('shampoo_sales.csv')

file1.get_data()

