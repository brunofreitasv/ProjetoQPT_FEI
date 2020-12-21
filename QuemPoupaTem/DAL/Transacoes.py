from DAL.DataAccess import DataAccess                                                     
from Util.Utilitarios import Utilitarios                                                  
                                                                                          
class Transacoes:                                                                         
    class __Transacoes(DataAccess):                                                       
        def __init__(self):                                                               
            super().__init__('Transacoes.txt')                                            
                                                                                          
    __instance = None                                                                     
                                                                                          
    def __init__(self):                                                                   
        if not Transacoes.__instance:                                                     
            Transacoes.__instance = Transacoes.__Transacoes()                             
                                                                                          
    def __loadDatabase(func):                                                             
        def decorated(*args, **kwargs):                                                   
            Transacoes()                                                                  
            Transacoes.__instance.loadData()                                              
            res = func(*args, **kwargs)                                                   
            Transacoes.__instance.saveChanges()                                           
            return res                                                                    
        return decorated                                                                  
                                                                                          
    @staticmethod                                                                         
    @__loadDatabase                                            
    def add_transacao(cpf, valor, tarifa, saldo_atual):                                   
        count = 1                                                                         
        if cpf in Transacoes.__instance.dataBase:                                         
            count = int(max(Transacoes.__instance.dataBase[cpf], key=int)) + 1            
        else:                                                                             
            Transacoes.__instance.dataBase[cpf] = {}                                      
                                                                                          
        multiplicador = '+' if tarifa == 0 else '-'                                       
                                                                                          
        Transacoes.__instance.dataBase[cpf][count] = {  'Data'   : Utilitarios.getTime(), 
                                                        'Sinal'  : multiplicador,         
                                                        'Valor'  : valor,                 
                                                        'Tarifa' : tarifa,                
                                                        'Saldo'  : saldo_atual  }         
                                                                                          
    @staticmethod                                                                         
    @__loadDatabase                                           
    def apaga_historico(cpf):                                                             
        Transacoes.__instance.dataBase.pop(cpf, None)                                     
                                                                                          
    @staticmethod                                                                         
    @__loadDatabase                                            
    def busca_historico(cpf):                                                             
        return Transacoes.__instance.dataBase[cpf]                                        
                                                                                          
                                                                                          