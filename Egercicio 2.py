#Determina la solucion logica de una operacion

a = int(input("a -> "))
b = int(input("b -> "))

resultado_logico = ((3+5*8)<3 and (-6/3*4)+2<2) or (a>b)

print(resultado_logico)