'''
Created on 6/5/2015

@author: Susana Rodriguez M    11-10893
@author: Mathieu De Valery F.    10-10193
@author: Gabriel Iglesias M.    11-10476

'''
import unittest
from billetera import *


class TestBilletera(unittest.TestCase):

    #Casos de prueba de existencia
    def testInit(self):
        billeteraElectronica = billetera(1110893, "Susana", "Rodriguez",24287498,12345,1912)
        
    #Casos de prueba de existencia
    def testSaldoExiste(self):
        billeteraElectronica2 = billetera(1110476, "Gabriel", "iglesias",20193839,90876,1401)
        billeteraElectronica2.consultarSaldo() 
        
    #Caso de prueba interior del metodo consultar saldo    
    def testSaldo(self):
        billeteraElectronica3 = billetera(1010193, "Mathieu", "De Valery",20674668,0,1010)
        self.assertEqual(billeteraElectronica3.consultarSaldo(), 0.0)        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()