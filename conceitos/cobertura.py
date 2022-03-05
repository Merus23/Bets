#Aposta1
a  = float(input('Informe o valor investido na 1º aposta:'))
odd1 = float(input('Informe a odd da 1º aposta:'))
r1 = a * odd1

#Aposta2
b = float(input('Informe o valor investido na 2º aposta:'))
odd2 = float(input('Informe a odd da 2º aposta:'))
r2 = b * odd2

if((r1 >  a + b) and (r2 > a + b)):
    print('Ganho e ganho!!!')

elif((r1 <  a + b) and (r2 < a + b)):
    print('Minimizador de ganhos!')
