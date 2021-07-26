from funçoes import atualizar_recordes, consulta_dados


def jokenpo():
    from PySimpleGUI import PySimpleGUI as sg
    from random import choice
    import buttons
    from funçoes import consulta_nome

    p1escolha = ''
    pcescolha = ''
    result = ''
    possibilidades = ['PEDRA', 'PAPEL', 'TESOURA']
    placar_pc = 0
    placar_player = 0
    nome = consulta_nome()
    win_w = 650
    win_h = 450
    bg_color = '#4f4f4f'

    # layout
    def jokenpo_inicio():

        sg.theme('DarkBlue14')

        global placar_pc, placar_player
        placar_pc = 0
        placar_player = 0

        layout = [
            [sg.Canvas(background_color=bg_color, size=(650, 20))],
            [sg.Canvas(background_color='#272828', size=(650, 10))],
            [sg.Canvas(background_color=bg_color, size=(650, 10))],
            [sg.Text(f'{f"Olá {nome}":^90}', font=('Dyuthi', 35), background_color=bg_color, justification='c')],
            [sg.Text(f'{"FAÇA A SUA ESCOLHA":^100}', font=('Dyuthi', 35), background_color=bg_color, justification='c')],
            [sg.Canvas(background_color=bg_color, size=(650, 10))],
            [sg.Canvas(background_color='#272828', size=(650, 10))],
            [sg.Canvas(background_color=bg_color, size=(60, 150)),
                sg.Button('', image_data=buttons.button_pedra64, key='PEDRA', button_color=(sg.theme_background_color('#4f4f4f'), sg.theme_background_color('#4f4f4f')), border_width=0.5),
                sg.Canvas(background_color=bg_color, size=(61, 150)),
                sg.Button('', image_data=buttons.button_papel64, key='PAPEL', button_color=(sg.theme_background_color('#4f4f4f'), sg.theme_background_color('#4f4f4f')), border_width=0.5),
                sg.Canvas(background_color=bg_color, size=(61, 150)),
                sg.Button('', image_data=buttons.button_tesoura64, key='TESOURA', button_color=(sg.theme_background_color('#4f4f4f'), sg.theme_background_color('#4f4f4f')), border_width=0.5),
                sg.Canvas(background_color=bg_color, size=(60, 150))],
            [sg.Canvas(background_color='#272828', size=(650, 10))],
            [sg.Canvas(background_color=bg_color, size=(650, 10))],
            [sg.Text(f'Placar PC: {placar_pc}', size=(24, 1), font=('Dyuthi', 16), background_color=bg_color, justification='left', key='placar_pc'),
                sg.Text(f'Placar do Player: {placar_player}', size=(24, 1), font=('Dyuthi', 16), background_color=bg_color, justification='left', key='placar_player')]
        ]

        # janela
        return sg.Window('JOKENPÔ',
                         location=(350, 150),
                         layout=layout,
                         background_color='#4F4F4F',
                         icon='imagens/jokenpo/icon_jokenpo.png',
                         size=(win_w, win_h),
                         finalize=True)

    def jogar():
        while True:
            for i in range(19000):
                sg.popup_animated(
                    gif,
                    location=(350, 190),
                    no_titlebar=True,
                    time_between_frames=100,
                    background_color='#4F4F4F')
            break
        return sg.popup_animated(None)

    def mostrar_resultado(nome='Player'):
        jogar()
        if nome == 'Default' or nome == '':
            nome = 'Player'

        sg.theme('DarkBlue14')
        layout = [
            [sg.Canvas(background_color=bg_color, size=(650, 10))],
            [sg.Text(f'{result}', size=(26, 1), font=('Dyuthi', 50), background_color='#4F4F4F', text_color='white', justification='center')],
            [sg.Image(png, background_color='#4F4F4F')],
            [sg.Canvas(background_color=bg_color, size=(650, 20))],
            [sg.Text(f'PC', size=(13, 2), font=('Dyuthi', 30), background_color=bg_color, justification='center'),
                sg.Text(f'{nome}', size=(13, 2), font=('Dyuthi', 30), background_color=bg_color, justification='center')],
            [sg.Button(f'{"Cancel":^}', key='Cancel', size=(41, 3)),
                sg.Button(f'{"JOGAR NOVAMENTE":^}', key='JOGAR', size=(41, 3))]
            ]

        return sg.Window('Jokenpo',
                         location=(350, 150),
                         size=(win_w, win_h),
                         layout=layout,
                         resizable=True,
                         return_keyboard_events=True,
                         finalize=True,
                         background_color='#4F4F4F',
                         margins=(0, 0),
                         no_titlebar=True)

    # Criar as janelas iniciais
    janela01, janela02 = jokenpo_inicio(), None

    # ler eventos 
    empates = 0
    tentativas = 0
    while True:
        window, eventos, values = sg.read_all_windows(timeout=1)
        if window == janela01 and eventos in (sg.WIN_CLOSED, 'Cancel'):
            break
        if window == janela01 and eventos == 'PEDRA':
            p1escolha = 'PEDRA'
        elif window == janela01 and eventos == 'PAPEL':
            p1escolha = 'PAPEL'
        elif window == janela01 and eventos == 'TESOURA':
            p1escolha = 'TESOURA' 

        pcescolha = choice(possibilidades)
        
        if pcescolha == 'PEDRA' and p1escolha == 'PEDRA':
            gif = 'imagens/jokenpo/jokenpo_gif/pedra_pedra.gif'
            png = 'imagens/jokenpo/jokenpo_png/pedra_pedra_result.png'
            result = 'Empate'
        elif pcescolha == 'PAPEL' and p1escolha == 'PAPEL':
            gif = 'imagens/jokenpo/jokenpo_gif/papel_papel.gif'
            png = 'imagens/jokenpo/jokenpo_png/papel_papel_result.png'
            result = 'Empate'
        elif pcescolha == 'TESOURA' and p1escolha == 'TESOURA':
            gif = 'imagens/jokenpo/jokenpo_gif/tesoura_tesoura.gif'
            png = 'imagens/jokenpo/jokenpo_png/tesoura_tesoura_result.png'
            result = 'Empate'
        
        elif pcescolha == 'PEDRA' and p1escolha == 'TESOURA':
            gif = 'imagens/jokenpo/jokenpo_gif/pedra_tesoura.gif'
            png = 'imagens/jokenpo/jokenpo_png/pedra_tesoura_result.png'
            result = 'Perdeu'
        elif pcescolha == 'PAPEL' and p1escolha == 'PEDRA':
            gif = 'imagens/jokenpo/jokenpo_gif/papel_pedra.gif'
            png = 'imagens/jokenpo/jokenpo_png/papel_pedra_result.png'
            result = 'Perdeu'
        elif pcescolha == 'TESOURA' and p1escolha == 'PAPEL':
            gif = 'imagens/jokenpo/jokenpo_gif/tesoura_papel.gif'
            png = 'imagens/jokenpo/jokenpo_png/tesoura_papel_result.png'
            result = 'Perdeu'

        elif pcescolha == 'PEDRA' and p1escolha == 'PAPEL':
            gif = 'imagens/jokenpo/jokenpo_gif/pedra_papel.gif'
            png = 'imagens/jokenpo/jokenpo_png/pedra_papel_result.png'
            result = 'Venceu'
        elif pcescolha == 'PAPEL' and p1escolha == 'TESOURA':
            gif = 'imagens/jokenpo/jokenpo_gif/papel_tesoura.gif'
            png = 'imagens/jokenpo/jokenpo_png/papel_tesoura_result.png'
            result = 'Venceu'
        elif pcescolha == 'TESOURA' and p1escolha == 'PEDRA':
            gif = 'imagens/jokenpo/jokenpo_gif/tesoura_pedra.gif'
            png = 'imagens/jokenpo/jokenpo_png/tesoura_pedra_result.png'
            result = 'Venceu'

        if window == janela01 and eventos in ('PEDRA', 'PAPEL', 'TESOURA'):
            tentativas += 1
            janela01.Hide()
            janela02 = mostrar_resultado(nome)
            if result == 'Perdeu':
                placar_pc += 1
                window['placar_pc'].update(f'Placar PC: {placar_pc}')
            elif result == 'Venceu':
                placar_player += 1
                window['placar_player'].update(f'Placar Player: {placar_player}')
            elif result == 'Empate':
                empates += 1
            media = (placar_player * 100) / tentativas

        if window == janela02 and eventos == 'JOGAR':
            janela02.Hide()
            janela01.UnHide()
        if window == janela02 and eventos in (sg.WIN_CLOSED, 'Cancel'):
            if media > consulta_dados(classificacao='ouro')[6]:
                atualizar_recordes(nome=consulta_dados(classificacao='prata')[1],
                                   vitorias=consulta_dados(classificacao='prata')[2],
                                   empates=consulta_dados(classificacao='prata')[3],
                                   derrotas=consulta_dados(classificacao='prata')[4],
                                   total=consulta_dados(classificacao='prata')[5],
                                   media=consulta_dados(classificacao='prata')[6],
                                   classificacao='bronze')
                atualizar_recordes(nome=consulta_dados(classificacao='ouro')[1],
                                   vitorias=consulta_dados(classificacao='ouro')[2],
                                   empates=consulta_dados(classificacao='ouro')[3],
                                   derrotas=consulta_dados(classificacao='ouro')[4],
                                   total=consulta_dados(classificacao='ouro')[5],
                                   media=consulta_dados(classificacao='ouro')[6],
                                   classificacao='prata')
                atualizar_recordes(nome=consulta_nome(),
                                   vitorias=placar_player,
                                   empates=empates,
                                   derrotas=placar_pc,
                                   total=tentativas,
                                   media=media,
                                   classificacao='ouro')
            elif media > consulta_dados(classificacao='prata')[6]:
                atualizar_recordes(nome=consulta_dados(classificacao='prata')[1],
                                   vitorias=consulta_dados(classificacao='prata')[2],
                                   empates=consulta_dados(classificacao='prata')[3],
                                   derrotas=consulta_dados(classificacao='prata')[4],
                                   total=consulta_dados(classificacao='prata')[5],
                                   media=consulta_dados(classificacao='prata')[6],
                                   classificacao='bronze')
                atualizar_recordes(nome=consulta_nome(),
                                   vitorias=placar_player,
                                   empates=empates,
                                   derrotas=placar_pc,
                                   total=tentativas,
                                   media=media,
                                   classificacao='prata')
            elif media > consulta_dados()[6]:
                atualizar_recordes(nome=consulta_nome(),
                                   vitorias=placar_player,
                                   empates=empates,
                                   derrotas=placar_pc,
                                   total=tentativas,
                                   media=media,
                                   classificacao='bronze')
            break
    window.Close()
