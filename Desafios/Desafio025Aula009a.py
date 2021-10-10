cidade = str(input('Informe o nome da sua cidade: ')).strip().title()
cidadedividida = cidade.split()
print('O nome da sua cidade contem santo no primeiro nome:\n{}'.format('Santo' == cidadedividida[0]))
