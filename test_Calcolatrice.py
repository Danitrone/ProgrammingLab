import unittest
from Calcolatrice import Calcolatrice

class TestCalcolatrice(unittest.TestCase):
    def test_calcolatrice(self):
        self.assertEqual(Calcolatrice.somma(5,5),10)
        self.assertEqual(Calcolatrice.prodotto(4,3),12)
        self.assertEqual(Calcolatrice.sottrazione(7,3),4)
        self.assertEqual(Calcolatrice.divisione(81,9),9)
        self.assertEqual(Calcolatrice.potenza(2,3),8)
        self.assertEqual(Calcolatrice.radice(4),2)
