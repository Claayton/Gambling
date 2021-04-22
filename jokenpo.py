def jokenpo():
    from PySimpleGUI import PySimpleGUI as sg
    from random import choice
    from time import sleep
    import buttons

    p1escolha = ''
    pcescolha = ''
    result = ''
    possibilidades = ['PEDRA', 'PAPEL', 'TESOURA']

    # layout
    def jokenpo_inicio():
        sg.theme('DarkBlue14')
        layout = [
            [sg.Text(f'', size=(10,3), background_color = '#4F4F4F'),
            sg.Text(f'\nFAÇA A SUA ESCOLHA', size=(35,3), background_color = '#4F4F4F')],
            [sg.Button('', image_data=buttons.button_pedra64, key='PEDRA', button_color=(sg.theme_background_color('#4f4f4f'), sg.theme_background_color('#4f4f4f')), border_width=0.5),
            sg.Button('', image_data=buttons.button_papel64, key='PAPEL', button_color=(sg.theme_background_color('#4f4f4f'), sg.theme_background_color('#4f4f4f')), border_width=0.5),
            sg.Button('', image_data=buttons.button_tesoura64, key='TESOURA', button_color=(sg.theme_background_color('#4f4f4f'), sg.theme_background_color('#4f4f4f')), border_width=0.5)]
        ]

        # janela
        return sg.Window('JOKENPÔ',
        layout, background_color = '#4F4F4F',
        icon= 'image/icons/icon_jokenpo.png',
        size=(360, 200),
        finalize=True)

    def jogar():
        while True:
            for i in range(20000):
                sg.popup_animated(
                    gif,
                    no_titlebar=True,
                    time_between_frames=100,
                    background_color = '#4F4F4F')
            break
        return sg.popup_animated(None)

    def resultado():
        WIN_W = 80
        WIN_H = 25

        sg.theme('DarkBlue14')
        layout = [
            [sg.Button(f'{"JOGAR NOVAMENTE":^}', key='JOGAR', size=(35,3))],
            [sg.Image(png, background_color = '#4F4F4F')],
            [sg.Button(f'{"Cancel":^}', key='Cancel', size=(35,3))]]

        return sg.Window('Jokenpo',
        layout=layout,
        resizable=True,
        return_keyboard_events=True,
        finalize=True,
        background_color='#4F4F4F',
        margins=(0,0),
        no_titlebar=True)

    # Criar as janelas iniciais
    janela01, janela02 = jokenpo_inicio(), None

    # ler eventos 
    while True:
        window, eventos, values = sg.read_all_windows(timeout=1)
        if window == janela01 and eventos in (sg.WIN_CLOSED, 'Cancel'):
            break
        
        if window == janela01 and eventos == 'PEDRA' :
            p1escolha = 'PEDRA'
        elif window == janela01 and eventos == 'PAPEL':
            p1escolha = 'PAPEL'
        elif window == janela01 and eventos == 'TESOURA':
            p1escolha = 'TESOURA' 

        pcescolha = choice(possibilidades)
        
        if pcescolha == 'PEDRA' and p1escolha == 'PEDRA':
            gif = 'image/jokenpo_gif/pedra_pedra.gif'
            png = 'image/jokenpo_png/pedra_pedra_result.png'
            result = 'Empate'
        elif pcescolha == 'PAPEL' and p1escolha == 'PAPEL':
            gif = 'image/jokenpo_gif/papel_papel.gif'
            png = 'image/jokenpo_png/papel_papel_result.png'
            result = 'Empate'
        elif pcescolha == 'TESOURA' and p1escolha == 'TESOURA':
            gif = 'image/jokenpo_gif/tesoura_tesoura.gif'
            png = 'image/jokenpo_png/tesoura_tesoura_result.png'
            result = 'Empate'
        
        elif pcescolha == 'PEDRA' and p1escolha == 'TESOURA':
            gif = 'image/jokenpo_gif/pedra_tesoura.gif'
            png = 'image/jokenpo_png/pedra_tesoura_result.png'
            result = 'Venceu'
        elif pcescolha == 'PAPEL' and p1escolha == 'PEDRA':
            gif = 'image/jokenpo_gif/papel_pedra.gif'
            png = 'image/jokenpo_png/papel_pedra_result.png'
            result = 'Venceu'
        elif pcescolha == 'TESOURA' and p1escolha == 'PAPEL':
            gif = 'image/jokenpo_gif/tesoura_papel.gif'
            png = 'image/jokenpo_png/tesoura_papel_result.png'
            result = 'Venceu'

        elif pcescolha == 'PEDRA' and p1escolha == 'PAPEL':
            gif = 'image/jokenpo_gif/pedra_papel.gif'
            png = 'image/jokenpo_png/pedra_papel_result.png'
            result = 'Perdeu'
        elif pcescolha == 'PAPEL' and p1escolha == 'TESOURA':
            gif = 'image/jokenpo_gif/papel_tesoura.gif'
            png = 'image/jokenpo_png/papel_tesoura_result.png'
            result = 'Perdeu'
        elif pcescolha == 'TESOURA' and p1escolha == 'PEDRA':
            gif = 'image/jokenpo_gif/tesoura_pedra.gif'
            png = 'image/jokenpo_png/tesoura_pedra_result.png'
            result = 'Perdeu'

        if window == janela01 and eventos in ('PEDRA', 'PAPEL', 'TESOURA'):
            janela01.Hide()
            jogar()
            janela02 = resultado()
        if window == janela02 and eventos == 'JOGAR':
            janela02.Hide()
            janela01.UnHide()
        if window == janela02 and eventos in (sg.WIN_CLOSED, 'Cancel'):
            break
    window.Close()

    