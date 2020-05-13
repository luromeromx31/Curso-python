print("Programa para evaluar becas")

salario=int(input("Introduce el salario: "))
hermanos=int(input("Introduce el numero de hermanos: "))
distancia=int(input("Introduce la distancia en KM: "))

def becas(becas,hermanos,distancia):
    if salario<20000 or hermanos>2 and distancia>3:
        beca=True
    else:
        beca=False
    return beca

beca=becas(salario,hermanos,distancia)

if beca is True:
    print("Calificas para la beca")
else:
    print("No calificas para la beca")
        
        
