#Las tuplas se escriben entre parentesis

tupla=("luis",5,1.34,5,123456)
print(tupla[1])
print(tupla[:])

lista=list(tupla)

print(lista[:])

lista2=["Ricardo",1,5.5,False]
tupla2=tuple(lista2)
print(lista2[:])
print(tupla2[:])

print("luis" in tupla2)
#Busca cuantas veces se encuentra el numero 5 en la tupla
print(tupla.count(5))
#Obtener numero de elementos de tupla
print(len(tupla))
#tupla unitaria
tupla3=("Unitaria",)
print(len(tupla3))

nombret, gradot, calt, aprot=tupla2
nombrel, gradol, call, aprol=lista2


print(nombret)
print(gradol)
