print ("\n")
print ("-----------Seja bem-vindo ao seu banco digital-----------")
print ("\n")

saldo = 1000

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
        op = input ("Saque, Depósito, Saldo:")
        if op == "Saque":
            saque = int(input("Quanto deseja sacar?"))
            print(f"Seu saque de {saque} foi autorizado. Seu saldo agora é de {saldo - saque}. ")
        if op == "Depósito":
            deposito = int(input("Quanto deseja depositar?"))
            print(f"Seu depósito de {deposito} foi concluído. Seu saldo agora é de {saldo + deposito}. ")
        if op == "Saldo":
            print(f"Seu saldo é de {saldo}.")

        print("Deseja realizar outra operação?")
        quest = input("[1]-Sim  [2]-Não ")
        if quest == "2":
            print("Até logo!")
        if quest == "1":
            print ("Qual operação deseja realizar?")
            op = input ("Saque, Depósito, Saldo:")
        if op == "Saque":
            saque = int(input("Quanto deseja sacar?"))
            print(f"Seu saque de {saque} foi autorizado. Seu saldo agora é de {saldo - saque}. ")
        if op == "Depósito":
            deposito = int(input("Quanto deseja depositar?"))
            print(f"Seu depósito de {deposito} foi concluído. Seu saldo agora é de {saldo + deposito}. ")
        if op == "Saldo":
            print(f"Seu saldo é de {saldo}.")
          
    break



    