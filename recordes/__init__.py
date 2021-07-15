def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def gravar_nome_do_ultimo_player(nome):
    arquivo = 'recordes/nome_atual.txt'
    if not arquivoexiste(arquivo):
        criararquivo('recordes/nome_atual.txt')
    try:
        with open (arquivo, 'w') as nomes:
            nomes.write(nome)
    except:
        print('Houve um erro no salvamento do nome do jogador')
    

def ler_nome_do_ultimo_player():
    arquivo = 'recordes/nome_atual.txt'
    try:
        with open (arquivo, "rt") as nomes:
            for c in nomes:
                nome = c
        return nome            
    except:
        return ''


"""def lerarquivo(nome):
    from time import sleep
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        print('Pessoas Cadastradas')
        sleep(1)
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:_<30}{dado[1]:_>5} anos')
    finally:
        a.close()"""


def dados_do_jogador(nome=ler_nome_do_ultimo_player(), pontuação=['Jokenpô', 'ParouÍmpar', 'Dado']):
    jogador = nome
    if jogador == '':
        jogador = 'Default'
    NovoRecorde = [jogador, pontuação]
    return NovoRecorde


def cadastrar_recorde(arquivo, jogador=dados_do_jogador()):
    arquivo = 'recordes/recorde.txt'
    if not arquivoexiste(arquivo):
        criararquivo('recordes/recorde.txt')
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{jogador[0]};{jogador[1]}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo recorde de {jogador} cadastrado!')
            a.close()
