import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
import os
import tkinter.filedialog



def selecionar():
       caminho = filedialog.askopenfilename(
            title='Selecione o aquivo CSV',
            filetypes=(
                ("CSV files", "*.csv"),
                ("all files", "*.*") )
        )
       return caminho


def data_plot():
    caminho = selecionar()
 
     
    if caminho: 
       dados = pd.read_csv(caminho)
       meses =  dados['meses'].to_list()
       valores = dados['valores'].to_list()
       fig, grafico = plt.subplots()
       grafico.plot(meses, valores)
       

       # tkinter com o pyplot
       canvas= FigureCanvasTkAgg(fig, master=janela)
       canvas.draw()
       canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand = True)
    else:
        print('Erro o processo')  




janela  =  tk.Tk()

btn1 =  tk.Button(janela, text = 'Plot Bar', command = data_plot )
btn1.pack(pady=5)

janela.mainloop()
















# dicionario = {
# 'a':[1,2,3,5,5,25],
# 'b':[4,5,6,10,10,10]
# }

# # d1 =[[1,2,3, 4,5,5,7,5],[1,2,3,6,6,10,6,10],[4,536,5,56,2,89]]

# # dados = pd.DataFrame(d1,columns= ['a', 'b', 'c'])
# dadoss = pd.DataFrame(dicionario)

# print(dadoss.head())
# print(dadoss.tail())
# print(dadoss.describe())


# # d  =  dados['c'][0]
# # print(dadoss)


# # dados2 = pd.Series(dicionario)
# # d =  dados2[1]

# # print(d)
