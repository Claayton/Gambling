import buttons
from PySimpleGUI import PySimpleGUI as sg
from games.jokenpo import jokenpo
from games.dado import dado
from games.parouimpar import parouimpar
from recordes import recordes
from funçoes import gravar_nome_do_ultimo_player, ler_nome_do_ultimo_player

# -------------------------------------------------------------------------
# Janela inicial


def janela_inicio():
    WIN_W = 650
    WIN_H = 450
    bgcolor = '#272828'
    ccolor = 'black'

    sg.theme('DarkBlue14')
    layout = [
        [sg.Text('Digite aqui seu nome:', size=(18, 1), font=("Helvetica", 15), background_color = bgcolor, text_color='white', key='nome'),
        sg.Input(size=(19, 1), font=("Helvetica", 20), background_color = '#2f3030', text_color='white', do_not_clear=False, key='input'),
        sg.Button('Salvar', size=(18, 1), key='Salvar')],   
        [sg.Text('☒', size=(WIN_W, 1), font=("Helvetica", 8), background_color = bgcolor, text_color='red', key='gravado',justification='right')],    
        [sg.Canvas(background_color=ccolor, size=(650, 10), pad=None)],
        [sg.Text('TESTE SUA SORTE', size=(26, 1), font=('Dyuthi', 50), background_color = bgcolor, text_color='white', justification='center')],    
        [sg.Canvas(background_color=ccolor, size=(650, 10), pad=None)],
        [sg.Text('       JOKENPÔ           PAR OU ÍMPAR            DADO          ', size=(50, 1), font=('Dyuthi', 20), background_color = bgcolor, text_color='white')],
        [sg.Canvas(background_color=ccolor, size=(650, 10), pad=None)],    
        [sg.Canvas(background_color=bgcolor, size=(20, 150), pad=None),
        sg.Button('', image_data=buttons.button_jokenpo, key='JOKENPO', button_color=(sg.theme_background_color('#4f4f4f'), sg.theme_background_color('#4f4f4f')), border_width=0.5),
        sg.Canvas(background_color=bgcolor, size=(30, 150), pad=None), 
        sg.Button('', image_data=buttons.button_poui64, key='PAROUIMPAR', button_color=(sg.theme_background_color('#4f4f4f'), sg.theme_background_color('#4f4f4f')), border_width=0.5),
        sg.Canvas(background_color=bgcolor, size=(30, 150), pad=None), 
        sg.Button('', image_data=buttons.button_dado64, key='DADO', button_color=(sg.theme_background_color('#4f4f4f'), sg.theme_background_color('#4f4f4f')), border_width=0.5),
        sg.Canvas(background_color=bgcolor, size=(20, 150), pad=None)],
        [sg.Canvas(background_color=ccolor, size=(650, 10), pad=None)],
        [sg.Canvas(background_color=bgcolor, size=(455, 25), pad=None), sg.Button('recordes', size=(18, 1), key='recordes')],
        ] 

    return sg.Window('Gambling',
    location=(350, 150),
    size=(WIN_W, WIN_H),
    layout=layout,
    resizable=True,
    return_keyboard_events=True,
    finalize=True,
    titlebar_icon= 'imagens/icon_main.png',
    icon= 'imagens/icon_main.png',
    background_color = bgcolor)


# -------------------------------------------------------------------------
# Criar as janelas iniciais

janela01, janela02, janela03, janela04, janela05 = janela_inicio(), None, None, None, None

# -------------------------------------------------------------------------

# Criar loop para leitura de eventos 

while True:
    window, event, valores = sg.read_all_windows(timeout=1)
    if window == janela01 and event in (sg.WIN_CLOSED, 'Cancel'):
        gravar_nome_do_ultimo_player(nome='')
        break
    if window == janela01 and event in ('Salvar'):
        nome_do_jogador = str(valores['input']).capitalize()
        gravar_nome_do_ultimo_player(nome=nome_do_jogador)
        window['gravado'].update(f'Boa Sorte {ler_nome_do_ultimo_player():}!', text_color='green')
    if window == janela01 and event == 'JOKENPO':
        window['gravado'].update(f'Boa Sorte {ler_nome_do_ultimo_player():}!', text_color='green')
        nome_do_jogador = str(valores['input']).capitalize()
        gravar_nome_do_ultimo_player(nome=nome_do_jogador)
        janela01.Hide()
        janela02 = jokenpo()
        janela01.UnHide()
    if window == janela01 and  event == 'PAROUIMPAR':
        window['gravado'].update(f'Boa Sorte {ler_nome_do_ultimo_player():}!', text_color='green')
        nome_do_jogador = str(valores['input']).capitalize()
        gravar_nome_do_ultimo_player(nome=nome_do_jogador)
        janela01.Hide()
        janela03 = parouimpar()
        janela01.UnHide()
    if window == janela01 and event == 'DADO':
        window['gravado'].update(f'Boa Sorte {ler_nome_do_ultimo_player():}!', text_color='green')
        nome_do_jogador = str(valores['input']).capitalize()
        gravar_nome_do_ultimo_player(nome=nome_do_jogador)
        janela01.Hide()
        janela04 = dado()
        janela01.UnHide()
    if window == janela01 and event == 'recordes':
        janela01.Hide()
        janela05 = recordes()
        janela01.UnHide()
window.close()
