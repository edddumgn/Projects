import random
def jogar():
	user = input("Escolha uma jogada!\n'r'para rock(PEDRA), 'p' for paper(PAPEL) e 's' para scissors(TESOURA): ")
	computer = random.choice(["r","p","s"])
	print(f'O computador escolheu {computer}!')
	if user == computer:
		return "Empate"
	if vencer(user,computer):
		return "Você ganhou!!!"
	return "Você perdeu! Tente novamente!" 	
		
def vencer(jogador,oponente):
	if (jogador == "r" and oponente == "s") or (jogador == "s" and oponente == "p") or (jogador == "p" and oponente == "r"):
		return True
		
print(jogar())	
