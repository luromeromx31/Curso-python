diccionario={"Alemania":"Berlin","Francia":"Paris","España":"Madrid","Reino Unido":"Londres"}

print(diccionario["Francia"])
print(diccionario)

diccionario["México"]="Ciudad de México"

print(diccionario)

diccionario["México"]="CDMX"

print(diccionario)

del diccionario["Alemania"]

print(diccionario)

diccionario["CP"]=3020

print(diccionario)

tupla=["Francia","España","Alemania"]

diccionario2={tupla[0]:"Paris",tupla[1]:"Madrid",tupla[2]:"Berlin"}

print(diccionario2)

print(diccionario2["Francia"])

#tupla dentro de un diccionario
diccionario3={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":[1991,1992,1993,1996,1997,1998]}
print(diccionario3)

#Diccionario dentro de una tupla dentro de una Diccionario
diccionario3={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}

print(diccionario3["Anillos"])

print(diccionario3.keys())

print(diccionario3.values())

print(len(diccionario3))