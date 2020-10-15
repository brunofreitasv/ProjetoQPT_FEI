from DAL.DataAccess import DataAccess

class Clientes:
     class __Clientes(DataAccess):
        def __init__(self):
            super().__init__('Clientes.txt')

     __instance = None
     
     def __init__(self):
         if not Clientes.__instance:
             Clientes.__instance = Clientes.__Clientes()
     
     def __loadDatabase(func):
         def decorated(*args, **kwargs):
             Clientes()
             Clientes.__instance.loadData()
             res = func(*args, **kwargs)
             Clientes.__instance.saveChanges()
             return res
         return decorated

     @staticmethod
     @__loadDatabase
     def add_cliente(cpf, nome, senha):
         Clientes.__instance.dataBase[cpf] = {'Nome' : nome, 'Senha' : senha}

     @staticmethod
     @__loadDatabase
     def apaga_cliente(cpf):
         Clientes.__instance.dataBase.pop(cpf, None)

     @staticmethod
     @__loadDatabase
     def existe(cpf):                                                # Subrotina que verifica se o CPF inserido existe na base de clientes. A chave é o CPF.
         return cpf in Clientes.__instance.dataBase                  # Retorna True se o cpf informado existe nas chaves da base caso contratio retorna False.
                                                                     
     @staticmethod                                                   
     @__loadDatabase                                                 
     def verifica_senha(cpf, senha):                                 # Subrotina que busca a senha na base de clientes.
         senha_db = Clientes.__instance.dataBase[cpf]['Senha']       # Pega a senha no dicionario do cliente.
         return senha == senha_db

     @staticmethod
     @__loadDatabase
     def busca_nome(cpf):
         return Clientes.__instance.dataBase[cpf]["Nome"]
    
             