#encoding: UTF-8
#Genaro Ortiz Durán, A01375315
#Descripción: Diseño topd-down para encontrar el diámetro, volumen y área de una esfera.

from math import*

#Multiplica el radio por dos para saber el diámetro.
def diametro(radio):
    d=(radio*2)
    return d
#Multiplica el radio al cubo por pi y por cuatro tercios para sacar el volumen.
def volumen(radio):
    V=((4/3)*pi)*(radio**3)
    return V

#Multiplica por cuatro a pi y al radio al cuadrado para sacar el área.
def area(radio):
    A=4*(pi*(radio**2))
    return A

def main():
  radio = int(input("Escribe el radio de la esfera:"))
  print("Diámetro:",diametro(radio))
  print("Volumen", format (volumen(radio), ".2f"))
  print("Área:", format(area(radio), ".2f"))
main()