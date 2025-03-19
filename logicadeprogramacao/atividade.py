
# Analise o problema e verifique quais são os dados que o usuário precisa fornecer (digitar). 
sexo = input('Escolha se é homem ou mulher:')
altura = float(input('Digite a sua altura:'))

if sexo == 'homem':
    peso_ideal = (72.7 * altura) -58
    print(f'Seu peso ideal é:{peso_ideal:.2f}kg')

elif sexo == 'mulher':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é:{peso_ideal:.2f}kg')