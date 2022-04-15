#OPERADORES LOGICOS

#******************************************
a = 10
b = 12
c = 13
d = 10
print(((a>b)or(a<c))and((a==c)or(a>=b)))
#***************************************

x = 10
y = 15
z = 20
#resultado = ((a<b) and (b<c))
#resultado = ((a>b) and (b<c))
#resultado = ((a>b) or (b<c))
resultado = not((a>b) or (b<c))
print(resultado)