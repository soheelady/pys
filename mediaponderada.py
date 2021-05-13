# Calculadora de Média Ponderada:

print('Olá, Bem vindo a Calculadora de média ponderada')
print('Por favor digite as notas conforme solicitado:')

# Calculando:
while True:
    try:
        nota_1 = float(input(f'Qual a sua primeira nota?\n>'))
        nota_2 = float(input(f'Qual a sua segunda nota?\n'))
        nota_3 = float(input(f'Qual a sua terceira nota?\n>'))
        nota_4 = float(input(f'Qual a sua quarta nota?\n>'))
        media_1 = (((nota_1 * 1.50) + (nota_2 * 1.50) + (nota_3 * 4.00) + (nota_4 * 3.00)) / 10)
        if media_1 >= 7:
            print(f'Sua média é de {media_1}, parabéns, você foi aprovado!')
        if media_1 <= 7:
            print(f'Sua média é {media_1}, sinto muito mas você não foi aprovado.')
        break    # para o loop

    # Tratando Possíveis Erros:
    except ValueError:
        print('Por favor tente novamente, digite apenas números!')
