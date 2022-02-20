class MovingAverage:
    
    def __init__(self,win): 
        
        # Lunghezza finestra
        self.win=win
        
        if type(self.win) != int:
            raise ExamException('BO')
            
        if self.win==None:
            raise ExamException('Indicare il valore della finestra')
        if(self.win==0):
            raise ExamException('La finestra non può valere 0')
            
        if self.win<0:
            raise ExamException('La finestra non può essere negativa')
                
        
    def compute(self,lista):
        if self.win>len(lista):
            raise ExamException('La finestra super la lunghezza della lista')
        # Controllo gli input
        if lista==None:
            raise ExamException('La lista non può essere vuota')
            return(0)
       
            
        if type(lista)!=list:
            raise ExamException('L input dato non è una lista')

        if self.win==1:
            return(lista)
            
        else:

            media=[]
    
            for number in range(len(lista)-1):
                
                    if(number+(self.win-1) > len(lista)-1):
                        break
                    else:    
                        i=0
                        somma=[]
                  
                        
                        
                        while  i<self.win: 
                        
                            somma.append(lista[number+i])
                            
                                
                            i+=1
                            
                        media.append(sum(somma)/self.win)
                
            return(media)
                
# Estendo la classe Exception         
class ExamException(Exception):
    pass

moving_average=MovingAverage(3)
result=moving_average.compute([3,6,9,12])

print(result)

    
            
            
        






