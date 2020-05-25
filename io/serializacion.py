import pickle

lista_nombres=["pedro", "Maria", "Isabel"]

ficheroBinario=open("io/listaNombres", "wb")

pickle.dump(lista_nombres, ficheroBinario)

ficheroBinario.close()

del (ficheroBinario)