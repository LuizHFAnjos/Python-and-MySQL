import mysql.connector

def conectar():
    try:
        conexao = mysql.connector.connect(
            host='Localhost',
            user='root',
            password='',
            database='escola'
        )
        return conexao
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None

def menu_principal():
    print('-' * 50)
    print('       Cadastro de Alunos Escola VSCODE')
    print('-' * 50)
    print('(1) Cadastrar alunos')
    print('(2) Alunos Cadastrados')
    print('(3) Editar aluno')
    print('(4) Deletar aluno')
    print('(5) Sair')
    return int(input('R = '))

def cadastrar_aluno(conexao):
    nome = input('Nome do aluno: ')
    serie = input('Série do aluno: ')
    
    try:
        cursor = conexao.cursor()
        comando = f'INSERT INTO alunos (nome, serie) VALUES ("{nome}", "{serie}")'
        cursor.execute(comando)
        conexao.commit()
        print('ALUNO CADASTRADO!')
    except mysql.connector.Error as err:
        print(f"Erro ao cadastrar aluno: {err}")
    finally:
        cursor.close()

def listar_alunos(conexao):
    try:
        cursor = conexao.cursor()
        comando = 'SELECT * FROM alunos ORDER BY matricula'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        
        for matricula, nome, serie in resultado:
            print(f'Matricula: {matricula:<3} | Nome: {nome:<10} | Série: {serie}')
    except mysql.connector.Error as err:
        print(f"Erro ao listar alunos: {err}")
    finally:
        cursor.close()

def editar_aluno(conexao):
    matricula = int(input('Digite a matricula do aluno: '))
    serie = input('Nova série do aluno: ')

    try:
        cursor = conexao.cursor()
        comando = f'UPDATE alunos SET serie = "{serie}" WHERE matricula = {matricula}'
        cursor.execute(comando)
        conexao.commit()
        print('ALUNO ATUALIZADO!')
    except mysql.connector.Error as err:
        print(f"Erro ao editar aluno: {err}")
    finally:
        cursor.close()

def deletar_aluno(conexao):
    delete_ma = int(input('Informe a matricula do aluno que deseja excluir da lista: '))
    
    try:
        cursor = conexao.cursor()
        comando = f'DELETE FROM alunos WHERE matricula = {delete_ma}'
        cursor.execute(comando)
        conexao.commit()
        print('ALUNO DELETADO!')
    except mysql.connector.Error as err:
        print(f"Erro ao deletar aluno: {err}")
    finally:
        cursor.close()

def main():
    conexao = conectar()
    
    if not conexao:
        return
    
    while True:
        opcao = menu_principal()
        
        if opcao == 1:
            cadastrar_aluno(conexao)
        elif opcao == 2:
            listar_alunos(conexao)
        elif opcao == 3:
            editar_aluno(conexao)
        elif opcao == 4:
            deletar_aluno(conexao)
        elif opcao == 5:
            print('Encerrando programa...')
            break
        else:
            print('Opção inválida!')

    conexao.close()

if __name__ == '__main__':
    main()
