class Vehiculo():

    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ",self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelera: ", self.acelera, "\nFrena: ", self.frena)

class furgoneta(Vehiculo):
    
    def carga(self,carga):
        self.cargado=carga
        if self.cargado:
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"
    
class VElectricos():
    def __init__(self):
        self.autonomia=100
    def cargaEnergia(self):
        self.cargando=True

class Moto(Vehiculo):
    hcaballito=""

    def caballo(self):
        self.hcaballito="Voy haciendo el caballito"

    def estado(self):
        print("Marca: ",self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelera: ", self.acelera, "\nFrena: ", self.frena, "\nCaballito: ", self.hcaballito)
