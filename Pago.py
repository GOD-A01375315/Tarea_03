# encoding: UTF-8
# Genaro Ortiz Durán, A01375315
# Descripción: Diseño topd-down para encontrar el pago de un trabajador.

from math import *

#Calcula el pago normal de un trabajador multiplicando las horas normales por el pago por hora.
def pagoNormal(h, p):
    pN = (h * p)
    return pN

#Calcula el pago por horas extras. Se calcula multiplicando las horas por las horas extras, el resultado se multiplica por el 1.50 que equivale al 50% más que las horas normales. Para sacar el extra se suma las horas normlaes mas las horas normales por 1.50.
def pagoExtra(h, a):
    pe = h * a
    pe2 = (pe * 1.50)
    pE = pe + pe2
    return pE

def main():
    h = int(input("Teclea las horas normales trabajadas:"))
    a = int(input("Teclea las horas extras trabajadas:"))
    p = int(input("Teclea el pago por hora:"))
    print("pago normal:", "$", format(pagoNormal(h, p), ".2f"))
    print("pago extra:", "$", format(pagoExtra(h, a), ".2f"))
    pT=pagoNormal(h,p)+pagoExtra(h,a)
    print("Pago total:",pT)





main()
