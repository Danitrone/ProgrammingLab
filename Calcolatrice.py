from math import sqrt


class Calcolatrice:
    
    def somma(membro1,membro2):

        if type(membro1)!= int and type(membro1)!= float:

                raise Exception('Il primo membro ha un tipo  errato')
                

        if type(membro2)!= int and type(membro2)!= float:

                raise Exception('Il secondo membro ha un tipo  errato')
                


        return(membro1+membro2)

    def sottrazione(membro1, membro2):

        if type(membro1)!= int and type(membro1)!= float:
                raise Exception('Il primo membro ha un tipo  errato')
                

        if type(membro2)!= int and type(membro2)!= float:

            try:
                float(membro2)
                
            except Exception:
                raise Exception('Il secondo membro ha un tipo  errato')
                
        return(membro1-membro2)
    
    def prodotto(membro1,membro2):

        if type(membro1)!= int and type(membro1)!= float:

                raise Exception('Il primo membro ha un tipo                         errato')
                

        if type(membro2)!= int and type(membro2)!= float:
                raise Exception('Il secondo membro ha un tipo                                         errato')
                
 
        return(membro1*membro2)

    def divisione(membro1,membro2):

        if membro2==0:
            raise Exception('Impossibile dividere per 0')
            

        if type(membro1)!= int and type(membro1)!= float:
                raise Exception('Il primo membro ha un tipo  errato')
                

        if type(membro2)!= int and type(membro2)!= float:
                raise Exception('Il secondo membro ha un tipo  errato')
                

        return(membro1/membro2)
    
    def potenza(base,esponente):

        if type(esponente)!= int:
                raise Exception('L esponente non è di tipo intero')
                

        if type(base)!= int:
                raise Exception('La base non è di tipo intero')
                
        
        return(base**esponente)

    def radice(membro1):
            
            if type(membro1)!= int and type(membro1)!= float:
                    raise Exception('Il primo membro ha un tipo  errato')
                
            if membro1 <= 0:
                raise Exception('L argomento della radice non può essere minore o uguale a 0')
                
            return(sqrt(membro1))
            
        
   

        




        

