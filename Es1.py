class CSVFile:
    
    def __init__(self,name):
        self.name=name;
    
    def somma(self):
         Lista=[]

         file=open(self.name,'r')

       
         for line in file:

            Lista_in=line.split(',')
                
            
            if Lista_in[0] != 'Date':
                Data=Lista_in[0]
                Value=Lista_in[1]
                Lista.append(float(Value))
                    
         file.close()

         return(Lista)

csv_file=CSVFile('shampoo_sales.csv')
Element=csv_file.somma()

for item in Element:
    print(item)

print((Element))