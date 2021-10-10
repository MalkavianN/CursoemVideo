import random
nome1 = input('Informe o primeiro nome: ')
nome2 = input('Informe o segundo nome: ')
nome3 = input('Informe o terceiro nome: ')
nome4 = input('Informe o quarto nome: ')
nomesorteado = nome1, nome2, nome3, nome4
sorteado = random.sample(nomesorteado, 1)
print('O sorteado foi: {}'.format(sorteado))
