
#================#
#Moduli importati#
#================#

from datetime import datetime

#============================#
# Estendo la classe Exception#
#============================#

class ExamException(Exception):
    pass
    
#=================================#   
# Creo la classe CSVTimeSeriesFile#
#=================================#

class CSVTimeSeriesFile:
    
    #Costruttore
    def __init__(self,name):
        
        self.name=name
        
        if not isinstance(self.name,str):
            raise ExamException('Il nome del file deve essere una stringa')
            
        self.can_read=True
        
    #Modulo get_data
    def get_data(self):
        
        # Controllo che il file esista
        try:
            file=open(self.name,'r')
            file.readline()
            
        except Exception :
            self.can_read=False
            
        #Se il file non esiste
        if not self.can_read:
            
            print('File inesistente')
            return(None)

        #Se il file esiste
        else:
            
            # Creo tre liste con vari utilizzi:
            # data serve a creare una lista di liste
            # time serve per controllare che le time stamp siano ordinate e non siano presenti dei doppioni
            # new copia la lista data, eliminando le righe in cui il valore dei passeggeri non è positivo e intero
            
                 data=[]
                 time=[]
                 new=[]
            
            # apro il file in modalità lettura
                 file=open(self.name,'r')
    
                # ciclo sul file
                 for line in file:
                        
                        tmp=line.split(',')
                     
                        # Gestisco il caso della prima riga
                        if(tmp[0]!= 'date'):
                            
                            #Controllo che tmp[0] sia una data e in caso abbia un riscontro negativo salto la riga
                            controllo=True
                            
                            try:
                                time_stamp=datetime.strptime(tmp[0],'%Y-%m')
                                
                            except Exception:
                                controllo=False
                                
                            if not controllo:
                                pass
                                
                            else:
                                #Elimino gli spazi \n
                                tmp[-1]=tmp[-1].strip()
                                
                                # Controllo l'ordine delle timestamp e che non ci siano doppioni
                                if time is None:
                                    time.append((time_stamp))
                                else:
                                    
                                    for element in time:
                                        #Se la data è ripetuta
                                        if time_stamp==element:
                                            raise ExamException('Il time stamp {} è un doppio. '.format(time_stamp))
                                        #Se la data è disordinata
                                        elif time_stamp<time[-1]:
                                            raise ExamException('La data {} non è ordinata'.format(time_stamp))
                                            
                                  
                                    time.append(time_stamp)
                                            
                                
                                #Creo la mia lista di liste
                                data.append(tmp)   

                                
        # Cernisco la lista 'data', togliendo le liste che presentano valori che non mi interessano
                                
        for element in data:
            
            try:
                value=int(element[1])
                
            except Exception:
                continue
                
            if value>0:
                
                Lista=[]
                Lista.append(element[0])
                Lista.append(value)
                new.append(Lista)
                
            else:
                continue
                
        # Chiudo il file
        file.close()

        if not isinstance(new,list):
            raise ExamException('L output della funzione get_data non è una lista')
        else:
            return(new)



#=========================================================#
#Definisco la funzione 'detect_similar_monthly_variations'#
#=========================================================#

def detect_similar_monthly_variations(time_series, years):
    
    # Controllo di time_series #
    
    if not isinstance(time_series,list):
        raise ExamException('L input della funzione deve essere una lista')
        
    for lista in time_series:
        if not isinstance(lista,list):
            raise ExamException('L elemento all indice {} non è una lista. Elemento: {}'.format(i,lista))
            
    # Controllo di years #     
            
    if not isinstance(years,list):
        raise ExamException('L input della funzione deve essere una lista')
    
    if len(years)!=2:
        raise ExamException('La lista contenente gli anni da confrontare deve essere di due elementi')
        
    if not isinstance(years[0],int):
        # Provo a convertire years_0 in formato intero
       
        try:
            years[0]=int(years[0])
                
        except Exception:
            raise ExamException('Impossibile riconvertire l anno {} in tipo intero'.format(years[0]))
            
          
        
    if not isinstance(years[1],int):
        # Provo a convertire years_1 in formato intero
            try:
                years[1]=int(years[1])
            except Exception as e:   
                raise ExamException('Impossibile riconvertire l anno in tipo intero'.format(years[1]))
        
    if years[0]<=0 or years[1]<=0:
            raise ExamException('Gli anni da valutare devono essere positivi')
       
    if years[1]-years[0]!=1:
        raise ExamException('Gli anni non sono consecutivi')
        
#================================================================# 
# Controllo che gli elementi di years appartengano a time_series #
#================================================================#

    # Creo delle variabili flag per controllare l'appartenenza degli elementi di years
        
    check1=False
    check2=False
    
    for item in time_series:
        
        sub_list=item[0].split('-')
        
        if int(sub_list[0])==years[0]:
            check1=True
            
        if int(sub_list[0])==years[1]:
            check2=True
    
    if check1 and check2:
        
        # Ho verificato che gli anni sono presenti all'interno di time_series
        # Creo una lista con tutti i mesi dell anno con gennaio all'indice 0
        
        mesi=['gennaio','febbraio','marzo','aprile','maggio','giugno','luglio','agosto','settembre','ottobre','novembre','dicembre']
        
        # Creo due dizionari per legare il numero di passeggeri al corrispettivo mese
        
        passeggeri0={}
        passeggeri1={}

        for lista in time_series:
            
                # Creo una lista splittano il primo elemento delle list in time_series
                sub_list=lista[0].split('-')
            
                # Converto in intero gli elementi della nuova lista, che userò per riempire i dizionari
            
                time_year=int(sub_list[0])
                month=int(sub_list[1])

                
                if time_year<=years[1]:
                    
                    
                    if time_year==years[0]:
                       # Utilizzo la lista mesi che ho definito sopra
                        
                            mese=mesi[month-1]
                            passeggeri0[mese]=lista[1]
                        
                    if time_year==years[1]:
                            mese=mesi[month-1]
                            passeggeri1[mese]=lista[1]
                        
        #Controlo che effivamente ci sia una misurazione per ogni anno
                        
        if len(passeggeri0)<=1:
            raise ExamException('Deve esserci almeno una misurazione all anno. Anno da controllare:{} '.format(years[0]))
            
        if len(passeggeri1)<=1:
            raise ExamException('Deve esserci almeno una misurazione all anno. Anno da controllare:{} '.format(years[1]))
        
        print(passeggeri0)
        print(passeggeri1)

        differenza=0
        result=[]
        
        for i in range(11):
            
            # prova è una variabile che mi indica se si sono presentati i casi in cui non posso fare la misurazione della differenza tra gli anni
            
            prova=1
            
            try:
                #Faccio la differenza tra i mesi consecutivi del primo anno e del secondo, poi le confronto
                
                differenza1=passeggeri0[mesi[i+1]]-passeggeri0[mesi[i]]
                differenza2=passeggeri1[mesi[i+1]]-passeggeri1[mesi[i]]
                differenza=abs(differenza1-differenza2)
                
            except KeyError:
                prova=prova*0
           

            if differenza<=2 and prova==1:
                result.append(True)
                
            elif differenza>2 or prova==0:
                result.append(False)

        
       
        print(result)
        
        # Controllo che result sia una lista
        if not isinstance(result,list):
            raise ExamException('L output deve essere una lista')
            
        #Controllo che la lista result sia di 11 elementi
        if len(result)!=11:
            raise ExamException('La lista-output deve essere lunga 11')

        return(result)
        
    else:
        
        # Se uno dei due anni non appartiene a time_series
        raise ExamException('Controllo di appartenenza elementi di years fallito')



