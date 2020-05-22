print("Primer programa de POO.")

class Coche():
    #Creo metodo constructor.
    def __init__(self):
        #Encapsulo variable.
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        enmarcha=False
    
    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos

        if (self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta detenido"

    def estado(self):
        print(("El coche tiene: ", self.__ruedas, " ruedas, un ancho de: ", self.__anchoChasis, " y un largo de: ", self.__largoChasis))


print("---------------------- Se crea primera instancia del coche ------------------------")

miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("---------------------- Se crea segunda instancia del coche ------------------------")

miCoche2=Coche()

#Los siguientes print dan error, porque las variables fueron encapsuladas y solo son alcanzables desde dentro de la clase
#print("El largo de mi coche es: ",miCoche2.__largoChasis)
#print("El coche tiene ",miCoche2.__ruedas, " ruedas")
print(miCoche2.arrancar(False))
miCoche2.estado()