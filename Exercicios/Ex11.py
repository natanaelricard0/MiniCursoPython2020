# 11- Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

prod1 = float(input('Informe o preço do 1° produto: ')) #pede o preço dos 3 produtos para o usuário
prod2 = float(input('Informe o preço do 2° produto: '))
prod3 = float(input('Informe o preço do 3° produto: '))

if prod1 < prod2 and prod1 < prod3: #se o produto 1 for menor que o produto 2 e do que o produto 3, produto 1 é o mais barto
    print('O produto 1 é o mais barato')

elif prod2 < prod1 and prod2 < prod3: #senão, o produto 2 for menor do que o produto 1 e do que o produto 3, produto 2 é o mais barato
    print('O produto 2 é o mais barato')

elif prod3 < prod1 and prod3 < prod2: #senão, o produto 3 for menor do que o produto 1 e do que o produto 2, produto 3 é o mais barato 
    print('O produto 3 é o mais barato')