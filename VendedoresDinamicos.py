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
     for i in range(0, N):
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
     valor_total = 0
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

    case "English":
     print('###########################################################################')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤSeller Registration Program       ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('###########################################################################')
     N = int(input('Enter the number of sellers\n'))
     M = int(input('Enter the quantity of item per salesperson\n'))
     comercio = []
     repetir = "no"
     repeticao = 0
     for i in range(0, N):
       vendedores = {}
       vendedores['name'] = input(f'Enter the name of the seller{i + 1}: ')
       vendedores['itens'] = []
       vendedores['value'] = []
     for j in range(0, M):
        item = input(f'Enter the name of the item {j + 1} sold by the seller {vendedores["name"]}?:\n ')
        valor = float(input(f'Enter the value of the item {j + 1} Sold by the seller {vendedores["name"]}:\n '))
        vendedores['itens'].append(item)
        vendedores['value'].append(valor)
     comercio.append(vendedores)
     valor_total = 0
     while True:
      print(comercio)
      nome_vendedor = input('Which seller you want to buy from, or type "Finish" to exit:\n ')
      if nome_vendedor.lower() == 'end':
         break
      for vendedor in comercio:
         if vendedor['name'] == nome_vendedor:
            print(

                f'You chosen salesperson {vendedor["name"]}. The items and values are: {vendedor["itens"]} - {vendedor["value"]}')
            while repetir == "no":
                if repeticao == 0:
                    confimar = input('Do you want to buy this item?\n')
                else:
                    confimar = input('Do you want to repurchase this item?\n')
                if confimar == 'yes':
                    repeticao = repeticao + 1
                    valor_total += sum(vendedor['value'])
                else:
                    trocar = input('Do you want to switch sellers?\n')
                    break
            print(
                f'The total amount of purchases per salesperson is ${valor_total:.2f} bucks,along with the last purchase'
                f'vendedor(a) {vendedor["name"]} ')
            break
      else:
         print(f'The salesperson  "{nome_vendedor}" Not found. Please try again.')

    case "日本語":
     print('###########################################################################')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ     出品者登録プログラム             ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('###########################################################################')
     N = int(input('販売者の数を入力します\n'))
     M = int(input('販売員ごとの品目の数量を入力します\n'))
     comercio = []
     repetir = "いいえ"
     repeticao = 0
     for i in range(0, N):
       vendedores = {}
       vendedores['名前'] = input(f'販売者の名前を入力します{i + 1}: ')
       vendedores['項目'] = []
       vendedores['価値'] = []
     for j in range(0, M):
        item = input(f'アイテムの名前を入力します {j + 1}.売り手が販売{vendedores["名前"]}?:\n ')
        valor = float(input(f'アイテムの値を入力します {j + 1}. 売り手が販売 {vendedores["名前"]}:\n '))
        vendedores['項目'].append(item)
        vendedores['価値'].append(valor)
     comercio.append(vendedores)
     valor_total = 0
     while True:
      print(comercio)
      nome_vendedor = input('どの販売者から購入するか、「完了」と入力して終了します:\n ')
      if nome_vendedor.lower() == '完了':
         break
      for vendedor in comercio:
         if vendedor['名前'] == nome_vendedor:
            print(

                f'営業担当者を選んだ {vendedor["名前"]}. 項目と値は次のとおりです。 {vendedor["項目"]} - {vendedor["価値"]}')
            while repetir == "いいえ":
                if repeticao == 0:
                    confimar = input('この商品を購入しますか?\n')
                else:
                    confimar = input('このアイテムを再購入しますか?\n')
                if confimar == 'はい':
                    repeticao = repeticao + 1
                    valor_total += sum(vendedor['価値'])
                else:
                    trocar = input('販売者を切り替えますか?\n')
                    break
            print(
                f'販売員あたりの購入の合計金額は  {valor_total:.2f} です.最後の購入と一緒に'
                f'店員 {vendedor["名前"]} ')
            break
      else:
         print(f'営業担当者。"{nome_vendedor}" 見つかりませんでした。. もう一度やり直してください.')