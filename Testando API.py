import requests
import json
from tkinter import *



def cotacao_dolar():

    cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacoes = cotacoes.json()
    cotacao_dolar = float(cotacoes['USDBRL']['bid'])
    text_cotacoes['text'] = f'Dollar:   {cotacao_dolar:.2f}'



def cotacao_euro():
    cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacoes = cotacoes.json()
    cotacao_euro = float(cotacoes['EURBRL']['bid'])
    text_cotacoes['text'] = f'Euro:     {cotacao_euro:.2f}'


def cotacao_btc():
    cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacoes = cotacoes.json()
    cotacao_btc = float(cotacoes['BTCBRL']['bid'])
    text_cotacoes['text'] = f'Bitcoin:  {cotacao_btc:.3f}'



janela = Tk()
janela.geometry('500x300')
janela.title('COTAÇÃO')


text_orientacao = Label(janela, text='COTAÇÕES ATUAIS:')
text_orientacao.grid(column=0, row=0,padx=10, pady=10)

botao1 = Button(janela, text='USD', command=cotacao_dolar)
botao1.grid(column=1, row=1, padx=20, pady=20)
botao2 = Button(janela, text='EUR', command=cotacao_euro)
botao2.grid(column=2, row=1, padx=20, pady=20)
botao3 = Button(janela, text='BTC', command=cotacao_btc)
botao3.grid(column=3, row=1, padx=20, pady=20)

text_cotacoes = Label(janela, text='')
text_cotacoes.grid(column=0, row=4, padx=20, pady=20)


janela.mainloop()