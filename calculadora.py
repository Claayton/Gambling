# Janela da calculadora
def calculadora():
    from PySimpleGUI import PySimpleGUI as sg
    # layout
    sg.theme('Reddit')
    layout = [

        [sg.Input(size=(20, 2))], 
        [sg.Button(f'{"7":^3}', key='7'), sg.Button(f'{"8":^3}', key='8'), sg.Button(f'{"9":^3}', key='9'), sg.Button(f'{"/":^3}', key='/')],
        [sg.Button(f'{"6":^3}', key='6'), sg.Button(f'{"5":^3}', key='5'), sg.Button(f'{"4":^3}', key='4'), sg.Button(f'{"*":^3}', key='*')],
        [sg.Button(f'{"1":^3}', key='1'), sg.Button(f'{"2":^3}', key='2'), sg.Button(f'{"3":^3}', key='3'), sg.Button(f'{"-":^3}', key='-')],
        [sg.Button(f'{"0":^3}', key='0'), sg.Button(f'{".":^4}', key='.'), sg.Button(f'{"=":^3}', key='='), sg.Button(f'{"+":^3}', key='+')]
    ]
    # janela
    janela = sg.Window('Calculadora', layout)

    # ler eventos 
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
