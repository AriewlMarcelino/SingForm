import sqlite3
from Banco import SQliteBancoDeDados


class ExcluirUsuario(SQliteBancoDeDados):
    def __init__(self):
        super().__init__()
        self.id = input('Digite o id do usuario que deseja excluir ?')

    def excluir_usuario(self):
      while True:
        print('Insira um id disponivél !')
        self.id = input('Digite o id do usuario que deseja excluir ?')
        try:
          self.cursor.execute('DELETE FROM tabela_formulario_de_cadastro WHERE id = ?', (self.id,))
          self.banco.commit()
          print('Usuario removido com sucesso !')
          break
        except sqlite3.Error as erro:
            print(f'Erro ao excluir usuário: {erro}')
        finally:
            self.banco.close()

# excluir_usuario = ExcluirUsuario()
# excluir_usuario.excluir_usuario()