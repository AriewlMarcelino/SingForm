# import sqlite3

# class ExcluirTabela(SQliteBancoDeDados):
#       def __init__(self):
#         super().__init__()
#         self.banco = sqlite3.connect('bd_formulario_de_cadastro.db')
#         self.cursor = self.banco.cursor()

#       def exluir_tabela(self):
#         try:
#           self.cursor.execute('DROP TABLE IF EXISTS bd_formulario_de_cadastro')
#           self.banco.commit()
#           print('Tabela Excluida com sucesso !')
#         except sqlite3.Error as erro:
#           print(f'Erro ao excluir tabela.{erro}')
#         finally:
#           self.banco.close()

# excluir_tabela = ExcluirTabela()
# excluir_tabela.exluir_tabela()