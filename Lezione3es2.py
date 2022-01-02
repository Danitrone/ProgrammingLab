# Inizializzo le mie liste dove inserire i valori

Lista=[]

Listino=[]

# Apro il file

file=open('shampoo_sales.csv','r')

# Scopo dell'esercizio è trasformare il file in una lsta di liste

# Eseguo il ciclo per ogni riga

for line in file:

    # Splitto la riga e creo una lista in Listino
    
    Listino=line.split(',')
    
    # Differenzio ed elimino la riga inidcativa

    if (Listino[0]!='Date')

         # Aggiungo a Lista a ogni ciclo Listino

        Lista.append(Listino)

# Stampo Lista

print(Lista)

# Chiudo il file

file.close()