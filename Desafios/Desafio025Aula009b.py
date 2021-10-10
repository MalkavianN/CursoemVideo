cidade = str(input('Informe o nome da sua cidade: ')).strip().title()
cidadedividida = cidade.split()
if 'Santo' == cidadedividida[0]:
    print('No nome da sua cidade contem Santo no primeiro nome')
else:
    print('No nome da sua cidade não contem Santo no primeiro nome')

