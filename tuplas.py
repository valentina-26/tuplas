nombre=input("ingresa el nombre: ")
edad=input("ingrese su edad: ")
altura=input("ingrese su altura: ")
direccion=input("ingrese su direccion: ")

informacion=tuple((nombre,edad,altura,direccion))

print(informacion)

experien=input("cual es su experiencia laboral?: ")
añosE=input("cuantos años tiene d experiencia: ")
referen=input("cuales son sus refencias: ")

experiencia=tuple((experien, añosE, referen))

print(experiencia)

cuantos=input("con cuantos cursos cuenta?: ")
tipo=input("con que cursos cuenta?: ")

cursos=tuple((cuantos, tipo))

print(cursos)