# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:58:51 2020

@author: gustavo
"""
import datetime

dic_cliente = {
    }
dic_extrato = {'47463318800': {0 : ""}
    }
dic_conta = {'47463318800' : {'Tipoconta': 'Salário', 'Saldo': 1000}
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

def deb_saldo(dic_co, cpf, saldo):
    va=[]
    for c, v in dic_co[cpf].items():
        va.append(v)
    if va[0] == "Salário":
        s=float(va[1])
        tf=float(saldo)*0.05
        sa=s-float(saldo)*1.05
        
        if sa<0:
            sa=s
            print("Saldo da conta não pode ser inferior a R$0,00")
        else:
            dic_co[cpf]={'Tipo de conta' : va[0], 'Saldo' : sa}
            v=[]
            v.append(sa)
            v.append(tf)
            return v
        
    elif va[0] == "Comum":
        s=float(va[1])
        print(s)
        tf=float(saldo)*0.03
        sa=s-float(saldo)*1.03
       
        if sa<-500:
            sa=s
            print("Saldo da conta não pode ser inferior a R$-500,00")
        else:
            dic_co[cpf]={'Tipo de conta' : va[0], 'Saldo' : sa}
            v=[]
            v.append(sa)
            v.append(tf)
            return v
       
    if va[0] == "Plus":
        s=float(va[1])
        print(s)
        tf=float(saldo)*0.01
        sa=s-float(saldo)*1.01
       
        if sa<-5000:
            sa=s
            print("Saldo da conta não pode ser inferior a R$-5000,00")
        else:
            dic_co[cpf]={'Tipo de conta' : va[0], 'Saldo' : sa}
            v=[]
            v.append(sa)
            v.append(tf)
            return v
    
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
        saldo = input("Qual valor deseja  de sua conta? ")
        senha = input("Insira sua senha ")
        if verifica_senha(dic_cliente, senha):
            s=deb_saldo(dic_conta, cpf, saldo)
            add_extrato(dic_extrato, cpf, saldo, s)
            print(dic_extrato)
            break
        else:
            print("Senha incorreta")
    else:
        print("CPF não encontrado, insira um CPF existente ou abra uma conta")
