print('###########################################################################')
print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🇧🇷Português🇧🇷 - 🇺🇸English🇺🇸 - 🎌日本語🎌ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
print('###########################################################################')
linguagem = str(input('digite qual linguagem vai usar\nEnter which language you are going to use\n使用する言語を入力します\n\n'))

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
    case "Português":
     print('###########################################################################')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤPrograma de Cadastro de Vendedoresㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('###########################################################################')
     for i in range(0, 10):
         # Aqui você vai colocar os nomes das pessoas
         vendedores[i] = input('Quais são os nomes dos vendedores?\n')
     # ele ira mexer com o controle de repetição de compras
     while repetir == 'não':

         print('###########################################################################')
         # vai escolher o vendedor
         vendedor[i] = input(f'Digite qual Vendedor deseja comprar?\n{vendedores} ou Finalizar\n')
         # controla o retorno para a pergunta
         trocar = 'não'
         # organiza os vendedores com suas pré-locações
         while trocar == 'não':
             # vendedor e indentificado e executado
             if vendedor[i] == vendedores[0]:
                 print('###########################################################################')
                 print(f'{vendedores[0]} vender:\nKatanas = 7 reais')
                 # execução de compra
                 if pecas[0] == 0:
                     confimar = input('Deseja comprar essa peça?\n')
                 else:
                     confimar = input('Deseja comprar novamente essa peça?\n')
                     print('###########################################################################')
                     #compra finalizada
                 if confimar == 'sim':
                     # organiza os itens colocados no carrinho
                     pecas[0] = pecas[0] + 1
                     # insere o valor do item
                     precoV[0] = precoV[0] + 7
                 else:
                     # retorna para a pergunta
                     trocar = input('deseja trocar de vendedor?\n')

             ###########################################################################

             elif vendedor[i] == vendedores[1]:
                 print('###########################################################################')
                 print(f'{vendedores[1]} vender:\nEspada de Grayskull = 15 reais')
                 if pecas[1] == 0:
                     confimar = input('Deseja comprar essa peça?\n')
                 else:
                     confimar = input('Deseja comprar novamente essa peça?\n')
                     print('###########################################################################')
                 if confimar == 'sim':

                     pecas[1] = pecas[1] + 1
                     precoV[1] = precoV[1] + 15
                 else:
                     trocar = input('deseja trocar de vendedor?\n')

             ##############################################################################

             elif vendedor[i] == vendedores[2]:
                 print('###########################################################################')
                 print(f'{vendedores[2]} vender:\nNecroSword = 99 reais')
                 if pecas[2] == 0:
                     confimar = input('Deseja comprar essa peça?\n')
                 else:
                     confimar = input('Deseja comprar novamente essa peça?\n')
                     print('###########################################################################')
                 if confimar == 'sim':

                     pecas[2] = pecas[2] + 1
                     precoV[2] = precoV[2] + 99
                 else:
                     trocar = input('deseja trocar de vendedor?\n')

             ##############################################################################

             elif vendedor[i] == vendedores[3]:
                 print('###########################################################################')
                 print(f'{vendedores[3]} vender:\nEscudo de Metal = 30 reais')
                 if pecas[3] == 0:
                     confimar = input('Deseja comprar essa peça?\n')
                 else:
                     confimar = input('Deseja comprar novamente essa peça?\n')
                     print('###########################################################################')
                 if confimar == 'sim':

                     pecas[3] = pecas[3] + 1
                     precoV[3] = precoV[3] + 30
                 else:
                     trocar = input('deseja trocar de vendedor?\n')

             ##############################################################################

             elif vendedor[i] == vendedores[4]:
                 print('###########################################################################')
                 print(f'{vendedores[4]} vender:\nArmadura do Revenã de Ferro = 900 reais')
                 if pecas[4] == 0:
                     confimar = input('Deseja comprar essa peça?\n')
                 else:
                     confimar = input('Deseja comprar novamente essa peça?\n')
                     print('###########################################################################')
                 if confimar == 'sim':

                     pecas[4] = pecas[4] + 1
                     precoV[4] = precoV[4] + 900
                 else:
                     trocar = input('deseja trocar de vendedor?\n')

             ##############################################################################

             elif vendedor[i] == vendedores[5]:
                 print('###########################################################################')
                 print(f'{vendedores[5]} vender:\nOlho de agamotto = 125 reais')
                 if pecas[5] == 0:
                     confimar = input('Deseja comprar essa peça?\n')
                 else:
                     confimar = input('Deseja comprar novamente essa peça?\n')
                     print('###########################################################################')
                 if confimar == 'sim':

                     pecas[5] = pecas[5] + 1
                     precoV[5] = precoV[5] + 125
                 else:
                     trocar = input('deseja trocar de vendedor?\n')

             ##############################################################################

             elif vendedor[i] == vendedores[6]:
                 print('###########################################################################')
                 print(f'{vendedores[6]} vender:\nArmadura de Pegasus = 250 reais')
                 if pecas[6] == 0:
                     confimar = input('Deseja comprar essa peça?\n')
                 else:
                     confimar = input('Deseja comprar novamente essa peça?\n')
                     print('###########################################################################')
                 if confimar == 'sim':

                     pecas[6] = pecas[6] + 1
                     precoV[6] = precoV[6] + 250
                 else:
                     trocar = input('deseja trocar de vendedor?\n')

             ##############################################################################

             elif vendedor[i] == vendedores[7]:
                 print('###########################################################################')
                 print(f'{vendedores[7]} vender:\nSoro do Super-Soldado = 550 reais')
                 if pecas[7] == 0:
                     confimar = input('Deseja comprar essa peça?\n')
                 else:
                     confimar = input('Deseja comprar novamente essa peça?\n')
                     print('###########################################################################')
                 if confimar == 'sim':

                     pecas[7] = pecas[7] + 1
                     precoV[7] = precoV[7] + 550
                 else:
                     trocar = input('deseja trocar de vendedor?\n')

             ##############################################################################

             elif vendedor[i] == vendedores[8]:
                 print('###########################################################################')
                 print(f'{vendedores[8]} vender:\nPoção de Cura = 10 reais')
                 if pecas[8] == 0:
                     confimar = input('Deseja comprar essa peça?\n')
                 else:
                     confimar = input('Deseja comprar novamente essa peça?\n')
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
                     confimar = input('Deseja comprar essa peça?\n')
                 else:
                     confimar = input('Deseja comprar novamente essa peça?\n')
                     print('###########################################################################')

                 if confimar == 'sim':

                     pecas[9] = pecas[9] + 1
                     precoV[9] = precoV[9] + 10
                 else:
                     trocar = input('deseja trocar de vendedor?\n')

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
     print('###########################################################################')
     # Resultado final
     print('Vendedores\n', vendedores, '\nValores\n', precoV, '\nPeças Vendidas\n', pecas, '\nTotal a pagar!\n', Total)
     print('###########################################################################')

    case "English":
     repetir = 'no'
     trocar = 'no'
     print('###########################################################################')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤSeller Registration Programㅤㅤㅤㅤㅤ ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('###########################################################################')
     for i in range(0, 10):
     #Here you will put the names of the people
         vendedores[i] = input('What are the names of the sellers?\n')
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
                 print(f'Mr(s).{vendedores[0]} sell:\nKatanas = 7 bucks')
                 # Purchase Execution
                 if pecas[0] == 0:
                    confimar = input('Do you want to buy this piece?\n')
                 else:
                    confimar = input('Do you want to buy this piece? again?\n')
                    print('###########################################################################')
             #Checkout Completed
                 if confimar == 'yes':
                    pecas[0] = pecas[0] + 1
                    # Enter the value of the item
                    precoV[0] = precoV[0] + 7
                 else:
             # Returns to the question
                    trocar = input('Do you want to switch sellers?\n')
             ###########################################################################
             elif vendedor[i] == vendedores[1]:
                 print('###########################################################################')
                 print(f'Mr(s).{vendedores[1]} sell:\nSword of Grayskull = 15 bucks')
                 if pecas[1] == 0:
                      confimar = input('Do you want to buy this piece?\n')
                 else:
                      confimar = input('Do you want to buy this piece again?\n')
                      print('###########################################################################')
                 if confimar == 'yes':
                      pecas[1] = pecas[1] + 1
                      precoV[1] = precoV[1] + 15
                 else:
                      trocar = input('Do you want to switch sellers?\n')
             ##############################################################################
             elif vendedor[i] == vendedores[2]:
                 print('###########################################################################')
                 print(f'Mr(s).{vendedores[2]} sell:\nNecroSword = 99 bucks')
                 if pecas[2] == 0:
                      confimar = input('Do you want to buy this piece?\n')
                 else:
                      confimar = input('Do you want to buy this piece again?\n')
                      print('###########################################################################')
                 if confimar == 'yes':
                      pecas[2] = pecas[2] + 1
                      precoV[2] = precoV[2] + 99
                 else:
                      trocar = input('Do you want to switch sellers?\n')
                      ##############################################################################
             elif vendedor[i] == vendedores[3]:
                 print('###########################################################################')
                 print(f'Mr(s).{vendedores[3]} sell:\nshield of metal = 30 bucks')
                 if pecas[3] == 0:
                      confimar = input('Do you want to buy this piece?\n')
                 else:
                      confimar = input('Do you want to buy this piece again?\n')
                      print('###########################################################################')
                 if confimar == 'yes':
                      # Organizes the items placed in the cart
                      pecas[3] = pecas[3] + 1
                      precoV[3] = precoV[3] + 30
                 else:
                      trocar = input('Do you want to switch sellers?\n')
                      ##############################################################################
             elif vendedor[i] == vendedores[4]:
                  print('###########################################################################')
                  print(f'Mr(s).{vendedores[4]} sell  :\nIron Revenan Armor = 900 bucks')
                  if pecas[4] == 0:
                     confimar = input('Do you want to buy this piece?\n')
                  else:
                     confimar = input('Do you want to buy this piece again?\n')
                     print('###########################################################################')
                  if confimar == 'yes':
                     # Organizes the items placed in the cart
                     pecas[4] = pecas[4] + 1
                     precoV[4] = precoV[4] + 900
                  else:
                     trocar = input('Do you want to switch sellers?\n')
             ##############################################################################
             elif vendedor[i] == vendedores[5]:
                  print('###########################################################################')
                  print(f'Mr(s).{vendedores[5]} sell:\nEye of agamotto = 125 bucks')
                  if pecas[5] == 0:
                      confimar = input('Do you want to buy this piece?\n')
                  else:
                      confimar = input('Do you want to buy this piece again?\n')
                      print('###########################################################################')
                  if confimar == 'yes':
                      # Organizes the items placed in the cart
                      pecas[5] = pecas[5] + 1
                      precoV[5] = precoV[5] + 125
                  else:
                      trocar = input('Do you want to switch sellers?\n')
             ##############################################################################
             elif vendedor[i] == vendedores[6]:
                  print('###########################################################################')
                  print(f'Mr(s).{vendedores[6]} sell:\nArmor of Pegasus = 250 bucks')
                  if pecas[6] == 0:
                    confimar = input('Do you want to buy this piece?\n')
                  else:
                    confimar = input('Do you want to buy this piece again?\n')
                    print('###########################################################################')
                  if confimar == 'sim':
                    pecas[6] = pecas[6] + 1
                    precoV[6] = precoV[6] + 250
                  else:
                    trocar = input('Do you want to switch sellers?\n')
                    ##############################################################################
             elif vendedor[i] == vendedores[7]:
                  print('###########################################################################')
                  print(f'Mr(s).{vendedores[7]} sell:\nSuper-Soldier Serum = 550 bucks')
                  if pecas[7] == 0:
                    confimar = input('Do you want to buy this piece?\n')
                  else:
                    confimar = input('Do you want to buy this piece again?\n')
                    print('###########################################################################')
                  if confimar == 'yes':
                    # Organizes the items placed in the cart
                    pecas[7] = pecas[7] + 1
                    precoV[7] = precoV[7] + 550
                  else:
                    trocar = input('Do you want to switch sellers?\n')
             ##############################################################################
             elif vendedor[i] == vendedores[8]:
                  print('###########################################################################')
                  print(f'Mr(s).{vendedores[8]} sell:\nHealing Potion = 10 bucks')
                  if pecas[8] == 0:
                    confimar = input('Do you want to buy this piece?\n')
                  else:
                    confimar = input('Do you want to buy this piece again?\n')
                    print('###########################################################################')
                  if confimar == 'yes':
                    # Organizes the items placed in the cart
                    pecas[8] = pecas[8] + 1
                    precoV[8] = precoV[8] + 10
                  else:
                    trocar = input('Do you want to switch sellers?\n')
                 ##############################################################################
             elif vendedor[i] == vendedores[9]:
                  print('###########################################################################')
                  print(f'Mr(s).{vendedores[9]} sell:\nPc Gamer = 10 bucks')
                  if pecas[9] == 0:
                   confimar = input('Do you want to buy this piece?\n')
                  else:
                   confimar = input('Do you want to buy this piece again?\n')
                   print('###########################################################################')
                  if confimar == 'yes':
                    # Organizes the items placed in the cart
                   pecas[9] = pecas[9] + 1
                   precoV[9] = precoV[9] + 10
                  else:
                   trocar = input('Do you want to switch sellers?\n')
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
     print('###########################################################################')
     # Bottom line
     print('Sellers\n', vendedores, '\nValues\n', precoV, '\nParts Sold\n', pecas, '\nTotal payable!\n',Total)
     print('###########################################################################')

    case "日本語":
     repetir = 'いいえ'
     trocar = 'いいえ'
     print('###########################################################################')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ出品者登録プログラム  ㅤㅤㅤㅤ ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
     print('###########################################################################')
     for i in range(0, 10):
         # ここに、人の名前を入れます
         vendedores[i] = input('売り手の名前は何ですか?\n')
         # リピート購入管理を台無しにします
     while repetir == 'いいえ':

         print('###########################################################################')
         # 売り手を選びます
         vendedor[i] = input(f'どの売り手を購入しますか?\n{vendedores}または終了\n')
         # 質問の戻り値を制御します
         trocar = 'いいえ'
         # カートに入れた商品を整理します
         while trocar == 'いいえ':
                ###########################################################################
                # 売り手が特定され、実行される
                if vendedor[i] == vendedores[0]:
                  print('###########################################################################')
                  print(f'{vendedores[0]} 販売:\nKatanas = 7 ¥')
                  # 購入実行
                  if pecas[0] == 0:
                      confimar = input('この作品を買いますか?\n')
                  else:
                      confimar = input('この作品を買いますか?又。\n')
                      print('###########################################################################')
                  # チェックアウト完了
                  if confimar == 'はい':
                      # カートに入れた商品を整理します
                      pecas[0] = pecas[0] + 1
                      # アイテムの値を入力します
                      precoV[0] = precoV[0] + 7
                  else:
                      # 質問に戻る
                      trocar = input('売り手を切り替えますか?\n')

                ###########################################################################

                elif vendedor[i] == vendedores[1]:
                  print('###########################################################################')
                  print(f'{vendedores[1]} 販売:\nSword of Grayskull = 15  ¥')
                  if pecas[1] == 0:
                      confimar = input('この作品を買いますか?\n')
                  else:
                      confimar = input('この作品を買いますか?又。\n')
                      print('###########################################################################')
                  if confimar == 'はい':
                      pecas[1] = pecas[1] + 1
                      precoV[1] = precoV[1] + 15
                  else:
                      trocar = input('売り手を切り替えますか?\n')
               ##############################################################################

                elif vendedor[i] == vendedores[2]:
                  print('###########################################################################')
                  print(f'{vendedores[2]} 販売:\nNecroSword = 99  ¥')
                  if pecas[2] == 0:
                      confimar = input('この作品を買いますか?\n')
                  else:
                      confimar = input('この作品を買いますか?又。\n')
                      print('###########################################################################')
                  if confimar == 'はい':
                      pecas[2] = pecas[2] + 1
                      precoV[2] = precoV[2] + 99
                  else:
                      trocar = input('売り手を切り替えますか?\n')
               ##############################################################################

                elif vendedor[i] == vendedores[3]:
                  print('###########################################################################')
                  print(f'{vendedores[3]} 販売:\nshield of metal = 30  ¥')
                  if pecas[3] == 0:
                      confimar = input('この作品を買いますか?\n')
                  else:
                      confimar = input('この作品を買いますか?又。\n')
                      print('###########################################################################')
                  if confimar == 'はい':
                      # カートに入れた商品を整理します
                      pecas[3] = pecas[3] + 1
                      precoV[3] = precoV[3] + 30
                  else:
                      trocar = input('売り手を切り替えますか?\n')
              ##############################################################################

                elif vendedor[i] == vendedores[4]:
                  print('###########################################################################')
                  print(f'{vendedores[4]} 販売:\nIron Revenan Armor = 900  ¥')
                  if pecas[4] == 0:
                      confimar = input('この作品を買いますか?\n')
                  else:
                      confimar = input('この作品を買いますか?又。\n')
                      print('###########################################################################')
                  if confimar == 'はい':
                      # カートに入れた商品を整理します
                      pecas[4] = pecas[4] + 1
                      precoV[4] = precoV[4] + 900
                  else:
                      trocar = input('売り手を切り替えますか?\n')
               ##############################################################################

                elif vendedor[i] == vendedores[5]:
                  print('###########################################################################')
                  print(f'{vendedores[5]} 販売:\nEye of agamotto = 125  ¥')
                  if pecas[5] == 0:
                      confimar = input('この作品を買いますか?\n')
                  else:
                      confimar = input('この作品を買いますか?又。\n')
                      print('###########################################################################')
                  if confimar == 'はい':
                      # カートに入れた商品を整理します
                      pecas[5] = pecas[5] + 1
                      precoV[5] = precoV[5] + 125
                  else:
                      trocar = input('売り手を切り替えますか?\n')

                ##############################################################################

                elif vendedor[i] == vendedores[6]:
                  print('###########################################################################')
                  print(f'{vendedores[6]} 販売:\nArmor of Pegasus = 250  ¥')
                  if pecas[6] == 0:
                      confimar = input('この作品を買いますか?\n')
                  else:
                      confimar = input('この作品を買いますか?又。\n')
                      print('###########################################################################')
                  if confimar == 'はい':
                      pecas[6] = pecas[6] + 1
                      precoV[6] = precoV[6] + 250
                  else:
                      trocar = input('売り手を切り替えますか?\n')
                ##############################################################################

                elif vendedor[i] == vendedores[7]:
                  print('###########################################################################')
                  print(f'{vendedores[7]} 販売:\nSuper-Soldier Serum = 550  ¥')
                  if pecas[7] == 0:
                      confimar = input('この作品を買いますか?\n')
                  else:
                      confimar = input('この作品を買いますか?又。\n')
                      print('###########################################################################')
                  if confimar == 'はい':

                      pecas[7] = pecas[7] + 1
                      precoV[7] = precoV[7] + 550
                  else:
                      trocar = input('売り手を切り替えますか?\n')
                ##############################################################################

                elif vendedor[i] == vendedores[8]:
                  print('###########################################################################')
                  print(f'{vendedores[8]} 販売:\nHealing Potion = 10  ¥')
                  if pecas[8] == 0:
                      confimar = input('この作品を買いますか?\n')
                  else:
                      confimar = input('この作品を買いますか?又。\n')
                      print('###########################################################################')
                  if confimar == 'はい':
                      pecas[8] = pecas[8] + 1
                      precoV[8] = precoV[8] + 10
                  else:
                      trocar = input('売り手を切り替えますか?\n')

                ##############################################################################

                elif vendedor[i] == vendedores[9]:
                  print('###########################################################################')
                  print(f'{vendedores[9]} 販売:\nPc Gamer = 10  ¥')
                  if pecas[9] == 0:
                      confimar = input('この作品を買いますか?\n')
                  else:
                      confimar = input('この作品を買いますか?又。\n')
                      print('###########################################################################')

                  if confimar == 'はい':
                      pecas[9] = pecas[9] + 1
                      precoV[9] = precoV[9] + 10
                  else:
                      trocar = input('売り手を切り替えますか?\n')

                ##############################################################################
                 # これでプロセスは終了です
                elif vendedor[i] == '完了':
                  repetir = 'はい'
                  trocar = 'はい'

                ##############################################################################
                #ここで、売り手の名前にタイプがある場合
                elif vendedor[i] != vendedores[i]:
                  print('###########################################################################')
                  print('もう一度書き込む')
                  vendedor[i] = input(f'どの売り手を購入しますか?\n{vendedores}または終了\n')
         # Total value of sellers
         Total = sum(precoV)
         print('###########################################################################')
         # Bottom line
         print('売り手\n', vendedores, '\n価値観\n', precoV, '\n販売部品\n', pecas, '\n合計支払額!\n',Total)
         print('###########################################################################')