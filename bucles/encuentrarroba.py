print("Programa para encontrar @.")
correo=input("Introduce un correo: ")
arroba=False

for i in correo:
    if i=="@":
        arroba=True
        break
else:
    arroba=False

if arroba:
    print("El texto tiene una @.")
else:
    print("El texto NO tiene @.")