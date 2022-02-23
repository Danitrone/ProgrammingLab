# Imports:
from datetime import datetime as dt # Serve per controllare che la data sia effeetivamente una data

# ===================== #
#  Examexception class  #
# ===================== #
class ExamException(Exception):
    pass

# ========================= #
#  Csvtimeseriesfile class  #
# ========================= #
class CSVTimeSeriesFile():

    # =============== #
    #  Init function  #
    # =============== #
    def __init__(self, name):
        self.name = name

        # Controllo che il nome sia una stringa
        if not isinstance(name, str):
            raise ExamException('Errore: Il nome del file passato non è una stringa')

    # =================== #
    #  GET_DATA FUNCTION  #
    # =================== #
    def get_data(self):

        # Creo la lista che mi server per il futuro
        final_list = []

        # Pro ad aprire il file e leggerlo
        try:
            file = open(self.name, 'r')

        # Se non eseiste allora alzo una eccezione
        except Exception:
            raise ExamException('Errore: Il file non può essere aperto')

        # Itera tutto il file linea a linea
        for line in file:

            # Questa lista tiene data e numero di passeggeri per ogni iterazione
            elements_list = []

            # DIvido date e basseggeri
            list_element = line.split(',')

            # Controllo se sono alla prima linea allora la salto
            if list_element[0] != 'date':

                # L'elemento zero e la data  e quindi la salviamo nella variablile data
                date = list_element[0]

                # La data deve effettivamente essere una data quindi faccio un controllo:
                try:
                    date = dt.strptime(date, "%Y-%m")
                except Exception:
                    # Vuole dire che passiamo alla prossima intereazione
                    continue

                # Salvo la data
                date = list_element[0]

                # A questo punto controlliamo che il valoer dei passeggeri sai un numero intero, se non lo è salviamo zero
                try:
                    passengers = int(list_element[1])
                except IndexError:
                    passengers = 0

                # Se il numero e con la virgalo
                except ValueError:
                    continue # float

                if passengers < 0:
                    continue # negative

                # Adesso dobbiamo controllare se ci sono dei timestamp dublicati

                # Fare il controllo ha senso solo se la lista dei dati salvati ha almento 1 alemento
                if len(final_list) > 0:

                    # Iteriamo tutti gli elementi
                    for item in final_list:

                        # Salavo la data del precendente
                        prev_date = item[0]

                        # Controllo per i duplicati:
                        if prev_date == date:
                            raise ExamException('Erorre: timestamp "{}" è duplicata.'.format(date))

                    # Se non ci sono duplicati faccio un controllo per l'ordinoe 
                    prev_date == final_list[-1][0]

                    # Se l'elemento di prima e maggiore di un elemento di adesso allora alzo una eccezione
                    if prev_date > date:
                        raise ExamException('Erore: timestamp "{}" è nel ordine sbagliato.'.format(date))

                # Salviamo i valori nella nostra lista
                elements_list = [date, passengers]

                # Quindi lo aggiungiamo alla lista finale
                final_list.append(elements_list)

        # If the file is empty
        if not final_list:
            raise ExamException('Errore: il file è vuoto! ')

        # Ritorno la lista finale
        return  final_list

# =================================== #
#  DETECT SIMILAR MONTHLY DIFFERENCE  #
# =================================== #
def detect_similar_monthly_variations(time_series, years):

    # First of all, let's check that the list given is not empty or with missing values:
    if not years:
        raise ExamException('Errore : la lista degli anni è vuota')

    if len(years) != 2:
        raise ExamException('Errore: la lista degli anni passata ha meno di due anni')

    # Check if time_series is a list
    if not isinstance(time_series, list):
        raise ExamException('Errore: time_series non è una list of lists.')

    elif not isinstance(time_series[0], list):
        raise ExamException('Errore: time_series non è una lista di liste.')

    # Controllo che tutti gli anni siano effetivamente numero interi:
    if not isinstance(years[0], int) or not isinstance(years[1], int):
        raise ExamException('Errore gli anni passati non sono numeri interi')

    if years[0] == years[1]:
        raise ExamException('Errore: i due anni devone essere diversi ! ')

    # Il pirmo anno deve essere piu piccolo dell ultimo
    if years[0] > years[1]:
        raise ExamException('E R R O R: first year is higher than last year! ')

    # Controllo che il primo anno sia presente nella lista di liste timeseries
    if years[0] < int(time_series[0][0][:4]):
        raise ExamException('Erroe il primo anno non è presente nella lista')

    # First and last year can't be the same:

    if years[1] > int(time_series[-1][0][:4]):
        raise ExamException('Erroe: l\' anno finale non è presente nella lista ! ')

    # Devono essere consegutivi
    if years[1] != years[0] + 1:
        raise ExamException('E R R O R: first and last year are not consecutive! ')


    #### Spioega marco

    # Variables:
    dictionary = {}

    # Creating dictionary:

    for i in range(len(time_series)):
        # If the key is already present in dictionary, then append the value to the list of values - this is needed in case of duplicates
        if time_series[i][0] in dictionary:
            dictionary[time_series[i][0]].append(time_series[i][1])

        # If the key is not present in the dictionary then add the key-value pair
        else:
            dictionary[time_series[i][0]] = []
            dictionary[time_series[i][0]].append(time_series[i][1])

    # Creating a storage for the keys that are needed:
    keys = []

    # Storing years[0] value in another variable:
    storage_year = years[0]

    # Storing all needed keys in a separate list:
    while years[0] <= years[1]:

        # Running through the keys in the dictionary:
        for key in dictionary:
           
            # Taking just the first four digits (the year):
            key_year = key[:4]

            # This is needed to exit the for loop when it has processed every key for the current year:
            if int(key_year) > years[0]:
                break

            # Every key for the year gets stored in the previous created list:
            if int(key_year) == years[0]:
                keys.append(key)
                       
        # When the cycle is done processing a year, it increases so it can pass on to the next one:
        years[0] = years[0] + 1
       
    # Restoring years[0] to its initial value:
    years[0] = storage_year

    # Defining variables:
    final_list = []
    #keys = []

    # Now the monthly average difference will be calculated:

    # Defining variables:
    var = 0
    result = True
    for i in range(11):
       
        # Caclulating variation:
        try:
            var = (dictionary[keys[i + 1]][0] - dictionary[keys[i]][0]) - (dictionary[keys[(i + 1) + 12]][0] - dictionary[keys[i + 12]][0])

        except IndexError:
            result = False
           
        # If the absolute value of the variation is less or equal than 2, we append a True, else a False:
        if abs(var) <= 2:
            result = True
           
        else:
            result = False
       
        # Adding the average to the output list:
        final_list.append(result)

    # Final list must be 11 elements long:
    if len(final_list) == 11:
        # Returning the final result:
        return final_list

    else:
        raise ExamException('E R R O R: final list is not 11 elementsl long! ')

# ====== #
#  MAIN  #
# ====== #
time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
years = [1949, 1950]
print(time_series)
print(detect_similar_monthly_variations(time_series, years))


