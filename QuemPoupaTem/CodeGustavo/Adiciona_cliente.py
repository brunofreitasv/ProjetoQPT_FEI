# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:35:42 2020

@author: gustavo
"""

dic_cliente = {
    }
dic_conta = {
    }
dic_extrato = {
    }

# Gustavo
def verifica_cpf(dic, cpf): # Subrotina que verifica se o CPF inserido esta 
                            # correto. Os informados são o dicionario do 
                            # cliente e o CPF
    for i in dic.keys():    # Pega na chave do dicionario o CPF do cliente
        if cpf in i:        # Verifica o CPF do dicionario com o CPF informado
            return True     # caso exista o CPF a subrotina retorna True caso
    return False            # contrario retorna False

def add_cliente(dic_cl, cpf, senha, nome):
    dic_cl[cpf] = {'Nome' : nome, 'Senha' : senha}

def add_conta(dic_co, cpf, tc, saldo):
    dic_co[cpf] = { 'Tipo de conta' : tc, 'Saldo' : saldo}

def add_extrato(dic_ex, cpf):
    dic_ex[cpf]= {0:""}
    
    
while (True):  
    nome = input("Digite seu nome completo: ")
    cpf = input("Digite o CPF: ")
    if verifica_cpf(dic_cliente, cpf):
        print("CPF existente, verifica se o dado inserido está correto ou tente outra opção")
    else:
        tipo_conta = input("Qual conta deseja abrir? ")
        saldo = input("Qual o saldo inicial de sua conta? ")
        senha = input("Insira uma senha ")
        add_cliente(dic_cliente, cpf, senha, nome)
        add_conta(dic_conta, cpf, tipo_conta, saldo)
        add_extrato(dic_extrato, cpf)
        print(dic_cliente)
        print(dic_conta)
    