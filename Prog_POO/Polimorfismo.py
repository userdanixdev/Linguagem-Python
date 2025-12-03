# Polimorfismo:

#Como o polimorfismo se encaixa com herança. A palavra polimorfismo significa ter muitas formas. 
#Na programação, polimorfirsmo significa o mesmo nome de função (mas assinaturas diferentes) sendo usado para tipos diferentes.
#No entanto, o polimorfismo com herança, o mesmo método, herdado da classe pai, é possível modificar a classe herança mudando seu
#comportamento. Isso é útil em determinados casos em que a classe filha não se encaixa perfeitamente nos métodos da classe pai.

# Polimorfismo com Herança:

# Detalhe: Para fazer o polimorfismo precisamos da herança.

class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):     # Herança 
    def voar(self):
        return super().voar()
    
class Avestruz(Passaro):    # Herança
    def voar(self):
        print("Avestruz não pode voar.")
# Exemplo bizarro de herança para o método voar        
class aviao(Passaro):    # Herança
    def voar(self):
        print('Avião decolando...')

def plano_voo(objeto):  # Polimorfismo: qualquer objeto que tenha o método voar
    objeto.voar()

p1 = Pardal()
p2 = Avestruz()

plano_voo(p1)  # Saída: Voando...
plano_voo(p2)  # Saída: Avestruz não pode vo        
plano_voo(aviao())  # Saída: Avião decolando...           

# O polimorfismo não se preocupa com o 'objeto'. As classes podem possuir os métodos e podemos fazer o uso para
# realizar o polimorfismo.
    
