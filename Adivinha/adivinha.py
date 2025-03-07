print('===========================================')
print('Bem Vindo(a) ao Jogo De Adivinhação!')
print('===========================================')

numero_secreto = 12
total_de_tentativas = 3
for rodada in range (1, total_de_tentativas + 1):
    print(f'Tentativa {rodada} de {total_de_tentativas}')
    chute = int(input('Digite o seu número: '))

    acertou = numero_secreto == chute
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    print(f'Você Digitou {chute}')

    if(acertou):
        print('Você Acertou!')
        break 

    else: 
        if(chute_maior):
            (print('Seu Número foi maior que o Número Escolhido'))

        elif(chute_menor):
            (print('Seu número foi menor que o Número Escolhido'))


print('-----------')
print('Fim de Jogo')
print('-----------')



