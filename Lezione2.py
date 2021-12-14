
# Prova 1

    a = range( 10 )

    b = sum( a )

    print ( " Prova 1: {} \n ". format ( b ) )

# Esercizio vero
        
    def sum_list ( lista ):
        b = 0

        for item in lista:
            b = b + item

        print ( b )


    sum_list( lista = range ( 10 ) )