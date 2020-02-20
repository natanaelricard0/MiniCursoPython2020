# 10- Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:

n1 = float(input('Informe sua primeira nota: ')) #pede para o usuário informar suas 4 notas parciais
n2 = float(input('Informe sua segunda nota: '))
n3 = float(input('Informe sua terceira nota: '))
n4 = float(input('Informe sua quarta nota: '))

media = (n1 + n2 + n3 + n4) / 4 #soma as notas e divide pela quantidade de notas

print(media) #mostra a media na tela

if media >= 6 and media < 10: #se a media for maior ou igual a 6 e menor que 10 mostra que foi aprovado
    print('Aprovado')
    
elif media == 10: #se a nota for igual a 10 mostra que foi aprovado com distinção
    print('Aprovado com distinção')
    
elif media < 6: #se a media for menor do que 6 mostra que foi reprovado
    print('Reprovado')


    