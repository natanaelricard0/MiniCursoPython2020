# Faça um programa que calcule a área de um círculo e exiba o resultado na tela. {Fórmula: A = pi * raio ^ 2}

import math #importa a biblioteca math do Python para utilizarmos o Pi

raio = float(input('Informe o valor do raio: ')) #pede para o usuário informar o raio do círculo

area = (math.pi * raio ** 2) #fórmula para área do círculo, guarda o valor numa variável

print('A área do círculo é',area,'m^2') #mostra na tela o resultado que foi guardado na variável área para o usuário