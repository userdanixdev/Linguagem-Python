# Aprovando empréstimo:

# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

# Versões 1,2,3.
# POO: Versão 1

class Emprestimo_Casa:
    def __init__(self):
        self.casa = 0.0
        self.salario = 0.0
        self.anos = 0
        self.pay = 0
        self.valor_casa = 0
        self.tempo = 0
                

    def versao_1(self):
        self.casa=float(input('Valor da casa: R$ '))
        self.salario=float(input('Salario do comprador: R$ '))
        self.anos=int(input('Quantos anos de financiamento? '))
        prestacao=self.casa/(self.anos*12)
        minimo=self.salario*30/100
        print(f'Para pagar uma casa de R${self.casa:.2f} em {self.anos} anos,')
        print(f'A prestação será de R${prestacao:.2f} ou seja, acima de 30% do seu salário : ')
        if prestacao <= minimo:
            print('Emprestimo pode ser concedido.')
        else:
            print('Empréstimo Negado.')

    def versao_2(self):
        self.pay=int(input('Qual o salario? R$'))
        self.valor_casa=int(input('Qual o valor da casa financiada? R$? '))
        self.tempo=int(input('Em quantos vai pagar? '))
        pay_30=self.pay*0.3
        total_juros=self.valor_casa*(1+0.03)**self.tempo
        prestacao=total_juros/(self.tempo*12)
        if pay_30>=prestacao:
            print('Financiamento aprovado')
            print(f'Você irá pagar R${prestacao:.2f}por mês.')
            print(f'Total do financiamento: R$ {total_juros:.2f}')
        else:
            print('Financiamento não aprovado, mensalidade superior a 30% do salario.')
        print('Fim\n')

    def versao_3(self):
        casa_=int(input('Qual será o valor da casa? '))
        pay_=int(input('Qual será o salário? '))
        ano_=int(input('Quantos anos dispostos a pagar? '))
        prestacao_=casa_/(ano_*12)
        if prestacao_ > pay_*0.3:
            print('Seu emprestimo foi negado.')
        elif prestacao_ < pay_*0.3:
            print('Seu emprestimo foi aprovado.')
        print(f'Para financiar uma casa de R${casa_:.2f}em {ano_} anos..')
        print(f' A prestacao sera de R$ {prestacao_:.2f}')

    def iniciar(self):
        print('Versão1')
        self.versao_1()
        print('versao_02')
        self.versao_2()
        print('versao_03')
        self.versao_3()
        print('fim')


if __name__=='__main__':
    emprestimo=Emprestimo_Casa()
    emprestimo.iniciar()
    
        
        
        
        
        


