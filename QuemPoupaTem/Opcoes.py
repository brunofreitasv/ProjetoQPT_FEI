from DAL.Clientes import Clientes
from DAL.Contas import Contas
from DAL.Transacoes import Transacoes
from Util.Utilitarios import Utilitarios
import keyboard

class Opcoes(object):
    def __init__(self, option):
        self.__function = {
                            1 : self.__cria_cliente,
                            2 : self.__apaga_cliente,
                            3 : self.__debita,
                            4 : self.__deposita,
                            5 : self.__mostra_saldo,
                            6 : self.__gera_extrato
                          }[option]

    def execute_action(self):
        print("\n" * 100 + "Pressione Enter para iniciar...")
        keyboard.wait('enter', True)

        while True:
            for i in range(30): keyboard.send('backspace')
            keyboard.stash_state()

            if(self.__function()):
                print("Pressione [Enter] para retornar ao menu principal!")
                keyboard.wait('enter', True)
                return
            else:
                print("Pressione [s] para tentar novamente e [Esc] para retornar ao menu principal!")
                while True:
                    if keyboard.is_pressed('esc'): return
                    elif keyboard.is_pressed('s'): 
                        print("\n"*100)
                        break

    def __cria_cliente(self):
        cpf = input("Digite o CPF: ")
        if Utilitarios.valida_cpf(cpf):
            if Clientes.existe(cpf):
                print("CPF existente, verifique se o dado inserido está correto ou tente outra opção!\n")
            else:
                nome = input("Digite o nome completo: ")

                isfloat, saldo = Utilitarios.valida_float(input("Digite o saldo inicial da conta: "))
                if isfloat:
                    senha = input("Insira uma senha: ")
                    tipo = Utilitarios.seleciona_tipo_conta()

                    if(Utilitarios.confirma()):
                        Clientes.add_cliente(cpf , nome, senha)
                        Contas.add_conta(cpf, tipo, saldo)

                        print("\n" * 100 + "Novo cliente criado com sucesso!\n")
                        return True
        return False

    def __apaga_cliente(self):
        cpf_valido, cpf = self.__getCPF()
        if(cpf_valido and Utilitarios.confirma()):
            Clientes.apaga_cliente(cpf)
            Contas.apaga_conta(cpf)
            Transacoes.apaga_historico(cpf)

            print("\n" * 100 + "Cliente apagado com sucesso!\n")
            return True
        return False

    def __debita(self):
        cpf_valido, cpf = self.__getCPF()
        if(cpf_valido):
            isfloat, valor = Utilitarios.valida_float(input("Qual valor deseja debitar da conta? "))
            if isfloat:
                senha = input("Insira a senha: ")
                if Clientes.verifica_senha(cpf, senha):
                    tipo = Contas.busca_tipo_conta(cpf)
                    saldo_atual = Contas.busca_saldo(cpf)

                    trans_valida, n_saldo, tarif = Utilitarios.calcula_novo_saldo_tarifa(tipo, saldo_atual, valor)

                    if(trans_valida and Utilitarios.confirma()):
                        Contas.atualiza_saldo(cpf, n_saldo)
                        Transacoes.add_transacao(cpf, valor, tarif, n_saldo)

                        print("\n"*100 + "O valor foi debitado da conta!\n")
                        return True
                else:
                    print("\nSenha incorreta!\n")
        return False

    def __deposita(self):
        cpf_valido, cpf = self.__getCPF()
        if(cpf_valido):
            isfloat, valor = Utilitarios.valida_float(input("Qual valor deseja depositar na conta? "))
            if isfloat and Utilitarios.confirma():
                saldo_atual = Contas.busca_saldo(cpf)
                n_saldo = round(saldo_atual + valor, 2)

                Contas.atualiza_saldo(cpf, n_saldo)
                Transacoes.add_transacao(cpf, valor, 0, n_saldo)

                print("\n"*100 + "O valor foi depositado na conta!\n")
                return True
        return False

    def __mostra_saldo(self):
        sucesso = False
        cpf_valido, cpf = self.__getCPF()
        if(cpf_valido):
            senha = input("Insira a senha: ")
            if Clientes.verifica_senha(cpf, senha):
                print("\n"*100 + "O saldo da conta é igual a R${:.2f}\n".format(Contas.busca_saldo(cpf)))
                return True
            else:
                print("\nSenha incorreta!\n")
        return False

    def __gera_extrato(self):
        cpf_valido, cpf = self.__getCPF()
        if(cpf_valido):
            senha = input("Insira a senha: ")
            if Clientes.verifica_senha(cpf, senha):
                Utilitarios.mostra_extrato(cpf, 
                            Clientes.busca_nome(cpf),
                            Contas.busca_tipo_conta(cpf),
                            Transacoes.busca_historico(cpf))
                return True
            else:
                print("\nSenha incorreta!\n")
        return False

    def __getCPF(self):
        cpf = input("Digite o CPF: ")
        if not Clientes.existe(cpf):
            print("\n" * 100 + "CPF não encontrado!\n")
            return False, None
        return True, cpf