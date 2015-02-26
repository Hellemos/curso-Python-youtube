class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def ficandoVelho(self, novaIdade):
        self.idade = novaIdade
        print('Ta ficando velho hein? Sua atual idade eh: %d anos' % (self.idade))
    def projetoFicarGordo(self, novoPeso):
        self.peso += novoPeso
        print('Parabens!! Voce conseguiu ganhar peso =D seu peso atual eh: %d kg' %self.peso)
    def projetoFicarMagro(self, pesoPerdido):
        self.peso -= pesoPerdido
        print('E lamentavel, voce emagreceu =/ \nSeu peso atual eh: %d kg' % (self.peso))
    
