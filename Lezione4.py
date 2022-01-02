
# Definizione oggetto

class CSVFile ():
    
    # Inizializzazione

    def __init__(self,name):

        self.name=name
        
    # Indico la rappresentazione come stringa

    def __str__(self):

        return('CSVFile "{}"'.format(self.name))

    # Definisco il modulo dell'oggetto

    def get_data(self):
        # Inizalizzo la lista dove inserire le liste create

        Lista=[]
          
        # Apro il file che ho inidcato come oggetto 

        file=open(self.name)

        # Compio un ciclo for

        for line in file:
            # Splitto riga per riga in una lista e la colloco in Listino

            Listino=line.split(',')
            
            # Differenzio e elimino la riga indicativa

            if (Listino[0]!='Date'):

                # Aggiungo a Lista Listino, per ogni riga

                Lista.append(Listino)

       # Stampo Lista
       
        print (Lista)
        
       # Chiudo il file
       
        file.close()
        

# Dichiaro l'oggetto

csv=CSVFile('shampoo_sales.csv')

# Stampo il nome della list di liste

print(csv)

# Eseguo il modulo della'oggettp CSVFile

csv.get_data()