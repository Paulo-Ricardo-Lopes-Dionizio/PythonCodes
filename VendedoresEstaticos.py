print('###########################################################################')
print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🇧🇷Português🇧🇷 - 🇺🇸English🇺🇸 - 🎌日本語🎌ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
print('###########################################################################')
linguagem = str(input('digite qual linguagem vai usar\nEnter which language you are going to use\n使用する言語を入力します\n\n'))
carteira = int(input('digite quanto de dinheiro precisa usar \nenter how much money you need to use \n必要な金額を入力してください\n\n'))

i = 0
pecas = [0] * 10
contador = 0
preco = 0
precoV = [0] * 10
vendedores = [0] * 10
vendedor = [0] * 10
repetir = 'não'
trocar = 'não'
match linguagem:
    case "português":
     print('###########################################################################')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤPrograma de Cadastro de Vendedoresㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('###########################################################################')

     print("Temos no total de 10 vendedores")
     for i in range(0, 10):
         # Aqui você vai colocar os nomes das pessoas
         vendedores[i] = input(f'Qual sera o nome do vendedor(a) número {i + 1} ?\n')
     # ele irá mexer com o controle de repetição de compras
     while repetir == 'não':

         print('###########################################################################')
         # vai escolher o vendedor
         vendedor[i] = input(f'Digite qual Vendedor deseja comprar?\n{vendedores} ou Finalizar\n')
         # controla o retorno para a pergunta
         trocar = 'não'
         # organiza os vendedores com a suas pré-locações
         while trocar == 'não':
             # vendedor e indentificado e executado
             if vendedor[i] == vendedores[0]:
                 print('###########################################################################')
                 print(f'{vendedores[0]} vender:\nKatanas = 7 reais')
                 # execução de compra
                 if pecas[0] == 0:
                     confimar = input('Deseja comprar essa peça?(sim/não)\n')
                 else:
                     confimar = input('Deseja comprar novamente essa peça?(sim/não)\n')
                     print('###########################################################################')
                     #compra finalizada
                 if confimar == 'sim':
                     # organiza os itens colocados no carrinho
                     pecas[0] = pecas[0] + 1
                     # insere o valor do item
                     precoV[0] = precoV[0] + 7
                 else:
                     # retorna para a pergunta
                     trocar = input('deseja trocar de vendedor?(sim/não)\n')

             ###########################################################################

             elif vendedor[i] == vendedores[1]:
                 print('###########################################################################')
                 print(f'{vendedores[1]} vender:\nEspada de Grayskull = 15 reais')
                 if pecas[1] == 0:
                     confimar = input('Deseja comprar essa peça?(sim/não)\n')
                 else:
                     confimar = input('Deseja comprar novamente essa peça?(sim/não)\n')
                     print('###########################################################################')
                 if confimar == 'sim':

                     pecas[1] = pecas[1] + 1
                     precoV[1] = precoV[1] + 15
                 else:
                     trocar = input('deseja trocar de vendedor?(sim/não)\n')

             ##############################################################################

             elif vendedor[i] == vendedores[2]:
                 print('###########################################################################')
                 print(f'{vendedores[2]} vender:\nNecroSword = 99 reais')
                 if pecas[2] == 0:
                     confimar = input('Deseja comprar essa peça?(sim/não)\n')
                 else:
                     confimar = input('Deseja comprar novamente essa peça?(sim/não)\n')
                     print('###########################################################################')
                 if confimar == 'sim':

                     pecas[2] = pecas[2] + 1
                     precoV[2] = precoV[2] + 99
                 else:
                     trocar = input('deseja trocar de vendedor?(sim/não)\n')

             ##############################################################################

             elif vendedor[i] == vendedores[3]:
                 print('###########################################################################')
                 print(f'{vendedores[3]} vender:\nEscudo de Metal = 30 reais')
                 if pecas[3] == 0:
                     confimar = input('Deseja comprar essa peça?(sim/não)\n')
                 else:
                     confimar = input('Deseja comprar novamente essa peça?(sim/não)\n')
                     print('###########################################################################')
                 if confimar == 'sim':

                     pecas[3] = pecas[3] + 1
                     precoV[3] = precoV[3] + 30
                 else:
                     trocar = input('deseja trocar de vendedor?(sim/não)\n')

             ##############################################################################

             elif vendedor[i] == vendedores[4]:
                 print('###########################################################################')
                 print(f'{vendedores[4]} vender:\nArmadura do Revenã de Ferro = 900 reais')
                 if pecas[4] == 0:
                     confimar = input('Deseja comprar essa peça?(sim/não)\n')
                 else:
                     confimar = input('Deseja comprar novamente essa peça?(sim/não)\n')
                     print('###########################################################################')
                 if confimar == 'sim':

                     pecas[4] = pecas[4] + 1
                     precoV[4] = precoV[4] + 900
                 else:
                     trocar = input('deseja trocar de vendedor?(sim/não)\n')

             ##############################################################################

             elif vendedor[i] == vendedores[5]:
                 print('###########################################################################')
                 print(f'{vendedores[5]} vender:\nOlho de agamotto = 125 reais')
                 if pecas[5] == 0:
                     confimar = input('Deseja comprar essa peça?(sim/não)\n')
                 else:
                     confimar = input('Deseja comprar novamente essa peça?(sim/não)\n')
                     print('###########################################################################')
                 if confimar == 'sim':

                     pecas[5] = pecas[5] + 1
                     precoV[5] = precoV[5] + 125
                 else:
                     trocar = input('deseja trocar de vendedor?(sim/não)\n')

             ##############################################################################

             elif vendedor[i] == vendedores[6]:
                 print('###########################################################################')
                 print(f'{vendedores[6]} vender:\nArmadura de Pegasus = 250 reais')
                 if pecas[6] == 0:
                     confimar = input('Deseja comprar essa peça?(sim/não)\n')
                 else:
                     confimar = input('Deseja comprar novamente essa peça?(sim/não)\n')
                     print('###########################################################################')
                 if confimar == 'sim':

                     pecas[6] = pecas[6] + 1
                     precoV[6] = precoV[6] + 250
                 else:
                     trocar = input('deseja trocar de vendedor?(sim/não)\n')

             ##############################################################################

             elif vendedor[i] == vendedores[7]:
                 print('###########################################################################')
                 print(f'{vendedores[7]} vender:\nSoro do Super-Soldado = 550 reais')
                 if pecas[7] == 0:
                     confimar = input('Deseja comprar essa peça?(sim/não)\n')
                 else:
                     confimar = input('Deseja comprar novamente essa peça?(sim/não)\n')
                     print('###########################################################################')
                 if confimar == 'sim':

                     pecas[7] = pecas[7] + 1
                     precoV[7] = precoV[7] + 550
                 else:
                     trocar = input('deseja trocar de vendedor?(sim/não)\n')

             ##############################################################################

             elif vendedor[i] == vendedores[8]:
                 print('###########################################################################')
                 print(f'{vendedores[8]} vender:\nPoção de Cura = 10 reais')
                 if pecas[8] == 0:
                     confimar = input('Deseja comprar essa peça?(sim/não)\n')
                 else:
                     confimar = input('Deseja comprar novamente essa peça?(sim/não)\n')
                     print('###########################################################################')
                 if confimar == 'sim':

                     pecas[8] = pecas[8] + 1
                     precoV[8] = precoV[8] + 10
                 else:
                     trocar = input('deseja trocar de vendedor?\n')

             ##############################################################################

             elif vendedor[i] == vendedores[9]:
                 print('###########################################################################')
                 print(f'{vendedores[9]} vender:\nPc Gamer = 10 reais')
                 if pecas[9] == 0:
                     confimar = input('Deseja comprar essa peça?(sim/não)\n')
                 else:
                     confimar = input('Deseja comprar novamente essa peça?(sim/não)\n')
                     print('###########################################################################')

                 if confimar == 'sim':

                     pecas[9] = pecas[9] + 1
                     precoV[9] = precoV[9] + 10
                 else:
                     trocar = input('deseja trocar de vendedor?(sim/não)\n')

             ##############################################################################
             # aqui finaliza o processo
             elif vendedor[i] == 'finalizar':
                 repetir = 'sim'
                 trocar = 'sim'

             ##############################################################################
             # aqui caso aja erro na digitação no nome dos vendedores
             elif vendedor[i] != vendedores[i]:
                 print('###########################################################################')
                 print('Digite novamente')
                 vendedor[i] = input(f'Digite qual Vendedor deseja comprar?\n{vendedores} ou Nenhum\n')
     # valor total dos vendedores
     Total = sum(precoV)
     # valor com a carteira
     Total_carteira = carteira - Total
     print('###########################################################################')
     # Resultado final
     if Total > carteira:
         print('Vendedores\n', vendedores, '\nValores\n', precoV, '\nPeças Vendidas\n', pecas, '\nTotal a pagar!\n',Total, '\n  e devendo\nR$', Total_carteira, ' na carteira')
     else:
        print('Vendedores\n', vendedores, '\nValores\n', precoV, '\nPeças Vendidas\n', pecas, '\nTotal a pagar!\n', Total, '\n Sobrando apenas\nR$',Total_carteira,' na carteira')
        print('###########################################################################')

    case "english":
     repetir = 'no'
     trocar = 'no'
     print('###########################################################################')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤSeller Registration Programㅤㅤㅤㅤㅤ ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('###########################################################################')

     print("We have a total of 10 sellers")
     for i in range(0, 10):
         # Here you will put the names of the people

         vendedores[i] = input(f'What will be the name of the number seller {i + 1} ?\n')
     #It will mess with the repeat purchase control
     while repetir == 'no':
         print('###########################################################################')
     # will choose the seller
         vendedor[i] = input(f'Enter which Seller do you want to buy?\n{vendedores} Or finish\n')
     #Controls the return for the question
         trocar = 'no'
     #Organizes sellers with their pre-leases
         while trocar == 'no':
             #seller is identified and executed
             if vendedor[i] == vendedores[0]:
                 print('###########################################################################')
                 print(f'Mr(s).{vendedores[0]} sell:\nKatanas = 1 bucks')
                 # Purchase Execution
                 if pecas[0] == 0:
                    confimar = input('Do you want to buy this piece?(yes/no)\n')
                 else:
                    confimar = input('Do you want to buy this piece? again?(yes/no)\n')
                    print('###########################################################################')
             #Checkout Completed
                 if confimar == 'yes':
                    pecas[0] = pecas[0] + 1
                    # Enter the value of the item
                    precoV[0] = precoV[0] + 1
                 else:
             # Returns to the question
                    trocar = input('Do you want to switch sellers?(yes/no)\n')
             ###########################################################################
             elif vendedor[i] == vendedores[1]:
                 print('###########################################################################')
                 print(f'Mr(s).{vendedores[1]} sell:\nSword of Grayskull = 2 bucks')
                 if pecas[1] == 0:
                      confimar = input('Do you want to buy this piece?(yes/no)\n')
                 else:
                      confimar = input('Do you want to buy this piece again?(yes/no)\n')
                      print('###########################################################################')
                 if confimar == 'yes':
                      pecas[1] = pecas[1] + 1
                      precoV[1] = precoV[1] + 2
                 else:
                      trocar = input('Do you want to switch sellers?(yes/no)\n')
             ##############################################################################
             elif vendedor[i] == vendedores[2]:
                 print('###########################################################################')
                 print(f'Mr(s).{vendedores[2]} sell:\nNecroSword = 17 bucks')
                 if pecas[2] == 0:
                      confimar = input('Do you want to buy this piece?(yes/no)\n')
                 else:
                      confimar = input('Do you want to buy this piece again?(yes/no)\n')
                      print('###########################################################################')
                 if confimar == 'yes':
                      pecas[2] = pecas[2] + 1
                      precoV[2] = precoV[2] + 17
                 else:
                      trocar = input('Do you want to switch sellers?(yes/no)\n')
                      ##############################################################################
             elif vendedor[i] == vendedores[3]:
                 print('###########################################################################')
                 print(f'Mr(s).{vendedores[3]} sell:\nshield of metal = 5 bucks')
                 if pecas[3] == 0:
                      confimar = input('Do you want to buy this piece?(yes/no)\n')
                 else:
                      confimar = input('Do you want to buy this piece again?(yes/no)\n')
                      print('###########################################################################')
                 if confimar == 'yes':
                      # Organizes the items placed in the cart
                      pecas[3] = pecas[3] + 1
                      precoV[3] = precoV[3] + 5
                 else:
                      trocar = input('Do you want to switch sellers?(yes/no)\n')
                      ##############################################################################
             elif vendedor[i] == vendedores[4]:
                  print('###########################################################################')
                  print(f'Mr(s).{vendedores[4]} sell  :\nIron Revenan Armor = 162 bucks')
                  if pecas[4] == 0:
                     confimar = input('Do you want to buy this piece?(yes/no)\n')
                  else:
                     confimar = input('Do you want to buy this piece again?(yes/no)\n')
                     print('###########################################################################')
                  if confimar == 'yes':
                     # Organizes the items placed in the cart
                     pecas[4] = pecas[4] + 1
                     precoV[4] = precoV[4] + 162
                  else:
                     trocar = input('Do you want to switch sellers?(yes/no)\n')
             ##############################################################################
             elif vendedor[i] == vendedores[5]:
                  print('###########################################################################')
                  print(f'Mr(s).{vendedores[5]} sell:\nEye of agamotto = 22 bucks')
                  if pecas[5] == 0:
                      confimar = input('Do you want to buy this piece?(yes/no)\n')
                  else:
                      confimar = input('Do you want to buy this piece again?(yes/no)\n')
                      print('###########################################################################')
                  if confimar == 'yes':
                      # Organizes the items placed in the cart
                      pecas[5] = pecas[5] + 1
                      precoV[5] = precoV[5] + 22
                  else:
                      trocar = input('Do you want to switch sellers?(yes/no)\n')
             ##############################################################################
             elif vendedor[i] == vendedores[6]:
                  print('###########################################################################')
                  print(f'Mr(s).{vendedores[6]} sell:\nArmor of Pegasus = 45 bucks')
                  if pecas[6] == 0:
                    confimar = input('Do you want to buy this piece?(yes/no)\n')
                  else:
                    confimar = input('Do you want to buy this piece again?(yes/no)\n')
                    print('###########################################################################')
                  if confimar == 'sim':
                    pecas[6] = pecas[6] + 1
                    precoV[6] = precoV[6] + 45
                  else:
                    trocar = input('Do you want to switch sellers?(yes/no)\n')
                    ##############################################################################
             elif vendedor[i] == vendedores[7]:
                  print('###########################################################################')
                  print(f'Mr(s).{vendedores[7]} sell:\nSuper-Soldier Serum = 99 bucks')
                  if pecas[7] == 0:
                    confimar = input('Do you want to buy this piece?(yes/no)\n')
                  else:
                    confimar = input('Do you want to buy this piece again?(yes/no)\n')
                    print('###########################################################################')
                  if confimar == 'yes':
                    # Organizes the items placed in the cart
                    pecas[7] = pecas[7] + 1
                    precoV[7] = precoV[7] + 99
                  else:
                    trocar = input('Do you want to switch sellers?(yes/no)\n')
             ##############################################################################
             elif vendedor[i] == vendedores[8]:
                  print('###########################################################################')
                  print(f'Mr(s).{vendedores[8]} sell:\nHealing Potion = 2 bucks')
                  if pecas[8] == 0:
                    confimar = input('Do you want to buy this piece?(yes/no)\n')
                  else:
                    confimar = input('Do you want to buy this piece again?(yes/no)\n')
                    print('###########################################################################')
                  if confimar == 'yes':
                    # Organizes the items placed in the cart
                    pecas[8] = pecas[8] + 1
                    precoV[8] = precoV[8] + 2
                  else:
                    trocar = input('Do you want to switch sellers?(yes/no)\n')
                 ##############################################################################
             elif vendedor[i] == vendedores[9]:
                  print('###########################################################################')
                  print(f'Mr(s).{vendedores[9]} sell:\nPc Gamer = 1 bucks')
                  if pecas[9] == 0:
                   confimar = input('Do you want to buy this piece?(yes/no)\n')
                  else:
                   confimar = input('Do you want to buy this piece again?(yes/no)\n')
                   print('###########################################################################')
                  if confimar == 'yes':
                    # Organizes the items placed in the cart
                   pecas[9] = pecas[9] + 1
                   precoV[9] = precoV[9] + 1
                  else:
                   trocar = input('Do you want to switch sellers?(yes/no)\n')
            ##############################################################################
             # This is the end of the process
             elif vendedor[i] == 'finish':
                 repetir = 'yes'
                 trocar = 'yes'
             ##############################################################################
             # Here if there is a typo in the name of the sellers
             elif vendedor[i] != vendedores[i]:
                  print('###########################################################################')
                  print('write again')
                  vendedor[i] = input(f'Enter which Seller do you want to buy?\n{vendedores} Or finish\n')
     # Total value of sellers
     Total = sum(precoV)
     # value with the wallet
     Total_carteira = carteira - Total
     print('###########################################################################')
     # Final result
     if Total > carteira:
         print('Sellers\n', vendedores, '\nValues\n', precoV, '\nParts Sold\n', pecas, '\nTotal to pay!\n',
               Total, '\n and owing\nUS$', Total_carteira, ' in wallet')
     else:
         print('Sellers\n', vendedores, '\nValues\n', precoV, '\nParts Sold\n', pecas, '\nTotal to pay!\n',
               Total, '\nOnly US$\n left', Total_carteira, ' in wallet')

    case "日本語":
        repetir = 'いいえ'
        trocar = 'いいえ'
        print('###########################################################################')
        print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
        print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ販売者登録プログラムㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
        print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
        print('###########################################################################')

        print("合計で10人の販売者がいます")
        for i in range(0, 10):
            vendedores[i] = input(f'販売者番号 {i + 1} の名前を入力してください:\n')

        while repetir == 'いいえ':
            print('###########################################################################')
            vendedor[i] = input(f'どの販売者から購入しますか？\n{vendedores} または "終了"\n')
            trocar = 'いいえ'

            while trocar == 'いいえ':
                if vendedor[i] == vendedores[0]:
                    print('###########################################################################')
                    print(f'{vendedores[0]} の商品:\nカタナ = ¥187')
                    confimar = input('この商品を購入しますか？\n') if pecas[0] == 0 else input(
                        'もう一度この商品を購入しますか？\n')
                    print('###########################################################################')
                    if confimar == 'はい':
                        pecas[0] += 1
                        precoV[0] += 187
                    else:
                        trocar = input('別の販売者に切り替えますか？\n')

                elif vendedor[i] == vendedores[1]:
                    print('###########################################################################')
                    print(f'{vendedores[1]} の商品:\nグレイスカルの剣 = ¥402')
                    confimar = input('この商品を購入しますか？\n') if pecas[1] == 0 else input(
                        'もう一度この商品を購入しますか？\n')
                    print('###########################################################################')
                    if confimar == 'はい':
                        pecas[1] += 1
                        precoV[1] += 402
                    else:
                        trocar = input('別の販売者に切り替えますか？\n')

                elif vendedor[i] == vendedores[2]:
                    print('###########################################################################')
                    print(f'{vendedores[2]} の商品:\nネクロソード = ¥2651')
                    confimar = input('この商品を購入しますか？\n') if pecas[2] == 0 else input(
                        'もう一度この商品を購入しますか？\n')
                    print('###########################################################################')
                    if confimar == 'はい':
                        pecas[2] += 1
                        precoV[2] += 2651
                    else:
                        trocar = input('別の販売者に切り替えますか？\n')

                elif vendedor[i] == vendedores[3]:
                    print('###########################################################################')
                    print(f'{vendedores[3]} の商品:\nメタルシールド = ¥804')
                    confimar = input('この商品を購入しますか？\n') if pecas[3] == 0 else input(
                        'もう一度この商品を購入しますか？\n')
                    print('###########################################################################')
                    if confimar == 'はい':
                        pecas[3] += 1
                        precoV[3] += 804
                    else:
                        trocar = input('別の販売者に切り替えますか？\n')

                elif vendedor[i] == vendedores[4]:
                    print('###########################################################################')
                    print(f'{vendedores[4]} の商品:\nアイアン・レヴナントの鎧 = ¥24111')
                    confimar = input('この商品を購入しますか？\n') if pecas[4] == 0 else input(
                        'もう一度この商品を購入しますか？\n')
                    print('###########################################################################')
                    if confimar == 'はい':
                        pecas[4] += 1
                        precoV[4] += 24111
                    else:
                        trocar = input('別の販売者に切り替えますか？\n')

                elif vendedor[i] == vendedores[5]:
                    print('###########################################################################')
                    print(f'{vendedores[5]} の商品:\nアガモットの目 = ¥3.349')
                    confimar = input('この商品を購入しますか？\n') if pecas[5] == 0 else input(
                        'もう一度この商品を購入しますか？\n')
                    print('###########################################################################')
                    if confimar == 'はい':
                        pecas[5] += 1
                        precoV[5] += 3349
                    else:
                        trocar = input('別の販売者に切り替えますか？\n')

                elif vendedor[i] == vendedores[6]:
                    print('###########################################################################')
                    print(f'{vendedores[6]} の商品:\nペガサスの鎧 = ¥6.698')
                    confimar = input('この商品を購入しますか？\n') if pecas[6] == 0 else input(
                        'もう一度この商品を購入しますか？\n')
                    print('###########################################################################')
                    if confimar == 'はい':
                        pecas[6] += 1
                        precoV[6] += 6698
                    else:
                        trocar = input('別の販売者に切り替えますか？\n')

                elif vendedor[i] == vendedores[7]:
                    print('###########################################################################')
                    print(f'{vendedores[7]} の商品:\nスーパーソルジャー血清 = ¥14.734')
                    confimar = input('この商品を購入しますか？\n') if pecas[7] == 0 else input(
                        'もう一度この商品を購入しますか？\n')
                    print('###########################################################################')
                    if confimar == 'はい':
                        pecas[7] += 1
                        precoV[7] += 14734
                    else:
                        trocar = input('別の販売者に切り替えますか？\n')

                elif vendedor[i] == vendedores[8]:
                    print('###########################################################################')
                    print(f'{vendedores[8]} の商品:\n回復のポーション = ¥268')
                    confimar = input('この商品を購入しますか？\n') \
                        if pecas[8] == 0 else input(
                        'もう一度この商品を購入しますか？\n')
                    print('###########################################################################')
                    if confimar == 'はい':
                        pecas[8] += 1
                        precoV[8] += 268
                    else:
                        trocar = input('別の販売者に切り替えますか？\n')

                elif vendedor[i] == vendedores[9]:
                    print('###########################################################################')
                    print(f'{vendedores[9]} の商品:\nゲーミングPC = ¥268')
                    confimar = input('この商品を購入しますか？\n') \
                        if pecas[9] == 0 else input(
                        'もう一度この商品を購入しますか？\n')
                    print('###########################################################################')
                    if confimar == 'はい':
                        pecas[9] += 1
                        precoV[9] += 268
                    else:
                        trocar = input('別の販売者に切り替えますか？\n')

                elif vendedor[i] == '終了':
                    repetir = 'はい'
                    trocar = 'はい'

                elif vendedor[i] != vendedores[i]:
                    print('###########################################################################')
                    print('入力ミスです。もう一度入力してください。')
                    vendedor[i] = input(f'どの販売者から購入しますか？\n{vendedores} または "終了"\n')

            Total = sum(precoV)
            Total_carteira = carteira - Total
            print('###########################################################################')
            if Total > carteira:
                print('販売者\n', vendedores, '\n価格\n', precoV, '\n販売された部品\n', pecas,
                      '\n合計金額: ¥', Total,
                      '\nお支払いが足りません！（不足分: ¥', Total_carteira, '）')
            else:
                print('販売者\n', vendedores, '\n価格\n', precoV, '\n販売された部品\n', pecas,
                      '\n合計金額: ¥', Total,
                      '\n財布に残っている金額: ¥', Total_carteira)
            print('###########################################################################')
