from random import randint
pedra = 1

papel = 2

tesoura = 3

print('=-'*25)

print('J O K E N P Ô'.center(50))

print('-='*25)

jogador = str(input('FAÇA SUA JOGADA\n[PEDRA,PAPEL OU TESOURA]\nDIGITE QUAL: ').strip().upper())

print('=-'*25)

pc = randint(1,3)

if pc == 1:

    pc = pedra

elif pc == 2:

    pc = papel

elif pc == 3:

    pc = tesoura

############################# JOGADAS DA MAQUINA - WINS ###########################

if (jogador == 'PEDRA')and(pc == papel): #PAPEL GANHA DE PEDRA

    print(' ** MAQUINA VENCEU! **'.center(50))

    print(f'[ SUA JOGADA: {jogador} | JOGADA DA MAQUINA: PAPEL ]'.center(50))

elif (jogador == 'PAPEL')and(pc == tesoura): #TESOURA GANHA DE PAPEL

    print(' ** MAQUINA VENCEU! **'.center(50))

    print(f'[ SUA JOGADA: {jogador} | JOGADA DA MAQUINA: TESOURA ]'.center(50))

    

elif (jogador == 'TESOURA')and(pc == pedra): #PEDRA GANHA DE TESOURA

    print(' ** MAQUINA VENCEU! **'.center(50))

    print(f'[ SUA JOGADA: {jogador} | JOGADA DA MAQUINA: PEDRA ]'.center(50))

############################## EMPATES #############################################

elif (jogador == 'PEDRA')and(pc == pedra): #EMPATE - PEDRA

    print(' ** EMPATE **'.center(50))

    print(f'[ SUA JOGADA: {jogador} | JOGADA DA MAQUINA: PEDRA ]'.center(50))

elif (jogador == 'PAPEL')and(pc == papel): #EMPATE - PAPEL

    print(' ** EMPATE **'.center(50))

    print(f'[ SUA JOGADA: {jogador} | JOGADA DA MAQUINA: PAPEL ]'.center(50))

elif (jogador == 'TESOURA')and(pc == tesoura): #EMPATE - TESOURA

    print(' ** EMPATE **'.center(50))

    print(f'[ SUA JOGADA: {jogador} | JOGADA DA MAQUINA: TESOURA ]'.center(50))

############################ JOGADAS DO JOGADOR - WINS ################################

elif (jogador == 'PEDRA')and(pc == tesoura):  # PEDRA GANHA TESOURA

    print(' ** VOCÊ VENCEU ** '.center(50))

    print(f'[ SUA JOGADA: {jogador} | JOGADA DA MAQUINA: TESOURA ]'.center(50))

elif (jogador == 'papel')and(pc == pedra): #Papel ganha pedra

    print(' ** VOCÊ VENCEU ** '.center(50))

    print(f'[ SUA JOGADA: {jogador} | JOGADA DA MAQUINA: PEDRA ]'.center(50))

elif (jogador == 'TESOURA')and(pc == papel): #TESOURA GANHA DE PAPEL

    print(' ** VOCÊ VENCEU ** '.center(50))

    print(f'[ SUA JOGADA: {jogador} | JOGADA DA MAQUINA: PAPEL ]'.center(50))

elif (jogador == 'PAPEL')and( pc == pedra): #PAPEL ganha pedra

    print(' ** VOCÊ VENCEU ** '.center(50))

    print(f'[ SUA JOGADA: {jogador} | JOGADA DA MAQUINA: PAPEL ]'.center(50))

