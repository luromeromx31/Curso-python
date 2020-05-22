print("Primer programa de POO.")

class Coche():
    #Creo metodo constructor.
    def __init__(self):
        #Encapsulo variable.
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False
        self.color="rojo"
    
    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        print("Arrancando el coche.")
        if self.__enmarcha:
            chequeo=self.__chequeo_interno()
        
        if (self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif self.__enmarcha and chequeo==False:
            return "Error en el chequeo, no se puede arrancar"
        else:
            return "El coche esta detenido"

    def estado(self):
        print(("El coche tiene: ", self.__ruedas, " ruedas, un ancho de: ", self.__anchoChasis, " y un largo de: ", self.__largoChasis))

    #
    def __chequeo_interno(self):
        print("Realizando Chequeo Interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

print("---------------------- Se crea primera instancia del coche ------------------------")

miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("---------------------- Se crea segunda instancia del coche ------------------------")

miCoche2=Coche()
#print(miCoche2.arrancar(False))
miCoche2.estado()