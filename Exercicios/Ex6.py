# 5- Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input('Informe uma letra: '))

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('Vogal')
    
else:
    print('Consoante')