# 12- Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input('Informe uma nota entre 0 e 10: ')) #pede a nota para o usuário

while True: #enquanto for verdade...
    if nota < 0 or nota > 10: #se a nota for menor do que 0 OU maior do que 10 mostre na tela para tentar novamente
        print('Nota inválida, tente novamente') 
        nota = float(input('Informe uma nota entre 0 e 10: ')) #mostra o menu input para o usuário
        continue #continua repetindo caso a condição não seja atendida
    break #caso a condição seja atendida, o programa para de executar (break = parar)
