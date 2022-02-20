import unittest
from Es2 import CSVFile

file1=CSVFile('shampoo_sales.csv')
lista1=file1.get_data()
lista2=file1.get_data(1,37)


if sum(lista1)>sum(lista2):
    raise Exception('La somma di lista1 è maggiore di quella di lista2')

class TestCSVFile(unittest.TestCase):
    def test_getdata(self):
        self.assertEqual(sum(lista1),sum(lista2))
