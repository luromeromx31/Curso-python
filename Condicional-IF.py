print("Programa de evaluacion de notas de alumnos")

nota_alumno=input("Introduce tu calificación: ")

def evaluacion(nota):
    
    if nota<5:
        valoracion="reprovado"
    else:
        valoracion="aprovado"
    return valoracion
    
print(evaluacion(int(nota_alumno)))

