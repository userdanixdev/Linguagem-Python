#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.


print('Olá, Seja bem vindo ao programa Python!')
print('''Por aqui, vamos calcular a área de uma parede e
      saber quanto de tinta será necessário para pinta-la...''')
lar_parede = float(input('Me informe a largura da parede em metros: '))
alt_parede = float(input('Me informe a altura da parede em metros: '))
area = lar_parede * alt_parede
tinta = area/2
print('A área da sua parede é {} metros quadrados'.format(area))
print('E para pinta-la é necessário {} litros de tinta.'.format(tinta))
print('Obrigado e fim do programa!')


===============================================================================================
