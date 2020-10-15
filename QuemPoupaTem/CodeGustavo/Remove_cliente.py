# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 14:44:57 2020

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

def apaga_cliente(dic_cl, dic_co, dic_ex, cpf):
    del dic_cl[cpf]
    del dic_co[cpf]
    del dic_ex[cpf] 
    
while (True):   
    cpf = input("Digite o CPF: ")
    if verifica_cpf(dic_cliente, cpf):
        apaga_cliente(dic_cliente, dic_conta, dic_extrato, cpf)
        break
    else:
        print("CPF não encontrado, insira um CPF existente ou abra uma conta")
            