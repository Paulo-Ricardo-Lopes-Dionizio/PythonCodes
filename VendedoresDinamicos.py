N = int(input('Digite a quantidade de vendedores\n'))
M = int(input('Digite a quantidade de item por vendedor\n'))
linhas = N
colunas = M
vendedores = [0] * N
itens = [0] * M
valor = [0] * M

for i in range(0,N):
    vendedores[i] = str(input('Quais os nomes dos vendedores? : \n'))
    for j in range(0, M):
        itens[j] = str(input('Quais os itens dos vendedores? : \n'))
        valor[j] = float(input('Quais os valores dos vendedores?\n'))
    print(vendedores)
    print(f'{itens, valor}')




