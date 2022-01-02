# Creo la classe automobile
class Automobile():
    # Chiamo il costruttore
    def __init__(self, casa_automo, modello, numero_posti,targa):
        
        self.casa_automo=casa_automo
        self.modello= modello
        self.numero_posti=numero_posti
        self.targa=targa

    # Uso il metodo interno str èper stampare i dati dell'automobile
    def __str__(self):

        print('Casa: "{}"'.format(self.casa_automo))
        print('Modello: "{}"'.format(self.modello))
        print('Numero di posti: "{}"'.format(self.numero_posti))
        print('targa: "{}"'.format(self.targa))   
    # definisco la funzione parla per stampare broom broom
    def parla(self):
        print('Broom broom')

    # definisco la funzione confronta prende in input l'oggetto stesso e un'altro oggetto sempre della stessa classe.
    def confronta(self,auto2):
        if(
            self.casa_automo==auto2.casa_automo
            and self.modello==auto2.modello 
            and self.numero_posti==auto2.numero_posti):

            print('Auto1 e Auto2 sono uguali')

        else:

            print('Auto1 e Auto2 Non sono uguali')


class Transformer(Automobile):

    
    
    def __init__(self,nome,generazione,grado,reparto):
        self.nome=nome
        self.generazione=generazione
        self.grado=grado
        self.reparto=reparto

    def scheda_militare(self):
        
        print('Generazione: "{}"'.format(self.generazione))
        print('Grado: "{}"'.format(self.grado))
        print('Reparto: "{}"'.format(self.reparto))



# Istanzio gli oggetti
auto1=Automobile('volvo','x4',3,475785)

auto2=Automobile('volvo','x4',3,447836)

# gestisco gli errori
try:
    print('Auto 1')
    print(auto1) 
except TypeError:
    pass    
try:
    print('Auto 2')
    print(auto2)       
    
except TypeError:
    pass

# Chiamo le funzioni

auto1.confronta(auto2)

# Istanzio il mio trasnsformer
Babolbii=Transformer('Babolbii','quinta',2,'soldato')
print(Babolbii.nome)
Babolbii.scheda_militare()