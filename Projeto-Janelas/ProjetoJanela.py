from tkinter import *
global contador
contador = 0
def executar():
    global contador
    texto1 = 'numero impar :'
    texto2 = 'numero par :'
    if (contador %2 ) == 0:
        resultado = texto2 + str(contador)
        RespostaTexto['text'] = resultado
        RespostaTexto['fg'] = '#24851e'
        #print(texto2)
        #print(contador)
    else:
        resultado = texto1 + str(contador)
        RespostaTexto['text'] = resultado
        RespostaTexto['fg'] = '#F70000'
        #print(texto1)
        #print(contador)
    contador += 1
#class teste1:
 #   def __init__(self, master=None):
  #      self.widget1 = Frame(master)
   #     self.widget1.pack()
    #    self.msg = Label(self.widget1,text='Guinando')
     #   self.msg.pack()

janela = Tk()
#executar()
janela.title('teste')
janela.geometry('250x250')
#teste1(janela)coloca o texto em posiçao inicial na parte superior no centro
#botao.place(x=80,y=140) posição em qualquer ligar sem quadro de responsividade
RespostaTexto = Label(janela, width=15,height=2,text='texto apresentado',relief='flat',fg='#fcb603',bg='#121211')
RespostaTexto.grid(row=0,column=0,padx=10,pady=10)
#botao = Button(janela, width=10,height=1,text='botao1',relief='flat',fg='#fcb603',bg='#121211')
#botao.grid(row=0,column=0,padx=10,pady=10)
botao2 = Button(janela,command=executar, width=10,height=1,text='botao2',relief='flat',fg='#fcb603',bg='#121211')
botao2.grid(row=0,column=1,padx=10,pady=10)
janela.mainloop()