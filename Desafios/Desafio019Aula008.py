from math import cos, sin, tan, radians
ang = float(input('Informe o valor do ângulo a ser calculado: '))
co = cos(radians(ang))
sen = sin(radians(ang))
tang = tan(radians(ang))
print('O ângulo de {} tem o cosseno de: {:.2f}\nO ângulo de {} tem o seno de: {:.2f}\nO ângulo de {} tem a tangente de:'
      ' {:.2f}'.format(ang, co, ang, sen, ang, tang))
