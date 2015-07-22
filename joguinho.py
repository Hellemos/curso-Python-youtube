# -*- encoding: UTF-8 -*-
def soma(n1, n2):
    resultado = n1 + n2
    return resultado

def subtracao(n1, n2):
    resultado = n1 - n2
    return resultado

def multiplicacao(n1, n2):
    resultado = n1 * n2
    return resultado

def divisao(n1, n2):
    resultado = n1 / n2
    return resultado

def modulo(n1, n2):
    resultado = n1 % n2
    return resultado

def potenciacao(n1, n2):
    resultado = n1 ** n2
    return resultado

print('*** Seja bem vindo ao jogo das operações matemática! ***')
contador = True
while (contador == True):
    n1 = float(input('Entre com o primeiro valor: '))
    n2 = float(input('Entre com o segundo valor: '))

    print('*** Selecione uma das opções: *** ')
    op = int(input('1) Adição \n2) Subtração \n3) Multiplicação \n4) Divisão \n5) Módulo \n6) Potenciação \nR.: '))

    if op == 1:
        print('Resultado da soma:', soma(n1, n2))

    if op == 2:
        print('Resultado da subtracao:', subtracao(n1, n2))

    if op == 3:
        print('Resultado da multiplicacao:', multiplicacao(n1, n2))

    if op == 4:
        print('Resultado da divisao:', divisao(n1, n2))

    if op == 5:
        print('Resultado do modulo:', modulo(n1, n2))

    if op == 6:
        print('Resultado da potenciacao:', potenciacao(n1, n2))

    if op > 6:
        print('Opção inválida! Reinicie o jogo!')

    continuar = input('Deseja continuar? S/N \nR.: ')
    if (continuar.upper() == "S"):
        continuar = True
    else:
        continuar = False
        break
        
        
