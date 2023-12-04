N = int(input('Digite a quantidade de vendedores\n'))
M = int(input('Digite a quantidade de item por vendedor\n'))

repetir = 'finalizar'
comercio = []

for i in range(0,N):
    vendedores = {}
    vendedores['nome'] = input(f'Digite o nome do vendedor {i + 1}: ')
   # vendedores['nomes'] = []
    vendedores['itens'] = []
    vendedores['valores'] = []
    for j in range(0, M):
        #vendedor = input(f'Quais os nomes dos vendedores {j + 1} ?: \n')
        item = input(f'Digite o nome do item {j + 1} vendido pelo vendedor {vendedores["nome"]}?:\n ')
        valor = float(input(f'Digite o valor do item {j + 1} vendido pelo vendedor {vendedores["nome"]}:\n '))
        #vendedores['nomes'].append(vendedor)
        vendedores['itens'].append(item)
        vendedores['valores'].append(valor)
    comercio.append(vendedores)
print(comercio)
#print(f'Senhores: {vendedor}')
while repetir == 'finalizar':
    comercio[i] = input(f'Digite qual Vendedor deseja comprar? ou Finalizar\n')
    print(f'Você escolheu o {comercio[i]}\n os itens e valores são : ({item} - {valor})')

