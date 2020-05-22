class Persona():
    def __init__(self, nombre, edad, residencia):
        self.nombre=nombre
        self.edad=edad
        self.residencia=residencia
    
    def descripcion(self):
        print("Nombre: ", self.nombre, " Edad: ", self.edad, " Residencia: ", self.residencia)

class Empleado(Persona):
    def __init__(self, nombre, edad, residencia, salario, antiguedad):
        #Llamamos constructor de la clase padre
        super().__init__(nombre, edad, residencia)
        self.salario=salario
        self.antiguedad=antiguedad
    def descripcion(self):
        #Ejecutamos el metodo de la clase padre.
        super().descripcion()
        print("Salario: ", self.salario, " Antiguedad: ", self.antiguedad)

Manuel=Persona("Manuel", 55, "España")
Antonio=Empleado("Antonio", 55, "España", 1500, 20)

Antonio.descripcion()

#Para obtener la clase.

print(isinstance(Antonio, Persona ))
print(isinstance(Manuel, Empleado ))