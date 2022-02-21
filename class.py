class CSVFile:
    def __init__(self,name):
        
        self.name=name
        self.can_read=True

        if type(self.name) is not str:
            raise Exception('Il nome del file non è una stringa')

        try:
            file=open(self.name,'r')
            file.readline()
        except Exception as e:
            self.can_read=False
            
    
                
        
    def get_data(self,start=None,end=None):

        if not self.can_read:
            print('File inesistente')
            return(None)

        else:
            if start==None and end==None:
                 data=[]
            
            # apro il file in modalità lettura
                 file=open(self.name,'r')
    
                # ciclo sul file
                 for i,line in enumerate(file):
                        #splitto ogni riga alla virgola
                        tmp=line.split(',')
    
                        # Gestisco il caso della prima riga
                        if(tmp[0]!= 'Date'):
    
                            #Elimino gli spazi \n
                            tmp[-1]=tmp[-1].strip()
    
                             
                            data.append(float(tmp[1]))
                
            
            else:
                if start > end:
                   tmp=start
                   start=end
                   end=tmp

                if start<=0:
                   start=1

                if end>37:
                    end=37
            # preparo la lista vuota
                data=[]
                
                # apro il file in modalità lettura
                file=open(self.name,'r')
    
                # ciclo sul file
                for i,line in enumerate(file,1):
    
                    if i < start:
                        pass
    
                    if i >= start and i <= end:
                        
                    
                        #splitto ogni riga alla virgola
                        tmp=line.split(',')
    
                        # Gestisco il caso della prima riga
                        if(tmp[0]!= 'Date'):
    
                            #Elimino gli spazi \n
                            tmp[-1]=tmp[-1].strip()
     
                            data.append(tmp)
    
                # Chiudo il file e ritorno data 

            file.close()

            return(data)

class NumericalCSVFile(CSVFile):

    # Costruttore
    def __init__(self,name):
        super().__init__(name)
    
    def get_data(self):

        # Costruisco una lista per contenere i nuovi dati
        num_data=[]

        # Chiamo la funzione della classe padre
        data=super().get_data()

        # apro il file
        file=open(self.name,'r')

        # Annido due cicli for
        for element in data:

            for i,part in enumerate(element):

                if i==0:
                    num_data.append(part)
                else:
                    try:
                        num_data.append(float(part))
                    except Exception as e:
                        print('Errore di conversione:{}'.format(e))
                        break

        file.close()
        return(num_data)

        # Chiudo il file
       
                
                

            



file1=CSVFile('shampoo_sales.csv')

data=file1.get_data(23,66)

for element in data:
    line=element[0].split('-')
    print(line)




