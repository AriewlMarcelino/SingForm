import sqlite3

class SQliteBancoDeDados():
    def __init__(self):
        # Cria o banco de dados
        self.banco = sqlite3.connect('bd_formulario_de_cadastro.db')
        self.cursor = self.banco.cursor()

    def criar_banco(self):
        try:
            # Cria a tabela
            self.cursor.execute("CREATE TABLE tabela_formulario_de_cadastro (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, cpf INTEGER, endereco TEXT, email TEXT)")
            print(f'Tabela criada com sucesso.')
            # Grava a tabela criada em nosso banco de dados:
            self.banco.commit()
        except sqlite3.Error as erro:
            #Se por algum motivo no execultar ou der algum erro exiba o seguinte:
            print(f'Tabela não foi criada ! {erro}')
        finally:
            self.banco.close()

# SQliteBancoDeDados().criar_banco()

