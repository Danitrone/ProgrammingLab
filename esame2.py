
# Estendo la classe Exception
class ExamException(Exception):
    pass

# Creo la classe Diff
class Diff:
    
    # Chiamo il costruttore
    def __init__(self,ratio=1):
        
      # Considero il caso di ratio non indicato
            self.ratio=ratio
        
         
            if not isinstance(self.ratio,int):
                    raise ExamException(' ratio non è di tipo numerico ed è impossibile convertirlo')
                
            if self.ratio==0:
                raise ExamException('Impossibile dividere per 0')
                
            if self.ratio < 0 :
                raise ExamException('Ratio deve essere positivo')
            
        
            
    # Definisco il modulo compute per calcolare le differenze degli elementi della lista
            # -imput: Lista di valori numerici
            # -output: Lista delle differenze dei valori
        
    def compute(self,lista):
        
        if not isinstance(lista,list):
            raise ExamException('Gli elementi non sono in una lista')
        if len(lista)<2:
            raise ExamException('Lista con meno di due elementi!')
        # Check elementi della lista
        for element in lista:
            
            if type(element)!=int and type(element)!=float:
                raise ExamException('L elemento {} della lista non è in formato numerico'.format(element))
                
               
        list_diff=[]
        
        for i,element in enumerate(lista):
            
            if i==0:
                pass
                
            if i>0:
                list_diff.append((abs(element-lista[i-1])/self.ratio))

        return(list_diff)


diff=Diff()
result=diff.compute([2,4,8,16])

print(result)
            
        
    
    