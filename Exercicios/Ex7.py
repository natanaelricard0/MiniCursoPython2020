# 6- Faça um programa que receba uma temperatura em Fahrenheit e a converta para Celsius. {Fórmula: C = (F - 32) / 1.8}

tempF = float(input('Informe a temperatura em Fahrenheit: ')) #recebe a temperatura em Fahrenheit e guarda numa variável

tempC = (tempF - 32 / 1.8) #pega a temperatura em Fahrenheit, aplica numa fórmula, e guarda numa variável

print('A temperatura de',tempF,'Fahrenheit','em Celsius é:',tempC) #mostra na tela o resultado da conversão