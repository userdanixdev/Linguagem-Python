

#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com
#a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
#sabendo que o calculo para encontrar o IMC é: imc = (peso / altura ** 2)

print('Calculo de IMC = Índice de massa corporal ')
peso=float(input('Digite o peso da pessoa: '))
altura=float(input('Digite a altura da mesma pessoa: '))           
imc=peso/(altura **2)
if imc<18.5:
    print(f'Abaixo do peso.Por que seu IMC é: {imc:.1f}.')
if imc>=18.6 and imc<=25:
    print(f'Peso ideal. Por que seu IMC é: {imc:.1f}. ')
if imc>26 and imc<=30:
    print(f'SOBREPESO. Por que seu IMC é: {imc:.1f}. ')
if imc>=31 and imc<=40:
    print(f'OBESIDADE. Por que seu IMC é: {imc:.1f}. ')
if imc>41:
    print(f'OBESIDADE MÓRBIDA. Por que seu IMC é:{imc:.1f}. ')
print('Fim')

