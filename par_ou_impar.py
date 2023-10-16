#Projeto Par ou Ímpar

#Apresentação
print('\n\t\t\t -- Verificador de Número \n\n')

#Entradas
num = int(input('Digite um número: \n'))
if (num % 2) == 0:
    print(f'\n{num} é par!')
else:
    print(f'\n{num} é impar!')