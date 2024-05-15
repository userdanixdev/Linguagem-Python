# Herança Múltipla:
class Animal:
    def __init__(self,nro_patas):
        self.nro_patas = nro_patas
    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}'for chave,valor in self.__dict__.items()])}"
class Mamifero(Animal):
    def __init__(self,cor_pelo,**kw):  # kw**
        self.cor_pelo = cor_pelo
        super().__init__(**kw) # kw**
class Cachorro(Mamifero):
    def __init__(self,nro_patas):
        self.nro_patas = nro_patas
class Gato(Mamifero):
    pass
class Leao(Mamifero):
    pass
class Ave(Animal):
    def __init__(self,cor_bico,**kw): # kw**
       self.cor_bico = cor_bico
       super().__init__(**kw) # kw**
class Gato(Mamifero):
    pass       
class Ornitorrinco(Mamifero,Ave):
    pass

# Instâncias obrigatoriamente de forma nomeada com **kw
gato = Gato(nro_patas=4,cor_pelo='Preto')
print(gato)
ornitorrinco = Ornitorrinco(nro_patas=2,cor_pelo='vermelho',cor_bico='laranja')
print(ornitorrinco)




