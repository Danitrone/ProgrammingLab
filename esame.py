

# Estendo 
class ExamException(Exception):
    pass




class CSVFile:
    def __init__(self,name):
        
        self.name=name
        if not isinstance(self.name,str):
            raise ExamException('Il nome del file deve essere una stringa')
            
        self.can_read=True
        
      
    
                
        
    def get_data(self,start=None,end=None):
        try:
            file=open(self.name,'r')
            file.readline()
            
        except Exception :
            self.can_read=False
            
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
                        try:
                            tmp=line.split(',')
                            
                        except Exception:
                            raise ExamException('Errore nello split della linea {}:{}'.format(i,line))
    
                        # Gestisco il caso della prima riga
                        if(tmp[0]!= 'date'):
    
                            #Elimino gli spazi \n
                            tmp[-1]=tmp[-1].strip()
    
                             
                            data.append((tmp))
                
            
            else:
                
                if start > end:
                   raise ExamException('Start deve essere minore di end')

                if start<=0 or end <=0:
                    raise ExamException('I parametri di confine non possono essere minori di zero')
                   

                if end>145 or start>145:
                    raise ExamException('I parametri di confine non possono superare il numero di righe del file')
                    
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
                        
                        if tmp[0]!='date':
                            #Elimino gli spazi \n
                            tmp[-1]=tmp[-1].strip()
     
                            data.append(tmp)
    
                # Chiudo il file e ritorno data 

            file.close()

            return(data)

time_series_file=CSVFile(name='daa.csv')
time_series=time_series_file.get_data(140,145)

#for i,list in enumerate(data):
 #   print(i,list)