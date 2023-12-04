N = int(input('Digite a quantidade de vendedores(as)\n'))
M = int(input('Digite a quantidade de item por vendedor(a)\n'))

comercio = []
repeticao = 0

for i in range(0,N):
    vendedores = {}
    vendedores['nome'] = input(f'Digite o nome do(a) vendedor(a) {i + 1}: ')
    vendedores['itens'] = []
    vendedores['valores'] = []
    for j in range(0, M):
        item = input(f'Digite o nome do item {j + 1} vendido pelo(a) vendedor(a) {vendedores["nome"]}?:\n ')
        valor = float(input(f'Digite o valor do item {j + 1} vendido pela(a) vendedor(a) {vendedores["nome"]}:\n '))

        vendedores['itens'].append(item)
        vendedores['valores'].append(valor)
    comercio.append(vendedores)
print(comercio)
while True:
    nome_vendedor = input('Qual o(a) vendedor(a) que você deseja comprar ou digite "Finalizar" para sair:\n ')
    if nome_vendedor.lower() == 'finalizar':
        break
    for vendedor in comercio:
        if vendedor['nome'] == nome_vendedor:
            print(f'Você escolheu o(a) vendedor(a) {vendedor["nome"]}. Os itens e valores são: {vendedor["itens"]} - {vendedor["valores"]}')
            #if repeticao == 0:
                #confimar = input('Deseja comprar esse item?\n')
           # else:
               # confimar = input('Deseja comprar novamente esse item?\n')

            #if confimar == 'sim':
                #repeticao = repeticao + 1
                #vendedor["valor"] = vendedor["valor"]
            #else:
                #trocar = input('deseja trocar de vendedor?\n')
                #break
            break
    else:
        print(f'O(a) vendedor(a) "{nome_vendedor}" não foi encontrado(a). Tente novamente.')