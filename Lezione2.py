
# Prova 1 con sum

    a = range( 10 )

    b = sum( a )

    print ( " Prova 1: {} \n ". format ( b ) )

# Esercizio: scrivere una funzione per la somma di elementi di una lista
        
    def sum_list ( lista ):
        
        b = 0

        for item in lista:

            b = b + item

        print ( b )


    sum_list( lista = range ( 10 ) )