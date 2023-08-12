#Imagine um sistema de caixa eletrônico. Construa um programa que receba a senha de um correntista para validação do sistema de acesso.
#As restrições:
    #1.Quando a senha estiver correta, mostrar a mensagem: Olá, 'o nome'. Seja bem-vindo ao nosso banco!
    #2.Quando o usuário errar a senha pela primeira vez,mostrar a mensagem: Senha incorreta! Vc tem duas tentativas.
    #3.Se o usuário errar a senha pela segunda vez, mostrar a mensagem: Senha incorreta! Vc tem ainda uma tentativa
    #4.Se o usuário mostrar a senha novamente, mostrar a mensagem 'Sua senha foi bloqueada'

print('Olá, seja bem vindo ao BANCO DO DANIEL.')
erros = 0
while erros<3:
    senha=float(input('Por favor insira sua senha: '))
    if senha== 123456:
        print('Senha correta! Seja bem vindo ao banco.')
        break
    else:
        erros = erros + 1
        if erros <3:
        #if erros == erros:
           print(f'Senha incorreta! Vc tem {3 -  erros} tentativas.')
        else:
            print('''
            Seu senha foi bloqueada! Por favor, dirija-se a uma
                  de nossas agências.''')

Result:

Olá, seja bem vindo ao BANCO DO DANIEL.
Por favor insira sua senha: 4565
Senha incorreta! Vc tem 2 tentativas.
Por favor insira sua senha: 456
Senha incorreta! Vc tem 1 tentativas.
Por favor insira sua senha: 4565
Seu senha foi bloqueada! Por favor, dirija-se a uma
                  de nossas agências.





