nome = str(input('Informe seu nome completo: '))
dividido = nome.split()
print('No seu nome contem "Silva"?\n{}'.format('Silva' in dividido))