# -*- encoding: UTF-8 -*-

def aula():
    print('Aula sobre funções')

def nAula():
    print('Aula 16')

def cliente(nome):
    print ('Olá,', nome)

#Funções com parâmetros
def recebeNome(name):
    print('Olá,', name)

name = input('Entre com o nome: ')

#Funções dinâmicas
def soma(n1, n2):
    resultado = n1 + n2
    return resultado

print('O valor final da soma é:', soma(1, 2))

#Funções com Parâmetros pré-definidos
def soma(n1, n2, n3=5):
    resultado = n1 + n2 + n3
    return resultado

print('O valor final da soma é:', soma(1, 2))

aula()
nAula()
cliente('Hellen')
recebeNome(name)
