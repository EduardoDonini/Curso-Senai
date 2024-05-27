print ("\n")
print ("-----------Seja bem-vindo ao seu banco digital-----------")
print ("\n")

saldo = int()
limite = 500



senha = [2,1,0]
for n  in senha:
    acesso  = input('Digite sua senha >>')
    if acesso  != '1234':
        print('Negado')
        if n  == 0:
            print('Chances esgotadas, entre em contato com o banco!', n) 
    else:
        print('Autorizado')
        
        print ("\n")
        print ("Qual operação deseja realizar?")
        op = input ("[1]-Saque \n[2]-Depósito \n[3]-Saldo\n")
        if op == "1":
            saque = int(input("Quanto deseja sacar?\n"))
            if saque > (limite):
                print("Saque não autorizado.")
            if saque > (saldo):
                print("Saque não autorizado.")
            # else:
            #         print(f"Seu saque de {saque} foi autorizado. Seu saldo agora é de {saldo - saque}.\n")
        if op == "2":
            deposito = int(input("Quanto deseja depositar?\n"))
            print(f"Seu depósito de {deposito} foi concluído. Seu saldo agora é de {saldo + deposito}.\n")
            saldo = saldo + deposito
        if op == "3":
            print(f"Seu saldo é de {saldo}.\n")
            
        while True:
            print("Deseja realizar outra operação?\n")
            quest = input("[1]-Sim  \n[2]-Não \n")
            if quest == "2":
                print("Obrigado, até logo!")
                break
            if quest == "1":
                print ("Qual operação deseja realizar?\n")
                op = input ("[1]-Saque \n[2]-Depósito \n[3]-Saldo:\n")
            if op == "1":
                saque = int(input("Quanto deseja sacar?\n"))
                if int(limite) < (saque):
                    print("Saque não autorizado.\n")
                if int(saldo) < (saque):
                    print("Saque não autorizado.\n")
                if int(saldo) >= (saque):
                    print(f"Seu saque de {saque} foi autorizado. Seu saldo agora é de {saldo - saque}. \n")
                    saldo = int(saldo) - int(saque)
            if op == "2":
                deposito = int(input("Quanto deseja depositar?\n"))
                print(f"Seu depósito de {deposito} foi concluído. Seu saldo agora é de {saldo + deposito}. \n")
                saldo = saldo + deposito
            if op == "3":
                print(f"Seu saldo é de {saldo}.\n")
          
        break




    
