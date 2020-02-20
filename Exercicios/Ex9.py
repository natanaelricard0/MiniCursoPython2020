# 9- Faça um programa que receba três notas, mostre a média aritmética delas e informe se o aluno foi aprovado ou reprovado ( média para passar= 6).

n1 = float(input('Informe sua primeira nota: ')) #pede para o usuário informar suas 3 notas
n2 = float(input('Informe sua segunda nota: '))
n3 = float(input('Informe sua terceira nota: '))

media = (n1 + n2 + n3) / 3 #faz a soma e divide pela quantidade de notas e guarda o resultado numa variável denominada media

print(media) #mostra na tela o resultado que foi guardado na variável média

if media < 6: #se a nota for menor que 6 ele mostra para o usuário que ele foi reprovado
    print('Reprovado')
else: #se não mostra que está aprovado
    print('Aprovado')