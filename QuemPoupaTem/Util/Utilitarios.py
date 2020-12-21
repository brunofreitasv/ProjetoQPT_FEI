import keyboard
from datetime import datetime
                                                                                    
class Utilitarios(object):                                                          
                                                                                    
    tipos_conta = { 1:"Salário", 2:"Comum", 3:"Plus" }                              
                                                                                    
    @staticmethod                                                                   
    def seleciona_tipo_conta():                                                     
        print("\nSelecione o tipo de conta e pressione a tecla correspondente:")    
        for key, value in Utilitarios.tipos_conta.items():                          
            print("    {0} - {1}     ".format(key, value))                          
        print("\n")                                                                 
                                                                                    
        selected = -1                                                               
        while selected not in [1, 2, 3]:                                            
            if keyboard.is_pressed('1'): selected = 1                               
            elif keyboard.is_pressed('2'): selected = 2                             
            elif keyboard.is_pressed('3'): selected = 3                             
        keyboard.stash_state()                                                      
                                                                                    
        tipo = Utilitarios.tipos_conta[selected]                                    
        print("Tipo: %s" % tipo)                                                    
                                                                                    
        return tipo                                                                 
                                                                                    
    @staticmethod                                                                   
    def confirma():                                                                 
        print("\nConfirma a operação? [y / n]\n")                                   
             
        while True:                                                                 
            if keyboard.is_pressed('y'):                                            
                keyboard.stash_state()                                              
                return True                                                         
            elif keyboard.is_pressed('n'):                                          
                keyboard.stash_state()                                              
                return False                                                        
                                                                                    
    @staticmethod                                                                   
    def calcula_novo_saldo_tarifa(tipo_conta, saldo, valor):                        
                                                                                    
        fator = {                                                                   
                   Utilitarios.tipos_conta[1] : 0.05,                               
                   Utilitarios.tipos_conta[2] : 0.03,                               
                   Utilitarios.tipos_conta[3] : 0.01                                
                }[tipo_conta]                                                       
                                                                                    
        limite = {                                                                  
                   Utilitarios.tipos_conta[1] : 0.00,                               
                   Utilitarios.tipos_conta[2] : -500.00,                            
                   Utilitarios.tipos_conta[3] : -5000.00                            
                 }[tipo_conta]                                                      
                                                                                    
        tarifa = round(valor*fator, 2)                                              
        novo_saldo = round(saldo - valor*(1 + fator), 2)                            
                                                                                    
        if novo_saldo < limite:                                                     
            print("\n{0}\nSaldo da conta não pode ficar inferior a R${1:.2f}\n"     
                  .format("Falha ao debitar! Saldo insuficiente!", limite))         
            return False, None, None                                                
                                                                                    
        return True, novo_saldo, tarifa                                             
                                                                                    
    @staticmethod                                                                   
    def getTime():                                                                  
        return datetime.today().strftime("%d/%m/%Y %I:%M:%S %p")                    
                                                                                    
    @staticmethod                                                                   
    def valida_cpf(cpf):                                                            
        if not cpf.isdecimal() or len(cpf) != 11:                                   
            print("\nCPF inválido! Deve conter apenas números e 11 digitos!\n")     
            return False                                                            
        return True                                                                 
                                                                                    
    @staticmethod                                                                   
    def valida_float(string):                                                       
        try:                                                                        
            return True, float(string)                                              
        except ValueError:                                                          
            print("\nValor inválido! Deve ser um número decimal!\n")                
            return False, None                                                      
                                                                                    
    @staticmethod                                                                   
    def mostra_extrato(cpf, nome, tipo_conta, historico):                           
                                                                                    
        print("\n" * 100)                                                           
        print("Nome:   {0}".format(nome))                                           
        print("CPF:    {0}".format(cpf))                                            
        print("Conta:  {0}".format(tipo_conta))                                     
                                                                                    
        for k, v in sorted(historico.items()):                                      
            print("Data: %-25s   %-1s​ %-10.2f​  ​​ Tarifa: %-10.2f​  Saldo: %-10.2f​" %  
                  (v['Data'],v['Sinal'],v['Valor'],v['Tarifa'],v['Saldo']))         
                                                                                    
        print("\n")                                                                 