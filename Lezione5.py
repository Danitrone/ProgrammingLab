
# Definisco l'oggetto

class CSVFile():
    # Utilizzo il costruttore per inizializzare l'oggetto

    def __init__( self, name):

        self.name=name
        
        self.can_read=true
       
    
        try :
            file=open(self.name,'r')
            file.readline()
        except Exception as e:
            can_read=false
            print('Errore trovato durante l apertura del file: "{}"'.format(e))

    # Definisco una funzione per leggere e aprire il contenuto del file

    def get_data (self):
       
        if not can_read:
            print('File non leggibile')
            return(none)
        else:
            
            Lista=[]
            # Apro il file nella modalità selezionata
            file=open(self.name,self.modalita)
          
            for line in file:
                # Splitto ogni riga alla virgola collocandola prima nella lista Listino
                Listino=line.split(',')
                # Con la funzione strip elimino gli spazi a fine di ogni riga

                Listino[-1]=Listino[-1].strip()
                # Aggiungo Listino a Lista eccetto la prima riga
                if(Listino[0]!='Date'):
                    Lista.append(Listino)

            print('Title:"{}"'. format(self.name))

            print(Lista)
            return (Lista)
            file.close()


class NumericalCSVFile ( CSVFile ):
    # Chiamo il costruttore della classe super
    def __init__(self,name):
        self.name=name
        
    def Enumera (self):
        # Apriamo il file
        file=open(self.name)

        # Creo una lista vuota
        numeri=[]

        # uso un ciclo for
        for line in file:
            lista=line.split(',')
            lista[-1]=lista[-1].strip()
            # Differenzio il primo caso 
            if lista[0] == 'Date':
                numeri.append(lista[1])
            else:
                # Gestisco gli eventuali errori di valore
                try:
                    numeri.append(float(line))

                except ValueError:
                    print('Rilevato errore:"{}". Ricontrollare il file'.format(ValueError))
                    
        
        file.close
        return(numeri)



file2=NumericalCSVFile('shampoo_sales (w error).csv')

print(file2.Enumera())