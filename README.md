# Automação com pyautogui

import pyautogui as pag
import time

pag.PAUSE = 0.5 # o programa espera 0.5s entre cada comando executado

# abriria o navegador (Chrome)

pag.press("win")
pag.write("chrome")
pag.press("enter")

# entrar no site

pag.write("site desejado")
pag.press("enter")
time.sleep(5)

# preencher fomulário

pag.click(x=..., y=...) # posição do mouse na tela
pag.write("nome")
pag.press("tab")

pag.write("email")
pag.press("tab")

pag.write("telefone") # mesmo sendo um número, deve estar entre aspas
pag.press("tab")

# enviar o formulário

pag.press("enter")

# Pegando a posição do mouse na tela 

import pyautogui as pag
import time

time.sleep(5) # colocar o mouse onde se quer a posição
print(pag.position()) # me dá a posição do mouse na tela
