from matplotlib import pyplot
import numpy as np

from Es2 import CSVFile



class Model:
    
    def fit(self):
        raise NotImplemented('Il modulo non è implementato')
        
    def predict(self):
            raise NotImplemented('Il modulo non è implementato')


class IncrementModel(Model):
    
    # Creo una funzione per determinare data una lista di dati         l'incremento medio
    def get_increment(self,data):
  
        tmp=None
        Val=[]
        for element in data:
            if tmp!=None:
                Val.append(element-tmp)
                
            tmp=element
            
        increment=sum(Val)/(len(data)-1)
        return(increment)
        
    
    def predict(self,data):
        
        predict_data=data[-1]+self.get_increment(data)
        
        return(predict_data)

    
class FitIncrementModel(IncrementModel):
 
    def fit(self,fit_data):
        
        self.global_avg_increment=super().get_increment(fit_data)
        

    def predict(self,data):

        predict_data=super().get_increment(data)
        
        return(data[-1]+(predict_data+self.global_avg_increment)/2)
        
       
# Lista con i valori di shampoo_sales
shampoo=[266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3, 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9]

# Numero di mesi che voglio valutare(Partendo dall'ultimo)
eval_month=12

# Lista con i mesi da usare per il fit fittare
cut_month=shampoo[ 0:len(shampoo)-eval_month ]

print('Lista valori per il fit\n')
print(len(shampoo))

                # modello senza fit #

prediction=IncrementModel()

error=0

for i in range(eval_month):
    
    # A ogni ciclo creo una lista di 3 elementi con la quale fare la predict
    data=shampoo[len(cut_month)+i-4:len(cut_month)+i]
    data_predict=prediction.predict(data)
    
    error += abs(data_predict-shampoo[len(cut_month)+i])

avarage_error=error/(eval_month+1)
    
    
print(avarage_error)

        


        
        
        
        
        
        
    
    
    
        
    




        

        
        
        
        
        
        
    
    
                
                
            
            
            
    
        
    