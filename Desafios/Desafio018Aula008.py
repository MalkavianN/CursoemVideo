from math import hypot
cato = float(input('Informe o comprimento do cateto oposto: '))
cata = float(input('Informe o comprimento do cateto adjacente '))
hyp = hypot(cato, cata)
print('O valor da hypotenusa é:{}'.format(hyp))
