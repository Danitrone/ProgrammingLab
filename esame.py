
#================#
#Moduli importati#
#================#


from datetime import datetime

# Estendo la classe Exception 
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
                 data=[]
                 time=[]
            # apro il file in modalità lettura
                 file=open(self.name,'r')
    
                # ciclo sul file
                 for line in file:
                        
                        tmp=line.split(',')
                     
                        # Gestisco il caso della prima riga
                        if(tmp[0]!= 'date'):
                            
                            #Controllo che tmp[0] sia una data
                            controllo=True
                            
                            try:
                                time_stamp=datetime.strptime(tmp[0],'%Y-%m')
                            except IndexError:
                                controllo=False
                                
                            if not controllo:
                                pass
                                
                            else:
                                #Elimino gli spazi \n
                                tmp[-1]=tmp[-1].strip()
    
                                if time is None:
                                    time.append((time_stamp))
                                else:
                                    for element in time:
                                        if time_stamp==element:
                                            raise ExamException('Il time stamp {} è un doppio. '.format(time_stamp))
                                        elif time_stamp< element:
                                            raise ExamException('Le date non sono ordinate')
                                    time.append(time_stamp)
                                            
                                #Creo la mia lista di liste
                               
                                data.append(tmp)         

        file.close()

        return(data)

time_series_file=CSVTimeSeriesFile(name='data.csv')
time_series=time_series_file.get_data()

# lista con i mesi dell'anno
mesi=['gennaio','febbraio','marzo','aprile','maggio','giugno','luglio','agosto','settembre','ottobre','novembre','dicembre']


#=========================================================#
#Definisco la funzione 'detect_similar_monthly_variations'#
#=========================================================#


def detect_similar_monthly_variations(time_series, years):
    
#==============================#
#Controllo input della funzione#
#==============================#
    
    # Controllo di time_series
    if not isinstance(time_series,list):
        raise ExamException('L input della funzione deve essere una lista')
        
    for i,lista in enumerate(time_series):
        if not isinstance(lista,list):
            raise ExamException('L elemento all indice {} non è una lista. Elemento: {}'.format(i,lista))
            
    # Controllo di years                       
    if not isinstance(years,list):
        raise ExamException('L input della funzione deve essere una lista')
    
    if len(years)!=2:
        raise ExamException('La lista contenente gli anni da confrontare deve essere di due elementi')
        
    if not isinstance(years[0],int):
        # Provo a convertire years_0 in formato intero
        if type(years[0])==str:
            try:
                int(years[1])
                
            except Exception as e:
                print(e)
        else:         
            raise ExamException('Gli anni devono essere di tipo intero')
            
    if not isinstance(years[1],int):
        # Provo a convertire years_1 in formato intero
        if type(years[1])==str:
            try:
                int(years[1])
            except Exception as e:
                print(e)
        else:         
            raise ExamException('Gli anni devono essere di tipo intero')
        
    if years[0]<=0 or years[1]<=0:
            raise ExamException('Gli anni da valutare devono essere positivi')
       
    if years[1]-years[0]!=1:
        raise ExamException('Gli anni non sono consecutivi')
        
#================================================================# #Controllo che gli elementi di years appartengano a time_series  #
#================================================================#

    # Creo delle variabili flag per controllare l'appartenenza degli elementi di years
        
    check1=False
    check2=False
    
    for i,item in enumerate(time_series):
        
        
        sub_list=item[0].split('-')
        
        if int(sub_list[0])==years[0]:
            check1=True
            
            # Salvo la posizione del primo  elemento contenente years[0]
            posizione1=i
            
        if int(sub_list[0])==years[1]:
            check2=True
            
            # Salvo la posizione del primo elemento contenente years[1]
            posizione2=i
        
    if check1 and check2:
        # se entrambi gli anni appartengono a time_series 
        
#==============================================================#
#Creo due liste, per registrare il numero di oasseggeri nei due# 
#anni consecutivi                                              #
#==============================================================#
        
        passeggeri_0={}
        passeggeri_1={}
        
        
        for i,element in enumerate(time_series):
            
            # Controllo che sto considerando l'anno giusto
        
            sub_list=element[0].split('-')
            time_month=int(sub_list[1])
            time_year=int(sub_list[0])
            
            if i<posizione1 and i<posizione2:
                pass
                
            if i >= posizione1 and time_year==years[0]:
            
                    # Controllo che il valore dei passeggeri sia positivo e intero
                    if isinstance(element[1],int) and element[1]> 0:
                        passeggeri_0[mesi[time_month-1]]=element[1]
                        
                    if element[1] is None:
                        passeggeri_0[mesi[time_month-1]]=False
                        
                   

            if i>=posizione2 and time_year==years[1]:
            
                # Controllo che il valore dei passeggeri sia positivo e intero
                if isinstance(element[1],int) and element[1]> 0:
                        passeggeri_1[mesi[time_month-1]]=element[1]
                    
                if element[1] is None:
                    passeggeri_1[mesi[time_month-1]]=False
                        
                    


#=============================================================#
# Creo due liste e registro le differenze nei mesi consecutivi# 
#degli anni consecutivi                                       #
# Costruisco le liste delle variazioni,tenendo conto che non  #   
#possono essere negative                                      #
#=============================================================#



        
        diff_pass_0=[]
        diff_pass_1=[]
        result=[]
          

        
        for i in range(11):
            
            if mesi[i+1] in passeggeri_0 and mesi[i] in passeggeri_0:
               
                diff_pass_0.append(passeggeri_0[mesi[i+1]]-passeggeri_0[mesi[i]])
               
            else:
               diff_pass_0.append(False)
               
            if mesi[i+1] in passeggeri_1 and mesi[i] in passeggeri_1:
                diff_pass_1.append(passeggeri_1[mesi[i+1]]-passeggeri_1[mesi[i]])
                
            else:
                diff_pass_1.append(False)
           

            if diff_pass_1[i]==False or diff_pass_0[i]==False:
                differenza=False
            else:
                differenza=(diff_pass_1[i]-diff_pass_0[i])

           
             
            if differenza<=2 and differenza>=-2 :
                result.append(True)
            else:
                if differenza==False:
                    result.append(False)
                elif differenza>2 and differenza<-2:
                    result.append(False)
                    

            
        print(result)
        return(result)
         
        
    else:
        # Se uno dei due anni non appartiene a time_series
        raise ExamException('Controllo di appartenenza elementi di years fallito')


prova1=detect_similar_monthly_variations(time_series,[1949,1950])
#=============#
# Test driver #  
#=============#
