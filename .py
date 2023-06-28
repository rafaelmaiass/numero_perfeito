numero = int(input('Digite um número: '))
divisores = []

for dividir in range(1, numero):
    if numero % dividir == 0:
        divisores.append(dividir)

if sum(divisores) == numero:
    print(f'O número {numero} é perfeito.')
else:
    print(f'O número {numero} não é perfeito.')
