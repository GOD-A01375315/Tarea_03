#encoding: UTF-8
#Genaro Ortiz Durán, A01375315
#Descripción: Diseño topd-down para encontrar precios de boletos.
A=400
B=250
C=135

#Calcula el costo total de los boletos por medio de las sumas de la cantidad pedida de asientos por categoría por su precio.
def calcularPago(a,b,c):
    totalPago=(A*a+(B*b)+(C*c))
    return totalPago

def main():
    boletosA = int(input("¿Cuántos boletos quieres en clase A:"))
    boletosB = int(input("¿Cuántos boletos quieres en clase B:"))
    boletosC = int(input("¿Cuántos boletos quieres en clase C:"))
    pT=calcularPago(boletosA,boletosB,boletosC)
    print("El costo total es:","$", format (pT, ".2f"))

main()