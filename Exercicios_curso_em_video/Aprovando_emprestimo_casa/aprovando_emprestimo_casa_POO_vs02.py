# Aprovando empréstimo bancário para financiamento
# Versão 02 POO: Validações do dados inseridos pelo usuário, tratamento de erros, títulos para cada versão.


class Emprestimo_Casa:
    def __init__(self):
        self.casa = 0.0
        self.salario = 0.0
        self.anos = 0
        self.pay = 0
        self.valor_casa = 0
        self.tempo = 0
                

    def versao_1(self):
        while True:
            try:
                self.casa=float(input('Valor da casa: R$ '))
                if self.casa >= 100000:
                    break
                else:
                    print('Por favor, insira um valor mínimo de R$ 100.000.')
            except ValueError:
                print('Por favor, insira um valor número válido.')
        while True:
            try:
                self.salario=float(input('Salario do comprador: R$ '))
                if self.salario <= 20000:
                    break
                else:
                    print('Por favor,insira um valor máximo de R$ 20.000,00.')
            except ValueError:
                print('Por favor, insira um valor numérico válido.')
        while True:
            try:
                self.anos=int(input('Quantos anos de financiamento? '))
                if self.anos <= 30:
                    break
                else:
                    print('Por favor, número máximo de financiamento é de 30 anos.')
            except ValueError:
                print('Por favor, insira valores inteiros.')
        prestacao=self.casa/(self.anos*12)
        minimo=self.salario*30/100
        print(f'\nPara pagar uma casa de R${self.casa:.2f} em {self.anos} anos,')
        print(f'A prestação será de R${prestacao:.2f}.')
        if prestacao <= minimo:
            print('Emprestimo Concedido.')
        else:
            print('Empréstimo Negado. Salário acima de 30% do seu salário')

    def versao_2(self):
        while True:
            try:
                self.pay=int(input('Qual o salario? R$'))
                if self.pay <= 20000:
                    break
                else:
                    print('Por favor, insira um valor máximo de R$ 20.000,00.')
            except ValueError:
                print('Por favor, insira números válidos.')
        while True:
            try:
                self.valor_casa=int(input('Qual o valor da casa financiada? R$? '))
                if self.valor_casa >= 100000:
                    break
                else:
                    print('Por favor, insira um valor mínimo de R$ 100.000,00.')
            except ValueError:
                print('Por favor, insira números válidos.')
        while True:
            try:
                self.tempo=int(input('Em quantos anos vai pagar? '))
                if self.tempo <= 30:
                    break
                else:
                    print('Por favor, número máximo de financiamento é de 30 anos.')
            except ValueError:
                print('Por favor, insira números válidos.')
        pay_30=self.pay*0.3
        total_juros=self.valor_casa*(1+0.03)**self.tempo  # Juros
        prestacao=total_juros/(self.tempo*12)
        if pay_30>=prestacao:
            print('Financiamento aprovado')
            print(f'Você irá pagar R${prestacao:.2f}por mês.')
            print(f'Total do financiamento: R$ {total_juros:.2f}')
        else:
            print('Financiamento não aprovado, mensalidade superior a 30% do salario.')
        print('Fim\n')

    def versao_3(self):
        while True:
            try:                
                casa_=int(input('Qual será o valor da casa? '))
                if casa_ >= 100000:
                    break
                else:
                    print('Por favor, insira um valor mínimo de R$ 100.000,00.')
            except ValueError:
                print('Por favor,insira números válidos.')
        while True:
            try:
                pay_=int(input('Qual será o salário? '))
                if pay_ <= 20000:
                    break
                else:
                    print('Por favor, teto máximo salarial de R$ 20.000,00.')
            except ValueError:
                print('Insira números válidos.')
        while True:
            try:
                ano_=int(input('Quantos anos dispostos a pagar? '))
                if ano_ <= 30:
                    break
                else:
                    print('Número máximo de financiamento é de 30 anos.')
            except ValueError:
                print('Insira números válidos.')                    
        prestacao_=casa_/(ano_*12)
        if prestacao_ > pay_*0.3:
            print('Seu emprestimo foi negado.')
        elif prestacao_ < pay_*0.3:
            print('Seu emprestimo foi aprovado.')
        print(f'Para financiar uma casa de R${casa_:.2f} em {ano_} anos..')
        print(f' A prestação será de R$ {prestacao_:.2f} reais.')

    def iniciar(self):
        print(f'{"+"*50}\n{"Versão 01: Financiamento ":^49}\n{"+"*50}')
        self.versao_1()
        print(f'{"+"*50}\n{"Versão 02: Financiamento: Com juros ":^49}\n{"+"*50}')
        self.versao_2()
        print(f'{"+"*50}\n{"Versão 03: Financiamento ":^49}\n{"+"*50}')
        self.versao_3()
        print('fim')


if __name__=='__main__':
    emprestimo=Emprestimo_Casa()
    emprestimo.iniciar()
    
        
        
        
        
        
