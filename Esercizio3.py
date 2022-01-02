# Inizializzo l'oggetto

class CSVFile():
    # Chiamo il costruttore
    def __init__(self, name):
        self.name=name
    
    # Indico il modo di stampare l'intestazione
    def __str__ (self):
        print('Titolo:"{}"'.format(self.name))
    
    # Creo il modulo get_data_vendite che mi estrarrà i dati delle vendite
    def get_data_vendite (self):

        lista=[]

        file=open(self.name,'r')

        for line in file:

            listino=line.split(',')
            listino[-1]=listino[-1].strip()    

            if(listino[0] != 'Date'):
                
                lista.append(float(listino[1]))

        print(lista)

        file.close()
        
        return(lista)
    
    # Creo il modulo get_data che mi estrarrà le date
    def get_data(self):

        data=[]
        file= open(self.name,'r')

        # Importo la funzione datetime
        from datetime import datetime

        for line in file:
            listino=line.split(',')

            if( listino[0] != 'Date'):
                datetime.strptime(listino[0],'%d-%m-%Y')
            
                data.append(listino[0])


        for element in data:
            print(element)

        file.close()

        return(data)


# Istanzio l'oggetto
file1=CSVFile('shampoo_sales.csv')
try:
    print(file1)
except TypeError:
    pass   
# Chiamo le funzioni dell'oggetto
file1.get_data_vendite()

file1.get_data()