import random
from time import sleep

print('Lançando os dados!!')
sleep(1)
ponto = ('...')
for i in ponto:
	sleep(0.2)
	print(i,end='',flush=True)
	

x1 = x2 = x3 = x4 = x5 = x6 = cont = 0

dadoLan = random.randint(1,7)
sleep(2)
while cont < 100:
	dadoLan = random.randint(1,7)
	if dadoLan == 1:
		x1 += 1
		cont += 1
	elif dadoLan == 2:
		x2 += 1
		cont += 1   
	elif dadoLan == 3:
		x3 += 1
		cont += 1
	elif dadoLan == 4:
		x4 += 1
		cont += 1
	elif dadoLan == 5:
		x5 += 1
		cont += 1
	elif dadoLan == 6:
		x6 += 1
		cont += 1
print(f'\nA quantidade de vezes que o dado caiu no numero 1 foi {x1}')
print(f'A quantidade de vezes que o dado caiu no numero 2 foi {x2}')
print(f'A quantidade de vezes que o dado caiu no numero 3 foi {x3}')
print(f'A quantidade de vezes que o dado caiu no numero 4 foi {x4}')
print(f'A quantidade de vezes que o dado caiu no numero 5 foi {x5}')
print(f'A quantidade de vezes que o dado caiu no numero 6 foi {x6}')
	
