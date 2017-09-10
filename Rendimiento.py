# encoding: UTF-8
# Genaro Ortiz Durán, A01375315
# Descripción: Diseño topd-down para encontrar el rendimiento de un auto.

#Calcula el rendimiento en km/l dividiendo los kilometros entre la gasolina.
def rendimiento(kilometros,gasolina):
    r=(kilometros/gasolina)
    return r
#Para convertir los km/l a mi/ga se divide los (km entre km1)=M y la (gasolina se multiplica por g)=G.Por último se divide M entre G.
def conversion(kilometros,gasolina):
    km1=1.609344
    g=	0.264172051
    M=kilometros/km1
    G=gasolina*g
    c=(M/G)
    return c
#La función divide los kilometros entre la gasolina, el resultado se utiliza como divisor de la distancia.
def litros(kilometros,gasolina,distancia):
    a=(kilometros/gasolina)
    d=(distancia/a)
    return d





def main():
    kilometros=int(input("Teclea el número de kilometros recorridos:"))
    gasolina=int(input("Teclea el número de litros de gasolina usados:"))
    print("Si recorres",kilometros,"con",gasolina,"litros de gasolina","el rendimiento es:",format(rendimiento(kilometros,gasolina),".2f"),"km/l",format(conversion(kilometros,gasolina),".2f"),"mi/gal")
    distancia = int(input("¿Cuantos kilometros vas a recorrer:"))
    print("Para recorrer",distancia,"km","necesitas",format(litros(kilometros,gasolina,distancia),".2f"),"litros de gasolina")
main()
