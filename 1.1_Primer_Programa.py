def sumar(a, b):
    suma  = a + b 
    return suma
numero_1 = int(input('ingrese el primer numero: ') )
numero_2 = int(input('ingrese el segundo numero: '))

resultado = sumar(numero_1, numero_2)

print('la suma de {} y {} es igual a {}.'.format(numero_2 , numero_2, resultado ))