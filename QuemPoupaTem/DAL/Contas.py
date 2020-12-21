#Toda a lógica e desenvolvimento foi feito em conjunto pelos dois membros da dupla

from DAL.DataAccess import DataAccess                                                       
                                                                                            
class Contas:                                                                               
    class __Contas(DataAccess):                                                             
        def __init__(self):                                                                 
            super().__init__('Contas.txt')                                                  
                                                                                            
    __instance = None                                                                       
                                                                                            
    def __init__(self):                                                                     
        if not Contas.__instance:                                                           
            Contas.__instance = Contas.__Contas()                                           
                                                                                            
    def __loadDatabase(func):                                                               
        def decorated(*args, **kwargs):                                                     
            Contas()                                                                        
            Contas.__instance.loadData()                                                    
            res = func(*args, **kwargs)                                                     
            Contas.__instance.saveChanges()                                                 
            return res                                                                      
        return decorated                                                                    
                                                                                            
    @staticmethod                                                                           
    @__loadDatabase                                                 
    def add_conta(cpf, tipo, saldo_inicial):                                                
        Contas.__instance.dataBase[cpf] = {'Tipo de conta' : tipo, 'Saldo' : saldo_inicial} 

    @staticmethod                                                                           
    @__loadDatabase                                                  
    def apaga_conta(cpf):                                                                   
        Contas.__instance.dataBase.pop(cpf, None)                                           

    @staticmethod                                                                           
    @__loadDatabase                                                  
    def busca_tipo_conta(cpf):                                                              
        return Contas.__instance.dataBase[cpf]["Tipo de conta"]                             

    @staticmethod                                                                           
    @__loadDatabase                                                  
    def busca_saldo(cpf):                                                                   
        return Contas.__instance.dataBase[cpf]["Saldo"]                                     
                                                                                            
    @staticmethod                                                                           
    @__loadDatabase                                                 
    def atualiza_saldo(cpf, saldo):                                                         
        Contas.__instance.dataBase[cpf]["Saldo"] = saldo                                    
                                                                                            


