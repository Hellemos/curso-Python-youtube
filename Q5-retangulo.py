class Retangulo(ObjetoGrafico):
    def __init__(self, base, altura, cor_de_preenchimento, cor_de_contorno):
        super(Retangulo, self).__init__(cor_de_preenchimento, cor_de_contorno)
        self.base = base
        self.altura = altura
        self.cor_de_preenchimento = cor_de_preenchimento
        self.cor_de_contorno = cor_de_contorno
       

