import mysql.connector
from time import sleep

def Conectar():
    try:
        conexao = mysql.connector.connect(
            host='Localhost',
            user='root',
            password='',
            database='mercado'
        )

        return conexao

    except mysql.connector.Error as err:
        print('Erro ao conectar com o banco de Dados!')
        return None
    
def Menu():
    print('-' * 50)
    print('       Mercado Anjos')
    print('-' * 50)
    print('(1)Cadastrar produto')
    print('(2)Listar produtos')
    print('(3)Editar produto')
    print('(4)Deletar produto')
    print('(5)Sair')
    return int(input('R = '))

def Cadastro(conexao):
    nomeP = str(input('Nome do produto: '))
    precoP = float(input('Preço do produto: '))
    descricaoP = str(input('Descrição do Produto: '))

    try:
        cursor = conexao.cursor()
        comando = f'INSERT INTO produtos (nome,preco,descricao) VALUES ("{nomeP}", "{precoP}", "{descricaoP}")'
        cursor.execute(comando)
        conexao.commit()
        print('PRODUTO CADASTRADO')
    except mysql.connector.Error as err:
        print(f'Erro ao cadastrar produto: {err}!')

    finally:
        cursor.close()

def Listar(conexao):
    try:
        cursor = conexao.cursor()
        comando = f'SELECT * FROM produtos'
        cursor.execute(comando)
        resultado = cursor.fetchall()

        for codigo, nomeP,precoP,descricaoP in resultado:
            print(f'Codigo : {codigo:<3} | Nome : {nomeP:<10} | Preço : {precoP:<5} | Descrição : {descricaoP}')

    except mysql.connector.Error as err:
        print(f"Erro ao Listar os produtos: {err}")
    finally:
        cursor.close()

def Editar(conexao):
    id = int(input('Digite o Codigo do Produto: '))

    new_nomeP = str(input('Atualizar Nome: '))
    new_precoP = float(input('Atualizar Preço: '))
    new_descricaoP = str(input('Atualizar Descrição: '))
    try:
        cursor = conexao.cursor()
        comando = f'UPDATE produtos SET nome = "{new_nomeP}", preco = {new_precoP}, descricao = "{new_descricaoP}" WHERE codigo = {id}'
        cursor.execute(comando)
        conexao.commit()
        print('PRODUTO ATUALIZADO!')
    except mysql.connector.Error as err:
        print(f'Erro ao atualizar produto: {err}')
    finally:
        cursor.close()

def Deletar(conexao):
    id = int(input('Digite o Codigo do Produto: '))

    try:
        cursor = conexao.cursor()
        comando = f'DELETE FROM produtos WHERE codigo = "{id}"'
        cursor.execute(comando)
        conexao.commit()
        print('PRODUTO DELETADO!')

    except mysql.connector.Error as err:
        print(f'Erro ao deletar produto: {err}')

    finally:
        cursor.close()


def main():
    conexao = Conectar()

    if not conexao:
        return
    

    while True:
        opcao = Menu()

        if opcao == 1:
            Cadastro(conexao)
        elif opcao == 2:
            Listar(conexao)
        elif opcao == 3:
            Editar(conexao)
        elif opcao == 4:
            Deletar(conexao)
        elif opcao == 5:
            print('Encerrando programa...')
            print('3...')
            sleep(1)
            print('2...')
            sleep(1)
            print('1')
            sleep(1)
            print('PROGRAMA ENCERRADO!')
            break
        else:
            print('OPÇÃO INVÁLIDA!')

    conexao.close()

if __name__=='__main__':
    main()