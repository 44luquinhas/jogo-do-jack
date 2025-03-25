import random

print('===========================================')
print('Bem Vindo(a) ao Jogo De Adivinhação!')
print('===========================================')

numero_secreto = round(random.randrange(1,51))
total_de_tentativas = 3
pontos = 5000

print(numero_secreto)
print('Qual o nível desejado?\n')
print('(1) Fácil (2) Médio (3) Difícil')

nivel = int(input ('Digite o nível desejado: '))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5


for rodada in range (1, total_de_tentativas + 1):
    print(f'Tentativa {rodada} de {total_de_tentativas}')
    chute = int(input('Digite o seu número: '))

    acertou = numero_secreto == chute
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    print(f'Você Digitou {chute}')

    if(acertou):
        print(f'Você acertou! Sua pontuação foi {pontos} pontos!')
        break 

    else: 
        if(chute_maior):
            (print('Seu Número foi maior que o Número Escolhido'))

        elif(chute_menor):
            (print('Seu número foi menor que o Número Escolhido'))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


print('-----------')
print('Fim de Jogo')
print('-----------')



