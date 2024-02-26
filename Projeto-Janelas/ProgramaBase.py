from tkinter import *

janela = Tk()
janela.title('Programa 1.0')
janela.geometry('1280x600')
barramenu = Menu(janela)

arquivo = Menu(barramenu, tearoff=0)
barramenu.add_cascade(label='Arquivo', menu=arquivo)
arquivo.add_command(label='Novo arquivo', command=None)
arquivo.add_command(label='Abrir..',command=None)
arquivo.add_command(label='Salvar', command=None)
arquivo.add_separator()
arquivo.add_command(label='Sair/Fechar', command=janela.destroy)

editar = Menu(barramenu, tearoff=0)

barramenu.add_cascade(label='Editar', menu=editar)
editar.add_command(label='Cortar', command=None)
editar.add_command(label='Copiar', command=None)
editar.add_command(label='Colar', command=None)
editar.add_command(label='selecionar tudo', command=None)
editar.add_separator()
editar.add_command(label='Procurar...', command=None)
editar.add_command(label='Procurar denovo', command=None)

ajuda = Menu(barramenu, tearoff=0)
barramenu.add_cascade(label='Ajudar', menu=ajuda)
ajuda.add_command(label='Ajuda Usuario', command=None)
ajuda.add_command(label='Previa', command=None)
ajuda.add_separator()
ajuda.add_command(label='Ajuda usuario', command=None)



menubutton = Menubutton(janela, text="Idiomas")

menubutton.menu = Menu(menubutton)
menubutton["menu"] = menubutton.menu

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

menubutton.menu.add_radiobutton(label="Português", variable=var1,command=None)
menubutton.menu.add_radiobutton(label="English", variable=var2,command=None)
menubutton.menu.add_radiobutton(label="日本語", variable=var3,command=None)

menubutton.pack()

janela.config(menu = barramenu)
mainloop()
