from AtualizaUsuarios import AtualizarUsuarios
from CadastroUsuarios import CadastrarUsuario
from ExcluirUsuarios import ExcluirUsuario
from ListarUsuarios import ListarUsuarios
import os


class Interface():

  def __init__(self):
    self.interface()

  
  def interface(self):
    while True:
      print('\n' * os.get_terminal_size().lines)
      print('-'*25)
      print(f'| Sistema de Formulario |')
      print('-'*25)

      print(f'1 - Adicionar Usuario')
      print(f'2 - Atualizar Usuario')
      print(f'3 - Deletar Usuario')
      print(f'4 - Listar Usuarios')
      print(f'0 - Sair')

      try:
        escolha = int(input('Escolha uma das opções acima: '))
        if escolha == 0:
          print('Saindo do sistema...')
          print('\n' * os.get_terminal_size().lines)
          break
        elif escolha == 1:
          os.system('cls')
          CadastrarUsuario.cadastrar_usuario(CadastrarUsuario())
          while True:
            try:
              escolha_usuario = input('Deseja adicionar mais algums usuario(s/n)?:')
              if escolha_usuario == 's':
                os.system('cls')
                CadastrarUsuario.cadastrar_usuario(CadastrarUsuario())
                os.system('cls')
                break
              elif escolha_usuario == 'n':
                os.system('cls')
                escolha
                break
            except:
                print(f'Escolha uma opção disponivél ! {escolha}')
                break
            finally:
              escolha
              break
          
        elif escolha == 2:
          return AtualizarUsuarios.atualizar_usuarios(AtualizarUsuarios())
        elif escolha == 3:
          return ExcluirUsuario.excluir_usuario(ExcluirUsuario())
        elif escolha == 4:
         os.system('cls')
         return ListarUsuarios.listar_usuarios(ListarUsuarios())
      except ValueError:
        print('Opção invalida! Tente as opções numericas !')
        print('Saindo do sistema...')

        break

Interface()

