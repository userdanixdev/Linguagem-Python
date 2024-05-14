class Bicicleta:
    def __init__(self,cor,modelo,ano,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        

    def buzinar(self):
        print('piiiii')
    def parar(self):
        print('Parando bicicleta..')
        print('Bike parou')
    def correr(self):
        print('Vrumm')
    def get_cor(self):
        return self.cor
    def __str__(self):
        #return f"{self.__class__.__name__}:{[f'{chave}={valor}'for chave,valor in self.__dict__.items()]}"
        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}'for chave,valor in self.__dict__.items()])}"

    def trocar_marcha(nro_marcha):
        print('Marcha trocada')

caloi = Bicicleta('vermelha','caloi',2022,600)
print(caloi)
