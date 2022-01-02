
#Inizializzo una lista vuota dove inserire i valori

Lista=[]

# Apro il file

file = open('shampoo_sales.csv','r')

#Utilizzo un ciclo for

for line in file:
    
    #Splitto ogni stringa di linea

    Lista1 = line.split (',')
    
    #Differenzio i due elementi della lista

    if (Lista1[0] != 'Date'):

        Data=Lista1[0]

        Values=Lista1[1]
         
        Lista.append(float(Values))
    
# Stampo lista prima della somma

print(Lista)

# Stampo la somma degli elementi della lista

print(sum(Lista))


file.close()




