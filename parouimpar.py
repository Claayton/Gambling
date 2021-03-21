# def parouimpar(): 
from PySimpleGUI import PySimpleGUI as sg
from random import randint

# layout
sg.theme('Reddit')
layout = [
    [sg.Text(f'{"Voce escolhe PAR ou IMPAR? ":<35}')],
    [sg.Radio(f'{" PAR":<10}', 'escolha1', default=True), sg.Radio(f'{" IMPAR"}', 'escolha1')],
    [sg.Text('Digite seu número aqui: '), sg.Input(size=(9, 1), key='usu_number')],
    [sg.Button(f'{"START":^44}', key='start')],        
    # [sg.Output(size=(30, 5))]
]
# janela
janela = sg.Window('PAR OU IMPAR', layout)

# ler eventos 
cont = 0
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if escolha1 == 'PAR':
        usu_choose = 'PAR'
        pc_choose = 'IMPAR'
    elif escolha1 == 'IMPAR':
        usu_choose = 'IMPAR'
        pc_choose = 'PAR'

    pc_number = randint(0, 10)
    # usu_number = valores['usu_number']
    sum = valores['usu_number'] + pc_number
    if sum % 2 == 0:
        result = 'PAR'
    else:
        result = 'IMPAR'
    if eventos == 'START':
        sg.popup('popup')
        print(f'A soma foi: {sum} ({result})')
        print(f'Sua escolha: {usu_choose}')
        print(f'Escolha do PC: {pc_choose}')
        if usu_choose == result:
            print(f'\033[1m{"GANHOU, JOGUE NOVAMENTE!":^25}\033[m')
            cont += 1
        else:
            print(f'\033[1;31;40m{"PERDEU OTARIO!":^25}\033[m')
        print(f'Voce escolhe o numero {usu_number}')
        print(f'PC escolhe o numero: {pc_number}') 
    print(f'Voce GANHOU {cont} vezes.')      
