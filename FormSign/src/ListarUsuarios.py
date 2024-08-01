from Banco import SQliteBancoDeDados
import sqlite3

class ListarUsuarios(SQliteBancoDeDados):
    def __init__(self):
        super().__init__()

    def listar_usuarios(self):
        try:
            print('*'*25)
            print('  Listagem de Usuarios')
            print('*'*25)
            self.cursor.execute("SELECT * FROM tabela_formulario_de_cadastro")
            for i in self.cursor.fetchall():
                print(f'\nId: {i[0]}')
                print(f'Nome: {i[1]}')
                print(f'CPF: {i[2]}')
                print(f'Endereço: {i[3]}')
                print(f'Email: {i[4]}\n')
            print('*'*25)
        except sqlite3.Error as erro:
            print(f'Erro ao listar usuarios: {erro}')
        finally:
            self.banco.close()

listar_usuarios = ListarUsuarios()
listar_usuarios.listar_usuarios()
