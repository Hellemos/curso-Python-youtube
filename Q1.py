class Quadrado:
    def __init__(self):
        self.tamanhoDoLado = 0
        self.area = 0.0

    def mudarLado(self, novoValor):
        self.tamanhoDoLado = novoValor
    def retornarValorLado(self):
        return self.tamanhoDoLado
    def calcularArea(self):
        self.area = self.tamanhoDoLado**2
        print('A area do quadrado eh: %.2f' % (self.area))
        
