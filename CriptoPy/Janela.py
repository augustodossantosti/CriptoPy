# Software para Criptografia de Mensagens
# @author: Augusto dos Santos
# Aluno de Análise e Desenvolvimento de Sistemas - FATEC

# Importando bibliotecas e Módulos

from functools import partial
from tkinter import *
from Funcoes import *

# Propriedades da Janela

janela = Tk()
janela.geometry("800x600+250+30")
janela.title("CriptoPy - 0.0.1")

# Widgets

lb1 = Label(janela, text="Insira a Mensagem para ser Criptografada/Descriptograda:")
lb1.place(x=40, y=130)

lb2 = Label(janela, text="A Mensagem de saída será exibida aqui:")
lb2.place(x=490, y=130)

txt1 = Text(janela, width=45, height=20)
txt1.place(x=20, y=160)

txt2 = Text(janela, width=45, height=20)
txt2.place(x=420, y=160)

# Funções e Botões

CriptoPy = Funções(txt1, txt2)

btn1 = Button(janela, width=20, text="Criptografar", command=CriptoPy.cript)
btn1.place(x=30, y=500)

btn2 = Button(janela, width=20, text="Descriptografar", command=CriptoPy.descript)
btn2.place(x=220, y=500)

btn3 = Button(janela, width=20, text="Copiar Mensagem", command=CriptoPy.areaTransf)
btn3.place(x=430, y=500)

btn4 = Button(janela, width=20, text="Salvar Mensagem", command=CriptoPy.salvaTexto)
btn4.place(x=620, y=500)

janela.mainloop()

# Ajuda Tkinter = C:/Python34/Lib/tkinter/__init__.py
