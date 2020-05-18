print("Programa para provar continue en bucles.")

texto=input("Introduce un texto: ")
letras=0
for i in texto:
    if i==" ":
        continue
    letras+=1
print("Escribiste: " + str(letras))