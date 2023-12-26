linguagem = str(input('Qual o seu idioma? English\n Português\n 日本語\n'))
match linguagem:
    case "English":
        value = int(input('Enter the value to find the perfect square for it!\n'))
        Perfect_Square = [value ** 2 for i in range(1)]
        print(Perfect_Square)

    case "Português":
        valor = int(input('Digite o valor para saber o quadrado perfeito dele!\n'))
        quadrado_Perfeito = [valor ** 2 for i in range(1)]
        print(quadrado_Perfeito)

    case "日本語":
        価値 = int(input('値を入力して、それにぴったりの正方形を見つけてください!\n'))
        パーフェクトスクエア = [価値 ** 2 for i in range(1)]
        print(パーフェクトスクエア)




