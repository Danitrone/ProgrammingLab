# Punto 1

# Definisco la funzione stampa che stampa il contenuto di una lista data in input

def stamp( Lista ):
 # Ciclo su ogni elemento della lista

    for item in Lista:
       # Stampo ogni elemento della lista

        print(item)
    
    

# Dichiaro le mia liste
Lista=range(10)

Listadiliste=[[2,3,4],[5,6,7]]

# Chiamo la funzione
print('Lista1')
stamp (Lista)   
print('Lista2')

try:
    stamp (Listadiliste)

except NameError:

    print('Rilevato errore di nome, ricontrollare prego')    

# Punto 2

def statistica ( Lista):
        flag=1
        
        for item in Lista:

            if(type(item)!=int):
                flag=0

             

        print('Dati "{}"'.format(Lista))
        # Trovo la somma
        if(flag==1):

            
            somma=0
            for element in Lista:
                somma=somma+element
            
            print('La somma vale:"{}"'.format(somma))

            # Trovo la media

            media=somma/len(Lista)

            print('La media vale "{}"'.format(media))
            
           # trovo il minimo

            min=Lista[0]
            
            for item in Lista:
                
                if(item <min):

                    min=Lista[i]

                
            
            print('Il minimo è "{}"'.format(min))

            # Trovo il massimo
            
            max=Lista[0]
            i=0
            for item in Lista:
                
                if(item >max):

                    max=item
                

            print('Il massimo è "{}"'.format(max))
     
        else:
             print('Siamo spiacenti la lista non è di tipo intero')


# Testo la funzione statistica

statistica(range(11))

statistica(range(23))

# Punto 3

def somma_vettoriale( Lista1, Lista2):
    print('Operazione di somma vettoriale')
    # Verifico che le due liste siano composte da numeri interi e basta

    flag=1
    for item in Lista1:

        if(type(item)!=int):
            flag=0
        
    if(flag==0):

        print('La lista1 non è una lista di interi')
    else:
        print('La lista1 è composta da interi')

    norma=1

    for item in Lista1:

        if(type(item)!=int):
            norma=0
        
    if(flag==0 and norma==0):

       print('La lista2 non è una lista di interi')
    else:
        print('La lista2 è composta da interi')
   # Verifico che le due liste abbiano la stessa lunghezza

    if(len(Lista1)==len(Lista2)):
        # Creo una lista dove collocare la somma delle altre due

        Listone=[]
        print('Le due liste hanno la stessa lunghezza')
        for item in Lista1:
            Listone.append(item)
        
        for item in Lista2:
            Listone.append(item)

           
        print('La lista data dalla somma è: "{}"'.format(Listone))
    else:
        print('Le due liste non hanno la stessa lunghezza')
        
# Chiamo  la funzione somma vettoriale

somma_vettoriale(range(9),range(9))

# the end