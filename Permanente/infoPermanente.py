import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre de: ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:
    personas=[]

    def __init__(self):
        listaDePersonas=open("Permanente/ficheroExterno", "ab+")
        listaDePersonas.seek(0)

        try:
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(personas)))
        except:
            print("El fichero esta vacio.")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregaPersona(self, p):
        self.personas.append(p)
        self.guardaPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardaPersonasEnFicheroExterno(self):
        listaDePersonas=open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostarInfoFicheroExterno(self):
        print("La información del fichero externo es: ")
        for p in self.personas:
            print(p)

miLista=ListaPersonas()
persona=Persona("Sandra", "Femenino", 29)
miLista.agregaPersona(persona)

persona=Persona("Antonio", "Masculino", 9)
miLista.agregaPersona(persona)
miLista.mostarInfoFicheroExterno()
#p=Persona("Ana", "Femenino", 25)
#miLista.agregaPersona(p)
