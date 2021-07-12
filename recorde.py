def bancodedadosonline(nome):
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


def lerarquivo(nome):
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
        a.close()


def cadastrar(arquivo, nome='defaut', pontuação=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{pontuação}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo recorde de {nome}!')
            a.close()


def recorde(jogador):
    recorde = 'recorde.txt'
    if not bancodedadosonline(recorde):
        criararquivo('recorde.txt')
        cadastrar(jogador)