from PySimpleGUI import PySimpleGUI as sg
from random import choice
from time import sleep

p1escolha = ''
pcescolha = ''
result = ''
possibilidades = ['PEDRA', 'PAPEL', 'TESOURA']

# layout
sg.theme('Reddit')
layout = [
    [sg.Button(f'{"PEDRA":^48}', key='PEDRA')],
    [sg.Button(f'{"PAPEL":^49}', key='PAPEL')],
    [sg.Button(f'{"TESOURA":^46}', key='TESOURA')],        
    [sg.Output(size=(33, 6))]
]
# janela
janela = sg.Window('JOKENPÔ', layout)

# ler eventos 
while True:
    eventos, valores = janela.read()
    pcescolha = choice(possibilidades)
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'PEDRA':
        p1escolha = 'PEDRA'
    elif eventos == 'PAPEL':
        p1escolha = 'PAPEL'
    elif eventos == 'TESOURA':
        p1escolha = 'TESOURA' 

    if pcescolha == p1escolha:
        result = 'EMPATE, TENTE NOVEMENTE!'
    elif pcescolha == 'PEDRA' and p1escolha == 'PAPEL' or pcescolha == 'PAPEL' and p1escolha == 'TESOURA' or pcescolha == 'TESOURA' and p1escolha == 'PEDRA':
        result = 'PARABÉNS, VOCÊ VENCEU!'
    else:
        result = 'PERDEU, TENTE NOVAMENTE!'

    if eventos == 'PEDRA' or eventos == 'PAPEL' or eventos == 'TESOURA':
        print('......................JO', end=''), sleep(0.5), print('KEN', end=''), sleep(0.5), print('PÔ..................')
        print(f'Você escolheu: {p1escolha}\nE o computador escolheu: {pcescolha}')
        print(result)
        print('........................................................')
