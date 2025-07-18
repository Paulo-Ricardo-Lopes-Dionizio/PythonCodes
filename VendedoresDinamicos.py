print('###########################################################################')
print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🇧🇷Português🇧🇷 - 🇺🇸English🇺🇸 - 🎌日本語🎌ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
print('###########################################################################')
linguagem = str(input('digite qual linguagem vai usar\nEnter which language you are going to use\n使用する言語を入力します\n\n'))
match linguagem:
    case "Português":
     print('###########################################################################')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤPrograma de Cadastro de Vendedoresㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('###########################################################################')
     N = int(input('Digite a quantidade de vendedores(as)\n'))
     M = int(input('Digite a quantidade de item por vendedor(a)\n'))
     comercio = []
     repetir = "não"
     repeticao = 0
     valor_total = 0
     for i in range(0, N):

       vendedores = {}
       #vendedores['nome'] = input(f'Digite o nome do(a) vendedor(a) {i + 1}: ')

       vendedores['itens'] = []
       vendedores['valores'] = []
     for j in range(0, M):
        item = input(f'Digite o nome do item {j + 1} vendido pelo(a) vendedor(a) {vendedores['nome']}?:\n ')
        valor = float(input(f'Digite o valor do item {j + 1} vendido pela(a) vendedor(a) {vendedores['nome']}:\n '))
        vendedores['itens'].append(item)
        vendedores['valores'].append(valor)
     comercio.append(vendedores)

     while True:
      print(comercio)
      nome_vendedor = input('Qual o(a) vendedor(a) que você deseja comprar ou digite "Finalizar" para sair:\n ')
      if nome_vendedor.lower() == 'finalizar':
         break
      for vendedor in comercio:
         if vendedor['nome'] == nome_vendedor:
            print(
                f'Você escolheu o(a) vendedor(a) {vendedor["nome"]}. Os itens e valores são: {vendedor["itens"]} - {vendedor["valores"]}')
            while repetir == "não":
                if repeticao == 0:
                    confimar = input('Deseja comprar esse item?\n')
                else:
                    confimar = input('Deseja comprar novamente esse item?\n')
                if confimar == 'sim':
                    repeticao = repeticao + 1
                    valor_total += sum(vendedor['valores'])
                else:
                    trocar = input('deseja trocar de vendedor?\n')
                    break
            print(
                f'O valor total de compras por vendedor é R${valor_total:.2f}, junto com a ultima compra pelo(a) '
                f'vendedor(a) {vendedor["nome"]} ')
            break
      else:
         print(f'O(a) vendedor(a) "{nome_vendedor}" não foi encontrado(a). Tente novamente.')

#arrumar depois