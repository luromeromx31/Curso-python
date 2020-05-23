print("Programa para evaluar un mail.")

mail=input("Introduce tu mail: ")

arroba=mail.count('@')

if (arroba!=1 or mail.rfind('@')==(len(mail)-1) or mail.find('@')==0):
    print("El correo es incorrecto.")
else:
    print("El correo es correcto:")