import pywhatkit
import pandas
import time as hora
from datetime import datetime as data
import pyautogui as py
from selenium.webdriver.common.keys import Keys as enviarMensagem

datahora = data.now()
dataAtual = datahora.day
min = datahora.minute
horario = 22
minuto = min + 1

contatos = pandas.read_csv("contatos.csv")
try:
        while True:
                if dataAtual == 16 :
                        for i, mensagem in enumerate(contatos['Mensagem']):
                                pessoa = contatos.loc[i, "Pessoa"]
                                numeroTelefone = contatos.loc[i,"Número"]
                                telefone = f"+55{numeroTelefone}"
                                pywhatkit.sendwhatmsg(telefone,mensagem,horario,minuto)
                                minuto += 1
                                hora.sleep(5)
                        print('Mensagem enviada')
                else:
                        print('Hoje não e dia de enviar um lembrete')
                        break
except:
        print('Erro de codigo')
