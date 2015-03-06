class Circulo(ObjetoGrafico):
    def __init__(self, raio, cor_de_preenchimento, cor_de_contorno):
        super(Circulo, self).__init__(cor_de_preenchimento, cor_de_contorno)
        self.raio = raio
        self.cor_de_preenchimento = cor_de_preenchimento
        self.cor_de_contorno = cor_de_contorno

