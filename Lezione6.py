# Inizializzo l'oggetto

class CSVFile():
    # Chiamo il costruttore
    def __init__(self, name):
        self.name=name
        self.can_read=True

        try:
            file=open(self.name,'r')
        except Exception as e:
            self.can_read= False
            print('File inesistente.\nRilevato l errore:{}'.format(e))
    
    # Creo il modulo get_data_vendite che mi estrarrà i dati delle vendite
    def get_data(self, start= 1,end= 36):
        if self.can_read == True:
               
            lista=[]
            
            if start <= 0 or end <=0:
                
                 raise Exception ('Attenzione a indicare start ed end. non devono essere minori di 0')

                 print('Start={}'.format(start))

                 print('End={}'.format(end))
              

            if end < start :
               
                raise Exception('Attenzion che end non deve essere minore di start')

                print('Start={}'.format(start))

                print('End={}'.format(end))
              
            
            if end > 36:

                raise Exception('Attenzion che end supera il numero di righe del file')

                print('End={}'.format(end))
              

            file=open(self.name,'r')


            for line in file:

                listino=line.split(',')
                listino[-1]=listino[-1].strip()    

                if(listino[0] != 'Date'):
                    
                    lista.append(listino)
            
       
            for i,element in enumerate(lista,1):

                if i >= start and i<=end:

                    print(i,element)

                else:

                    pass

         
            file.close()
            
            return(lista)
        
        # Creo il modulo get_data che mi estrarrà le date
    def get_date(self):

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

# Corpo del programma

file1=CSVFile('shampoo_sales.csv')

print('Title:"{}""'.format(file1.name))
file1.get_data()

