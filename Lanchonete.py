print('Bem Vindo a Lanchonete da Mayara Santos de Castro')

print('******************Cardápio****************')
print('| Código |       Descrição       | Valor |')
print('|   100  |    Cachorro Quente    | 09,00 |')
print('|   101  | Cachorro Quente Duplo | 11,00 |')
print('|   102  |         X-Egg         | 12,00 |')
print('|   103  |        X-Salada       | 12,00 |')
print('|   104  |        X-Bacon        | 14,00 |')
print('|   105  |         X-Tudo        | 17,00 |')
print('|   200  |   Refrigerante Lata   | 05,00 |')
print('|   201  |      Chá Gelado       | 04,00 |')
print('******************************************')

acumulador = 0 #Variável para pedidos acrescentados

while True: #Iniciando loop infinito para não ter limite de pedidos
    codigo = input('Entre com o código desejado: ')
    if codigo != '100' and codigo != '101' and codigo != '102' and codigo != '103' and codigo != '104' and codigo != '105' and codigo != '200' and codigo != '201':
        print('Operação Inválida. Digite códigos existentes no cardápio!')
        continue #Caso digitado um código fora do cardápio o programa coloca a informação de operação inválida e pede novamente que seja digitado código desejado.

    if codigo == '100': #Pedindo Cachorro Quente
        print('Você pediu um Cachorro Quente no valor de R$9,00.')
        acumulador = acumulador + 9 #caso seja acrescentado ao pedido
    elif codigo == '101': #Pedindo Cachorro Quente Duplo
        print('Você pediu um Cachorro Quente Duplo no valor de R$11,00.')
        acumulador = acumulador + 11 #caso seja acrescentado ao pedido
    elif codigo == '102': #Pedindo X-Egg
        print('Você pediu um X-Egg no valor de R$12,00.')
        acumulador = acumulador + 12 #caso seja acrescentado ao pedido
    elif codigo == '103': #Pedindo X-Salada
        print('Você pediu um X-Salada no valor de R$12,00.')
        acumulador = acumulador + 12 #caso seja acrescentado ao pedido
    elif codigo == '104': #Pedindo X-Bacon
        print('Você pediu um X-Bacon no valor de R$14,00.')
        acumulador = acumulador + 14 #caso seja acrescentado ao pedido
    elif codigo == '105': #Pedindo X-Tudo
        print('Você pediu um X-Tudo no valor de R$17,00.')
        acumulador = acumulador + 17 #caso seja acrescentado ao pedido
    elif codigo == '200': #Pedindo Refrigerante Lata
        print('Você pediu um Refrigerante Lata no valor de R$5,00.')
        acumulador = acumulador + 5 #caso seja acrescentado ao pedido
    elif codigo == '201': #Pedindo Chá Gelado
        print('Você pediu um Chá Gelado no valor de R$4,00.')
        acumulador = acumulador + 4 #caso seja acrescentado ao pedido
    #Menu com a opção para fazer mais algum pedido.
    pedido = int(input('Desejapedir mais alguma coisa? '
'''
[1] Sim 
[2] Não
 >>> '''))
    if pedido != 1 and pedido != 2: #Caso no menu seja digitado algo diferente de 1 e 2
        print('Operação Inválida.') #Saida do sistema e na sequência abre o menu novamente
        pedido = int(input('Desejapedir mais alguma coisa? '
'''
[1] Sim 
[2] Não
>>> '''))
    if pedido == 1: #Caso digite 1 no menu, volta para digitar código desejado.
        continue
    else:
        pedido == 2
        print('O valor total do seu pedido: R$ {:.2f}'.format(acumulador))
        break
