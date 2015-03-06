'''considerando que a cor de preenchimento do retangulo e 1, a do circulo e
2 e a do triangulo e 3 '''
class ObjetoGrafico(object):
    def __init__(self, cor_de_preenchimento, cor_de_contorno):
        self.cor_de_preenchimento = cor_de_preenchimento
        self.preenchida = True
        self.cor_de_contorno = cor_de_contorno
        
    def calcularArea(self):
        if self.cor_de_preenchimento == 1:
            print('A area do retangulo eh: ', self.base * self.altura, 'cm')
        elif self.cor_de_preenchimento == 2:
            print(3.14 * self.raio ** 2)
        elif self.cor_de_preenchimento == 3:
            print(self.base * self.altura / 2)
        else:
            print('figura nao encontrada =/')

    def calcularPerimentro(self):
        if self.cor_de_preenchimento == 1:
            print('passou aqui')
            print('O perimetro do retangulo eh: ', 2 * (self.base + self.altura, 'm'))
        elif self.cor_de_preenchimento == 2:
            print('O perimentro do cirulo eh: ', 2* 3.14 * self.raio, 'm') 
        elif self.cor_de_preenchimento == 3:
            print('Digite os lados do triangulo: ' )
            a = int(input('Lado A: '))
            b = int(input('Lado B: '))
            c = int(input('Lado C: '))            
            i = 1
            while i <= 3:
                if a == b == c:
                    perimetro = a + b + c
                else:
                    print('os lados sao diferentes')
                i += 1
            print('O perimetro do triangulo eh: ', perimetro)
            
        
