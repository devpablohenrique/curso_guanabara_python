valor = float(input('Informe um valor em metros: '))
centi = valor * 100
m = valor * 1000
print('O valor informado foi o {}m, convertido em centimetros é igual a {:.0f}cm e convertido em milimetros é igual a {:.0f}mm'.format(valor, centi, m))
