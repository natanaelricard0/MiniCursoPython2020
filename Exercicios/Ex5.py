# 5- Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input('Informe seu sexo digitando F ou M: ')) #pede para o usuário informar a letra inicial do seu sexo

if sexo == 'm': #se o usuário digitar a letra m ele printa masculino 
    print('M - Masculino')
    
elif sexo == 'f': #se o usuário digitar a letra f ele printa feminino
    print('F - Feminino')
    
else:
    print('Sexo inválido')