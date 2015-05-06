'''
Created on 6/5/2015

@author: susyroma
'''
class billetera:
    '''
    Clase de la billetera electronica
    '''

     
    def __init__(self, identificador, nombres, apellidos, CI, saldo, PIN):
        '''
        Constructor
        '''
        self.identificador = identificador
        self.nombres = nombres
        self.apellidos = apellidos
        self.ci = CI
        self.saldo = 0.0
        self.pin = PIN
        
    def consultarSaldo(self):
        return self.saldo