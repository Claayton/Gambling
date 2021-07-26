# Tabela de dados do nome do jogador:


def inserir_nome(nome_db='Nome.db', nome_tabela='Nomes', nome=None):
    import sqlite3
    from contextlib import closing

    with sqlite3.connect(nome_db) as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {nome_tabela}(
                    id integer not null,
                    nome varchar(30) not null)
                """)
            cursor.execute(f"""
                insert into {nome_tabela}(id, nome)
                    values(?, ?)
                """, ('1', nome,))
        conexao.commit()


def atualizar_nome(nome_db='Nome.db', nome_tabela='Nomes', nome=None):
    nome = nome.title().strip()
    import sqlite3
    from contextlib import closing

    with sqlite3.connect(nome_db) as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute(f"""
                update {nome_tabela}
                    set nome='{nome}'
                    where id='1'""")
        conexao.commit()


def deleta_tabela_nomes(nome_db='Nome.db', nome_tabela='Nomes'):
    import sqlite3
    from contextlib import closing
    try:
        with sqlite3.connect(nome_db) as conexao:
            with closing(conexao.cursor()) as cursor:
                cursor.execute(f"""
                    delete from {nome_tabela}
                        where nome=''""")
            conexao.commit()
    except IndentationError:
        print(f'Não conseguo deletar o Nome com ID: {id}!')


def consulta_nome(nome_db='Nome.db', nome_tabela='Nomes'):
    import sqlite3
    from contextlib import closing

    with sqlite3.connect(nome_db) as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute(f"select * from {nome_tabela} order by id")
            resultado = cursor.fetchall()
    return resultado[0][1]


# Tabela de dados dos recordes:


def arquivo_existe(nome_db='Dados.db'):
    try:
        a = open(nome_db)
        a.close()
        return True
    except FileNotFoundError:
        print('Impossível abrir o arquivo')
        return False


def inserir_recordes(nome_db='Dados.db', nome_tabela='Recordes_jokenpo'):
    import sqlite3
    from contextlib import closing

    with sqlite3.connect(nome_db) as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {nome_tabela}(
                id integer primary key autoincrement not null,
                nome varchar(30) not null,
                vitorias integer,
                empates integer,
                derrotas integer, 
                total integer,
                media integer)""")
            for c in range(0, 3):
                cursor.execute(f"""
                    insert into {nome_tabela}(nome, vitorias, empates, derrotas, total, media)
                    values(?, ?, ?, ?, ?, ?)""",
                               ('Default', '0', '0', '0', '0', '0'))
        conexao.commit()


def atualizar_recordes(nome_db='Dados.db',
                       nome_tabela='Recordes_jokenpo',
                       nome=None,
                       vitorias=None,
                       empates=None,
                       derrotas=None,
                       total=None,
                       media=None,
                       classificacao='ouro'):
    if classificacao == 'ouro':
        classificacao = 1
    elif classificacao == 'prata':
        classificacao = 2
    else:
        classificacao = 3
    if nome == '' or nome is None:
        nome = 'Default'

    import sqlite3
    from contextlib import closing

    with sqlite3.connect(nome_db) as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute(f"""
                update {nome_tabela}
                set nome='{nome}',
                vitorias='{vitorias}',
                empates='{empates}',
                derrotas='{derrotas}',
                total='{total}',
                media='{media}'
                where id = '{classificacao}'""")
        conexao.commit()


def consulta_dados(nome_db='Dados.db', nome_tabela='Recordes_jokenpo', classificacao='ouro'):
    import sqlite3
    from contextlib import closing

    with sqlite3.connect(nome_db) as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute(f"select * from {nome_tabela} order by media desc")
            resultado = cursor.fetchall()
            if classificacao == 'ouro':
                return resultado[0]
            elif classificacao == 'prata':
                return resultado[1]
            elif classificacao == 'bronze':
                return resultado[2]
