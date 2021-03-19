# def parouimpar(): 
from PySimpleGUI import PySimpleGUI as sg
from random import randint

# layout
sg.theme('Reddit')
layout = [
    [sg.Text('Voce escolhe PAR ou IMPAR?')],
    [sg.Checkbox('PAR', key='PAR')], [sg.Checkbox('IMPAR', key='IMPAR')], 
    [sg.Text('Digite seu número aqui: ')], [sg.Input(key='usu_number')],
    [sg.Button(f'{"START":^46}', key='start')],        
    [sg.Output(size=(33, 6))]
]
# janela
janela = sg.Window('PAR OU IMPAR', layout)

# ler eventos 
cont = 0
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    while True:
        if eventos == 'par':
            usu_choose = 'PAR'
            pc_choose = 'IMPAR'
        elif eventos == 'impar':
            usu_choose = 'IMPAR'
            pc_choose = 'PAR'

        pc_number = randint(0, 10)
        sum = valores['usu_number'] + pc_number
        if sum % 2 == 0:
            result = 'PAR'
        else:
            result = 'IMPAR'
        print(f'A soma foi: \033[32m{sum}\033[m (\033[32m{result}\033[m)')
        print(f'\033[mSua escolha: \033[32m{usu_choose}\033[m\nEscolha do PC: \033[32m{pc_choose}\033[m')
        print(f'\033[40m{" ":^25}\033[m')
        if usu_choose == result:
            print(f'\033[1;32;40m{"GANHOU, JOGUE NOVAMENTE!":^25}\033[m')
            cont += 1
        else:
            print(f'\033[1;31;40m{"PERDEU OTARIO!":^25}\033[m')
        print(f'\033[mVoce escolhe o numero \033[32mmmmmmmm{usu_number}\nPC escolhe o numero: \033[32m{pc_number}\033[m') 
    print(f'\033[32mVoce GANHOU {cont} vezes.\033[m')  
