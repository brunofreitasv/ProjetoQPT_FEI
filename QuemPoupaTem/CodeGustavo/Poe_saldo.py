# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:49:30 2020

@author: gustavo
"""
import datetime

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

def poe_saldo(dic_co, cpf, saldo):
    l=[]
    s=dic_co[cpf]['Saldo']
    s=s+saldo
    dic_co[cpf]['Saldo']=s
    l.append(s)
    l.append(0)
    return l
        
def add_extrato(dic_ex, cpf, saldo, sa):
    tarifa=sa[1]
    valor=sa[0]
    contador=0
    for c, v in dic_ex[cpf].items():
        contador = int(c)+1
    del dic_ex[cpf][0]
    if tarifa==0:
        data = datetime.datetime.today()
        data = data.strftime("%m/%d/%Y %I:%M:%S %p")
        dic_ex[cpf][contador] = { 'Data' : str(data) , '+' : saldo, 'Tarifa' : tarifa, 'Saldo' : valor}
    else:
        data = datetime.datetime.today()
        data = data.strftime("%m/%d/%Y %I:%M:%S %p")
        dic_ex[cpf][contador] = { 'Data' : str(data) , '-' : saldo, 'Tarifa' : tarifa, 'Saldo' : valor}
    
    
while (True):  
    cpf = input("Digite o CPF: ") 
    if verifica_cpf(dic_cliente, cpf):
        saldo = float(input("Qual valor deseja adicionar a sua conta? "))
        s=poe_saldo(dic_conta, cpf, saldo)
        add_extrato(dic_extrato, cpf, saldo, s)
        print(dic_conta)
        print(dic_extrato)
        break
    else:
        print("CPF não encontrado, insira um CPF existente ou abra uma conta")
    