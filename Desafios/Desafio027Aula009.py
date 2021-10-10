frase = str(input('Informe uma frase: ')).strip().lower()
print('Na sua frase contem {} a(s)\nA primeira vez que a letra "a" aparace na frase é na posição:{}\nA ultima vez que a'
      ' letra "a" aparece na frase é na posição:{}'.format(frase.count('a'), frase.find('a'),frase.rfind('a')))
