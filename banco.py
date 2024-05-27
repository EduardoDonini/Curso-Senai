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
          print('Chances esgotadas, entre em contato com o banco') 
    else:
        print('Autorizado')
        
        print ("\n")
        print ("Qual operação deseja realizar?")
        op = input ("[1]-Saque [2]-Depósito [3]-Saldo:")
        if op == "1":
            saque = int(input("Quanto deseja sacar?"))
            if saque > (limite):
                print("Saque não autorizado.")
            if saque > (saldo):
                print("Saque não autorizado.")
            else:
                print(f"Seu saque de {saque} foi autorizado. Seu saldo agora é de {saldo - saque}. ")
        if op == "2":
            deposito = int(input("Quanto deseja depositar?"))
            print(f"Seu depósito de {deposito} foi concluído. Seu saldo agora é de {saldo + deposito}. ")
            saldo = saldo + deposito
        if op == "3":
            print(f"Seu saldo é de {saldo}.")
            
    while True:
        print("Deseja realizar outra operação?")
        quest = input("[1]-Sim  [2]-Não ")
        if quest == "2":
            print("Obrigado, até logo!")
            break
        if quest == "1":
            print ("Qual operação deseja realizar?")
            op = input ("[1]-Saque [2]-Depósito [3]-Saldo:")
        if op == "1":
            saque = int(input("Quanto deseja sacar?"))
            if saque > (limite):
                print("Saque não autorizado.")
            if saque > (saldo):
                print("Saque não autorizado.")
            else:
                print(f"Seu saque de {saque} foi autorizado. Seu saldo agora é de {saldo - saque}. ")
                saldo = saldo - deposito
        if op == "2":
            deposito = int(input("Quanto deseja depositar?"))
            print(f"Seu depósito de {deposito} foi concluído. Seu saldo agora é de {saldo + deposito}. ")
            saldo = saldo + deposito
        if op == "3":
            print(f"Seu saldo é de {saldo}.")
          
    break




    
