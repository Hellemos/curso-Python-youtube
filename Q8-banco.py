class Banco(object):
    __total = 1000
    taxaReserva = 0.1
    reservaExigida = 100
    def __init__(self):
        pass

    def __calcularReserva(self):
        print(Banco.__total * self.taxaReserva)

    def podeFazerEmprestimo(self, valor):
        if valor <= Banco.__total:
            return True
        else:
            return False
        
        
