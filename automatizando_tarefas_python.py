import pyautogui as pag
import time

''' COMANDOS

pag.press() >> aperta uma tecla
pag.click() >> clica com o mouse
pag.write() >> escreve um texto
pag.hotkey("crtl", "c") >> escreve um atalho do pc

'''
pag.PAUSE = 0.5 # o programa espera 0.5s entre cada comando executado

# abriria o navegador (Chrome)

pag.press("win")
pag.write("chrome")
pag.press("enter")

# entrar no site

pag.write("hashtagtreinamentos.com/curso-python")
pag.press("enter")
time.sleep(5)

# preencher fomulário

pag.click(x=..., y=...) # olhar o arquivo posição.py, que pega a posição do mouse na tela
pag.write("Érika")
pag.press("tab")

pag.write("email")
pag.press("tab")

pag.write("telefone") # mesmo sendo um número, deve estar entre aspas
pag.press("tab")

# enviar o formulário

pag.press("enter")

