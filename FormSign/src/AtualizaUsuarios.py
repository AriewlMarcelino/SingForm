import sqlite3
from CadastroUsuarios import SQliteBancoDeDados

class AtualizarUsuarios(SQliteBancoDeDados):
  def __init__(self):
      super().__init__()
      self.cursor = self.banco.cursor()
      self.id = input('Digite o id do usuario que deseja atualizar ?')
      self.nome = input('Digite seu nome completo: ')
      self.cpf = input('Digite seu CPF: ')
      self.endereco = input('Digite seu endereço: ')
      self.email = input('Digite seu email: ')

  def atualizar_usuarios(self):
    try:
      self.cursor.execute('UPDATE tabela_formulario_de_cadastro SET nome=?, cpf=?, endereco=?, email=? WHERE id=?', (self.nome, self.cpf, self.endereco, self.email,self.id))
      self.banco.commit()
      print('Usuario atualizado com sucesso.')
    except sqlite3.Error as erro:
      print(f'Erro ao atualizar usuário: {erro}')
    finally:
      self.banco.close()



# AtualizarUsuarios().atualizar_usuarios()

