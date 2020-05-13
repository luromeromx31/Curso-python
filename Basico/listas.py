lista=["maria", "Luis","Ricardo", 0]

print(lista[:])

lista.append("Yamm")

print(lista[:])

lista.insert(3,"Pablo")

print(lista[:])

lista.extend(["Luis2","Ana2","Lucia2"])

print(lista[:])
#devielve el id del elemento en la lista
print(lista.index("Luis"))

#valida si un elemento se encuentra en la lista
print("Jose" in lista)

lista.remove("Luis")

print(lista[:])

lista.remove(0)

print(lista[:])

lista.pop()

print(lista[:])

lista2=["Perro","Gato","Pez"]

print(lista2[:])

lista3=lista+lista2

print(lista3[:])

lista4=lista2*3

print(lista4[:])