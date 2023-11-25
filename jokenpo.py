import os
import time
import random

pontos_jogador = 0
pontos_pc = 0
jogar_novamente = 1

while jogar_novamente != 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('==========================')
    print('Papel, Pedra ou Tesoura')
    print('==========================')
    print('')
    print('PLACAR:')
    print('Você: {}'.format(pontos_jogador))
    print('Computador: {}'.format(pontos_pc))
    print('\n')
    print('Escolha o seu lance:')
    print('1 - Papel | 2 - Pedra | 3 - Tesoura | 0 - Sair do jogo')
    try:
        jogada = int(input())
        while jogada not in [0, 1, 2, 3, 4]:
            print('Erro: a opção selecionada é inválida')
            print('Escolha o seu lance:')
            print('1 - Papel | 2 - Pedra | 3 - Tesoura | 0 - Sair do jogo')
            jogada = int(input())
        if jogada == 0:
            print('Até logo!')
            time.sleep(3)
            break
        jogada_pc = random.choice([1, 2, 3])
        dicionario_jogadas = {1: 'PAPEL', 2: 'PEDRA', 3: 'TESOURA'}

        print('')
        print('==============================')
        print('Sua jogada: {}'.format(dicionario_jogadas[jogada]))
        print('Jogada do computador: {}'.format(dicionario_jogadas[jogada_pc]))
        
        if jogada == 1 and jogada_pc == 1:
            print('Empate!')
        elif jogada == 1 and jogada_pc == 2:
            print('Você venceu!')
            pontos_jogador += 1
        elif jogada == 1 and jogada_pc == 3:
            print('O computador venceu')
            pontos_pc += 1
        elif jogada == 2 and jogada_pc == 1:
            print('O computador venceu')
            pontos_pc += 1
        elif jogada == 2 and jogada_pc == 2:
            print('Empate!')
        elif jogada == 2 and jogada_pc == 3:
            print('Você venceu!')
            pontos_jogador += 1
        elif jogada == 3 and jogada_pc == 1:
            print('Você venceu!')
            pontos_jogador += 1
        elif jogada == 3 and jogada_pc == 2:
            print('O computador venceu')
            pontos_pc += 1
        elif jogada == 3 and jogada_pc == 3:
            print('Empate!')
        
        print('')
        print('PLACAR ATUALIZADO:')
        print('Você: {}'.format(pontos_jogador))
        print('Computador: {}'.format(pontos_pc))

        print('==============================')
        print('')
        print('Deseja jogar novamente? 1 - Sim | 0 - Não')
        jogar_novamente = int(input())
        if jogar_novamente == 0:
            print('Até logo!')
            time.sleep(3)

    except:
        print('Erro: você deve digitar apenas números')
        time.sleep(3)


