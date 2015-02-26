class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = 0
        self.perimetro = 0
    def mudarLados(self, novoValorBase, novoValorAltura):
        self.base = novoValorBase
        self.altura = novoValorAltura
    def retornarValorLados(self):
        return 'O novo valor da base eh %d cm e da altura eh %d cm' % (self.base, self.altura)
    def calcularArea(self):
        self.area = self.base * self.altura
        print('A area do retangulo eh: %d cm' %self.area)
    def calcularPerimetro(self):
        self.perimetro = 2 * (self.base + self.altura)
        print('O perimetro deste retangulo tem valor igual a %d' % (self.perimetro))
    
        
