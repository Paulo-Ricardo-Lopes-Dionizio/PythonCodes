lista = ['item1','item2','item3']
print(lista[1][2])#chamar item + caracter(depende do numero,se tiver total de 4 letras são vai ate 3 e virse e versa)
print(lista[1])#destaca o item selecionado

n = lista.index('item1')#endereço da do item
print(n)
lista2 = ['item1-1','item2-1',['sub-item1','sub-item2']]
print(lista2[2][0])#pegado uma lista de outra sub-lista, em resumo

lista3 = lista + lista2
print(lista3)#soma de listas

listaN = [1,2,3,4,5,7,12,15,9]
print(max(listaN))
print(min(listaN))
print(sum(listaN))#soma

lista4 = []
lista4.insert(0,'primeiro')#posição + item
lista4.insert(1,'meio')
lista4.append(('ultimo'))#ultima posição
print(lista4)

lista5 = [0,1,2,3,4,5,6,7,8,9,10]
del lista5[0]#deleta a posição selecionada
del lista5[0:5]#deleta de um tanto para tanto por posição
print(lista5)

lista6 = ['a','b','c','d','e','f','g']
lista6.pop()#vazio tira o ultimo item, so botar algum numero de posição para tirar ele,vire comentario para usar o p1 e p2
print(lista6)
p1 = lista6.pop(0)#armazena o item da posição
p2 = lista6.pop(4)
print(p1)
print(p2)

lista7=[1,2,3,4,5,6,7,8,3,1,5,3,6,7]
lista7.clear()
print(lista7)

lista8=[1,2,3,4,5,6,7,8,3,1,5,3,6,7]
lista8.sort()
lista8.reverse()
print(len(lista8))
print(lista8)

tupla1 = tuple("aeiou")
tupla2 = "a", "e", "i", "o", "u"
tupla3 = ("a", "e", "i", "o", "u")
print(tupla1,tupla2,tupla3)#imutaveis mas divide as palavras


print(type(lista6))#fala das classes delas

#concatenação
tupla4="Domingo","Segunda","Terça"
tupla4 +="Quarta","quinta","sexta","sabado"
print(tupla4)

lista9 = [('1','paulo'),('2','Jose'),('3','Marcus')]
selecao = dict(lista9)#fez um tipo de lista de cadastro
print(selecao['1'])
selecao['2'] = 'JoseNeto'#mudou de item
print(selecao['2'])
selecao['4'] = 'Novo'
print(selecao)
selecao.update({'5':'Novo2','6':'Novo3'})
print(selecao)
del selecao['6']
print(selecao)

print(selecao.keys())
print(selecao.items())#keys + values
print(selecao.values())

