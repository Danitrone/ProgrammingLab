import random 

class Automa:

    def __init__(self):

        self.biancheria=None
        self.calzini=None
        self.maglia=None
        self.pantaloni=None
        self.calzature=None
    
    def biancheria(self):

        probability=random.randint(0,1)

        if probability==0:
            self.biancheria=None
            return(0)

        if probability==1:
            self.biancheria=True
            return(1)
    
    def calzini(self):

        probability=random.randint(0,1)

        if probability==0:
            self.calzini=None
            return(0)

        if probability==1:
            self.calzini=True
            return(1)
    
    def maglia(self):

        probability=random.randint(0,1)

        if probability==0:
            self.maglia=None
            return(0)

        if probability==1:
            self.maglia=True
            return(1)
    
    def pantaloni(self):

        probability=random.randint(0,1)

        if probability==0:
            self.pantaloni=None
            return(0)

        if probability==1:
            self.panta:loni=True
            return(1)
    
    def calzini(self):

        probability=random.randint(0,1)

        if probability==0:
            self.calzini=None
            return(0)

        if probability==1:
            self.calzini=True
            return(1)

        
        
        
def esegui(Automa,capo):

    if capo=='biancheria':
        result=Automa.biancheria
        return(result)
    
    if capo=='calzini':
        result=Automa.calzini
        return(result)

    if capo=='maglia':
        result=Automa.maglia
        return(result)

    if capo=='pantaloni':
        result=Automa.pantaloni
        return(result)

    if capo=='calzature':
        result=Automa.calzatura
        return(result)

        
            
capo=['biancheria','calzini','maglia','pantaloni','calzature']

Vestito=True
Vestiti_visti=[]

while(Vestito):

    capo_esame=random.choice(capo)

    if capo_esame=='biancheria' and Vestiti_visti is not None:
        pass

    else:    
        if capo_esame not in Vestiti_visti:

            analisi=esegui(Automa, capo_esame)
            
            if analisi==0:
                    raise Exception('L automa non è riuscito a indossare la biancheria')
                    break
            else: 
                    Vestiti_visti.append(capo_esame)

        else:
            pass

    if capo_esame=='calzini' and biancheria  not in Vestiti_visti:
        pass

    else:
        if capo_esame not in Vestiti_visti:

            analisi=esegui(Automa, capo_esame)

             
            if analisi==0:
                    raise Exception('L automa non è riuscito a indossare i calzini')
                    break
            else: 
                    Vestiti_visti.append(capo_esame)


        
        
    if capo_esame=='maglia' and 'calzini'  not in Vestiti_visti:
        pass

    else:
         if capo_esame not in Vestiti_visti:

            analisi=esegui(Automa, capo_esame)

         
            if analisi==0:
                    raise Exception('L automa non è riuscito a indossare la maglia')
                    break
            else: 
                    Vestiti_visti.append(capo_esame)


    
    if capo_esame=='pantaloni' and 'calzini'  not in Vestiti_visti:
        pass

    else:
         if capo_esame not in Vestiti_visti:

            analisi=esegui(Automa, capo_esame)
           
            if analisi==0:
                    raise Exception('L automa non è riuscito a indossare i pantaloni')
                    break
            else: 
                    Vestiti_visti.append(capo_esame)

        
    
    if capo_esame=='calzature' and 'pantaloni'  not in Vestiti_visti:
        pass

    else:
         if capo_esame not in Vestiti_visti:

            analisi=esegui(Automa, capo_esame)
            
            if analisi==0:
                raise Exception('L automa non è riuscito a indossare le calzature')
                break
            else: 
                Vestiti_visti.append(capo_esame)


      
    
    if Vestiti_visti==capo:
            Vestito=False
    
if Vestiti_visti==capo:
    print('L automa si è vestito correttamente')
else:
    print('Lautoma non è riuscito a vestirsi')

    


    







    