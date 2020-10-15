# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 21:07:24 2020

@author: gustavo
"""

dic_cliente = {'47463318800':{'Nome': 'Gustavo Benevenuto de Oliveira',
                              'Senha':'qawsed22'}
    }
dic_conta = {'47463318800':{ 'Conta': 'Salário', 'Saldo': 1000.00}}
dic_extrato = {'47463318800': {1 : {'Data': '22/02/2020 - 17:30', 
                                    '-': 200, 'Tarifa': '10.00', 
                                    'Saldo': 794.85},
                               2 : {'Data': '15/03/2020 - 8:00', 
                                    '+': 1000, 'Tarifa': '0.00', 
                                    'Saldo': 1794.85}}
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

def mostra_extrato(dic_cl, dic_co, dic_ex, cpf): # Subrotina que mostra o
                                                 # extrato da conta do cliente
                                                 # Os dados passados são o 
                                                 # dicionario do cliente, o
                                                 # dicionario da conta, o
                                                 # dicionario do extrato e o 
                                                 # CPF
    print(f"""Nome: {dic_cl[cpf]['Nome']}        
CPF: {cpf}
Conta: {dic_co[cpf]['Conta']}""", end="\n")      # Essa função imprime o nome
                                                 # o CPF e o tipo de conta do
                                                 # cliente
    for c, v in dic_ex[cpf].items():             # 
        for ch, va, in dic_ex[cpf][c].items():
            if ch == "Data":
                print(f"{ch}: {va} ", end=" ")
            elif ch =="-" or ch=="+":
                print(f"{ch}  {va} ", end=" ")
            elif ch =="Tarifa":
                print(f"{ch}: {va} ", end=" ")
            else:
                print(f"{ch}: {va}", end="\n")
    
while (True):  
    cpf = input("Digite o CPF: ") 
    if verifica_cpf(dic_cliente, cpf):
        senha = input("Insira sua senha ")
        if verifica_senha(dic_cliente, senha):
            mostra_extrato(dic_cliente, dic_conta, dic_extrato, cpf)
            break
        else:
            print("Senha incorreta")
    else:
        print("CPF não encontrado, insira um CPF existente ou abra uma conta")