# 12- Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nomeUsuario = input('Informe seu nome: ') #pede as informações do usuário
senhaUsuario = input('Informe sua senha: ')

while nomeUsuario == senhaUsuario: #enquanto nome de usuário for igual a senha, o programa deve pedir novamente as informações do usuário
    print('Nome de usuário não pode ser igual senha, tente novamente') #caso sejam iguais, o programa pede para o usuário enviar novamente suas informações
    nomeUsuario = input('Informe seu nome: ')
    senhaUsuario = input('Informe sua senha: ')

