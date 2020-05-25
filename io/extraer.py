import pickle

fichero=open("io/listaNombres", "rb")

lista=pickle.load(fichero)

print(lista)