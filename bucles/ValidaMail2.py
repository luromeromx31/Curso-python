print("Programa para validar Mail v2")
val=0
punto=0
arr=0

mimail=input("Introduce tu mail: ")

for i in range(len(mimail)):
    if mimail[i]=="@":
        arr=arr+1
    if mimail[i]==".":
        punto=punto+1

if (arr==1 and punto>=1):
    print("El mail es correcto")
else:
    print("El mail es incorrecto")