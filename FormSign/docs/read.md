# Sistema de Formulario com SQLite

'''
PSEUDOCODIGO:

1. O usuario vai entrar em um sistema de formulario que vai ter os respectivos campos:
  - Nome completo do usuario
  - CPF do usuario
  - Endereço do usuario
  - Email

2. Nesse Sistema o usuario vai ter algumas opções como:
  - A opção de adicionar usuario (que é o inicio da aplicação)
  - Ele vai ter a opção de atualizar as informações
  - Ele vai poder deletar as informações
  - Listar dados de usuarios cadastrados


CLASSE

- Usuario

SubClasse


ATRIBUTOS NÃO FIXOS(SERIA ATRIBUTOS QUE NÂO SERÂO SETADOS MANUALMENTE):

- nome
- cpf
- endereco
- email



METODOS

- cadastrar()
 - metodo responsavel por cadastrar os usuarios.

- atualizar()
 - metodo responsavel por atualizar as informações dos usuarios cadastrados.

- deletar()
 - metodo responsavel por deletar usuarios cadastrados.

- listar()
  - metodo responsavél pela listagem dos usuarios cadastrados.

- interface()
  - metodo responsavél pelo inicio da aplicação mostrando as opções que o usuario tem dentro do sistema.


TECNOLOGIAS

- Python
- SQLite
- PyQT5

'''


V1.0
- O sistema consegue adicionar remover,editar e atualizar os usuarios no banco de dados

Seção cadastrar:

Bugs a serem resolvidos
- Validar os campos de insersão do usuario com o nome, cpf, endereco e email
 - Para não deixar com que os usuario passem de campo se tive espaço ou se o valor for diferente do campo solicitado.

- Ajustar o campo cpf, para um formato ___.___.___-_

V2.0
Atualização futura Adicionar interface com tkinter 