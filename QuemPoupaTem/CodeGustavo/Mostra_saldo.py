# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 20:59:13 2020

@author: gustavo
"""

dic_cliente = {
    }
dic_extrato = {'47463318800': {0 : ""}
    }
dic_conta = {'47463318800' : {'Tipoconta': 'Saláro', 'Saldo': 1000}
    }

# Gustavo
def verifica_cpf(dic, cpf): # Subrotina que verifica se o CPF inserido esta 
                            # correto. Os informados são o dicionario do 
                            # cliente e o CPF
    for i in dic.keys():    # Pega na chave do dicionario o CPF do cliente
        if cpf in i:        # Verifica o CPF do dicionario com o CPF informado
            return True     # caso exista o CPF a subrotina retorna True caso
    return False            # contrario retorna False

# Gustavo
def verifica_senha(dic, senha): # Subrotina que verifica se a senha iserida
                                # esta correta. Os dados inforamdos são o 
                                # dicionario do cliente e a senha
    i = dic[cpf]['Senha']       # Pega a senha no dicionario do cliente
    if senha in i:              # Verifica se a senha informada é igual a
        return True             # senha inserida. Caso verdadeiro retorna True
    return False                # caso falso retorna False

def mostra_saldo(dic_co, cpf):
    print(f"Seu saldo é igual a R${dic_co[cpf]['Saldo']}")

    
    
while (True):  
    cpf = input("Digite o CPF: ") 
    if verifica_cpf(dic_cliente, cpf):
        senha = input("Insira sua senha ")
        if verifica_senha(dic_cliente, senha):
            mostra_saldo(dic_conta, cpf)
            break
        else:
            print("Senha incorreta")
    else:
        print("CPF não encontrado, insira um CPF existente ou abra uma conta")