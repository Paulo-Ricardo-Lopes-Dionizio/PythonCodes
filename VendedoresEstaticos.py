#dados dos arquivos
pecas = [0] * 10
contador = 0
preco = 0
precoV = [0] * 10
vendedores = [0] * 10
vendedor = [0] * 10
repetir = 'não'
trocar = 'não'
print('Criador:Paulo Ricardo Lopes Dionizio')
print('###########################################################################')
print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤPrograma de Cadastro de Vendedoresㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
print('#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ#')
print('###########################################################################')

#aqui vc vai colocar a quantidade de pessoas a serem registradas
for i in range(0,10):
    #Aqui você vai colocar os nomes das pessoas
    vendedores[i] = input('Quais são os nomes dos vendedores?\n')
#ele ira mexer com o controle de repetição de compras
while repetir == 'não':

    print('###########################################################################')
    #vai escolher o vendedor
    vendedor[i] = input(f'Digite qual Vendedor deseja comprar?\n{vendedores} ou Finalizar\n')
    #controla o retorno para a pergunta
    trocar = 'não'
    #organiza os vendedores com suas pré-locações
    while trocar == 'não':
        ###########################################################################
        #vendedor e indentificado e executado
        if vendedor[i] == vendedores[0]:
            print('###########################################################################')
            print(f'{vendedores[0]} vender:\nKatanas = 7 reais')
            #execução de compra
            if pecas[0] == 0:
                confimar = input('Deseja comprar essa peça?\n')
            else:
                confimar = input('Deseja comprar novamente essa peça?\n')
                print('###########################################################################')
            #compra finalizada
            if confimar == 'sim':
                #organiza os itens colocados no carrinho
                pecas[0] = pecas[0] + 1
                #insere o valor do item
                precoV[0] = precoV[0] + 7
            else:
                #retorna para a pergunta
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
            print(f'{vendedores[2]} vender:\nNecroSword = 99 reais')
            if pecas[2] == 0:
                confimar = input('Deseja comprar essa peça?\n')
            else:
                confimar = input('Deseja comprar novamente essa peça?\n')
            if confimar == 'sim':

                pecas[2] = pecas[2] + 1
                precoV[2] = precoV[2] + 99
            else:
                trocar = input('deseja trocar de vendedor?\n')

        ##############################################################################

        elif vendedor[i] == vendedores[3]:
            print(f'{vendedores[3]} vender:\nEscudo de Metal = 30 reais')
            if pecas[3] == 0:
                confimar = input('Deseja comprar essa peça?\n')
            else:
                confimar = input('Deseja comprar novamente essa peça?\n')
            if confimar == 'sim':

                pecas[3] = pecas[3] + 1
                precoV[3] = precoV[3] + 30
            else:
                trocar = input('deseja trocar de vendedor?\n')

        ##############################################################################

        elif vendedor[i] == vendedores[4]:
            print(f'{vendedores[4]} vender:\nArmadura do Revenã de Ferro = 900 reais')
            if pecas[4] == 0:
                confimar = input('Deseja comprar essa peça?\n')
            else:
                confimar = input('Deseja comprar novamente essa peça?\n')
            if confimar == 'sim':

                pecas[4] = pecas[4] + 1
                precoV[4] = precoV[4] + 900
            else:
                trocar = input('deseja trocar de vendedor?\n')

        ##############################################################################

        elif vendedor[i] == vendedores[5]:
            print(f'{vendedores[5]} vender:\nOlho de agamotto = 125 reais')
            if pecas[5] == 0:
                confimar = input('Deseja comprar essa peça?\n')
            else:
                confimar = input('Deseja comprar novamente essa peça?\n')
            if confimar == 'sim':

                pecas[5] = pecas[5] + 1
                precoV[5] = precoV[5] + 125
            else:
                trocar = input('deseja trocar de vendedor?\n')

        ##############################################################################

        elif vendedor[i] == vendedores[6]:
            print(f'{vendedores[6]} vender:\nArmadura de Pegasus = 250 reais')
            if pecas[6] == 0:
                confimar = input('Deseja comprar essa peça?\n')
            else:
                confimar = input('Deseja comprar novamente essa peça?\n')
            if confimar == 'sim':

                pecas[6] = pecas[6] + 1
                precoV[6] = precoV[6] + 250
            else:
                trocar = input('deseja trocar de vendedor?\n')

        ##############################################################################

        elif vendedor[i] == vendedores[7]:
            print(f'{vendedores[7]} vender:\nSoro do Super-Soldado = 550 reais')
            if pecas[7] == 0:
                confimar = input('Deseja comprar essa peça?\n')
            else:
                confimar = input('Deseja comprar novamente essa peça?\n')
            if confimar == 'sim':

                pecas[7] = pecas[7] + 1
                precoV[7] = precoV[7] + 550
            else:
                trocar = input('deseja trocar de vendedor?\n')

        ##############################################################################

        elif vendedor[i] == vendedores[8]:
            print(f'{vendedores[8]} vender:\nPoção de Cura = 10 reais')
            if pecas[8] == 0:
                confimar = input('Deseja comprar essa peça?\n')
            else:
                confimar = input('Deseja comprar novamente essa peça?\n')
            if confimar == 'sim':

                pecas[8] = pecas[8] + 1
                precoV[8] = precoV[8] + 10
            else:
                trocar = input('deseja trocar de vendedor?\n')

        ##############################################################################

        elif vendedor[i] == vendedores[9]:
            print(f'{vendedores[9]} vender:\nPc Gamer = 10 reais')
            if pecas[9] == 0:
                confimar = input('Deseja comprar essa peça?\n')
            else:
                confimar = input('Deseja comprar novamente essa peça?\n')

            if confimar == 'sim':

                pecas[9] = pecas[9] + 1
                precoV[9] = precoV[9] + 10
            else:
                trocar = input('deseja trocar de vendedor?\n')

        ##############################################################################
        #aqui finaliza o processo
        elif vendedor[i] == 'finalizar':
            repetir = 'sim'
            trocar = 'sim'

        ##############################################################################
        #aqui caso aja erro na digitação no nome dos vendedores
        elif vendedor[i] != vendedores[i]:
            print('###########################################################################')
            print('Digite novamente')
            vendedor[i] = input(f'Digite qual Vendedor deseja comprar?\n{vendedores} ou Nenhum\n')
#valor total dos vendedores
Total = sum(precoV)
print('###########################################################################')
#Resultado final
print('Vendedores\n', vendedores, '\nValores\n', precoV, '\nPeças Vendidas\n', pecas, '\nTotal a pagar!\n', Total)
print('###########################################################################')