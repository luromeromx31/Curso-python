# --------------- Funcion normal

def area_triangulo(base, altura):
    return(base*altura)/2

triangulo=area_triangulo(5,2)

print(triangulo)

#------------------ Funcion Lambda numericas

area_triangulo2=lambda base2,altura2:(base2*altura2)/2

print(area_triangulo2(5,7))


al_cubo=lambda numero:(numero**3)

print(al_cubo(3))

#------------------- Funcion lambda formato texto

destacar=lambda comision:"!${} !".format(comision)

print(destacar(400))
