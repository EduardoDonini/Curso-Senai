print('E-commerce X')
nome = input('Digite seu nome: ')
usuario = input('Digite seu usuario: ')
email = input('Digite seu e-mail: ')
senha = input('Digite seu senha: ')

print('olá', nome, 'seu usuário é ', usuario)

senha_dig = input('Senha: ')
usuario_dig = input('Usuário: ')

if  senha_dig == senha and usuario_dig == usuario: 
    print('Seja bem vindo(a)', nome, 'faça seu pedido:')
    menu = {
     'camiseta': 150.00,
     'meia': 50.00,
     'computador': 20.000,
     'fone': 100.00

    }
    print('produtos: ', menu )
    
    meus_produtos  = []
    total_pagar  = []
    pedido1 = input('digite o produto')
    pedido2 = input('digite o produto')
    pedido3 = input('digite o produto')
    
    meus_produtos +=(pedido1, pedido2, pedido3)
    total_pagar  += [menu[pedido1], menu[pedido2], menu[pedido3]]

    print('SEUS PEDIDOS:')
    print(meus_produtos)
    print(total_pagar)
    
    soma =  sum(total_pagar)
    float(soma)
    print('TOTAL DA COMPRA:')
    print('R$', soma)

    forma_pag = input('''
    ESCOLHA A FORMA DE PAGAMENTO:
    1 -  PIX
    2 - CC
    3 - PAYPALL
       
    ''')

    if forma_pag == '1':
        print('Seu pagamento foi efetuado com PIX: R$ ', soma )
    elif forma_pag == '2':
        print('Seu pagamento foi efetuado com CC: R$ ', soma )
    elif forma_pag == '3':
        print('Seu pagamento foi efetuado com PYPALL: R$ ', soma )   
    else: 
        print('digite algo valido')    

else: 
    print('Algo foi digitado errado')    




sair  =  input('digite enterpara sair')
