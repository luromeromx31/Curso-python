print("Programa para mostrar el polimorfismo")

class Coche():
    
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():
    
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():
    
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

def desplazamiento(vehiculo):
    vehiculo.desplazamiento()


miVehiculo=Camion()

desplazamiento(miVehiculo)