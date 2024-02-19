from tkinter import *
class teste1:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1,text='Guinando')
        self.msg.pack()
janela = Tk()
teste1(janela)
janela.geometry('300x300')
botao = Button(janela, width=20,text='botao1')
botao.place(x=80,y=140)
janela.title('teste')
janela.mainloop()