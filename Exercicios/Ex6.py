# 6- Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input('Informe uma letra: ')) #é declarado um str pois o usuario poderia apenas digitar texto (string)
 
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u': # se letra for igual a OU b OU c...
    print('Vogal') #o programa mostra "Vogal"
    
else:
    print('Consoante') #se não, consoante 