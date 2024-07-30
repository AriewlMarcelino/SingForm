from Banco import SQliteBancoDeDados
import sqlite3

class CadastrarUsuario(SQliteBancoDeDados):
    # Metodos construtor da classe CadastrarUsuario:
    def __init__(self):
        # Super chama a classe mãe e propriedades e atributos:
        super().__init__()
        self.nome = input('Digite seu nome completo: ')
        self.cpf = input('Digite seu CPF: ')
        self.endereco = input('Digite seu endereço: ')
        self.email = input('Digite seu email: ')

    #Metodo que é responsavél por execultar o cadastro do usuario:
    def cadastrar_usuario(self):
        try:
            # Tente inseir na tabela xxxx os seguintes atributos (xxxx,xxx,xxxxxxx,xxxxx) com os seguintes valores (self.xxxx):
            self.cursor.execute('INSERT INTO tabela_formulario_de_cadastro (nome, cpf, endereco, email) VALUES(?,?,?,?)', (self.nome, self.cpf, self.endereco, self.email))
            # Vai enviar as informações a tabela:
            self.banco.commit()
            # Exiba a seguinte mensagem:
            print('Usuário cadastrado com sucesso!\n')
        except sqlite3.Error as erro:
            print(f'Erro ao cadastrar usuário: {erro}')
        finally:
            self.banco.close()

# CadastrarUsuario().cadastrar_usuario()
# Interface().interface()

