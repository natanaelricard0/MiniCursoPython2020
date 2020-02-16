# 2- Faça um programa que receba três notas e imprima a média aritmética

nota1 = int(input('Informe a primeira nota: ')) #pede para o usuário a primeira nota
nota2 = int(input('Informe a segunda nota: ')) #pede para o usuário a segunda nota
nota3 = int(input('Informe a terceira nota: ')) #pede para o usuário a terceira nota

media = nota1 + nota2 + nota3 / 3 #efetua a soma e a divide pela quantidade de notas (tal como qualquer media) e guarda o valor numa variável denominada média

print('Sua média é:', media) #mostra a string 'sua média é' seguido da variável média, são separados por vírgula devido a sintaxe da linguagem
