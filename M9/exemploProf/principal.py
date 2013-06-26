# -*- coding: utf-8 -*-

import menu
import automoveis
import clientes
import util
import alugueres

# nome dos ficheiros
fxAutos = "fxAutos.dat"
fxClientes = "fxClientes.dat"
fxalugueres = "fxalugueres.dat"


def ler_ficheiros():
    # adicionar todos ficheiros a ler
    automoveis.automoveis = util.ler_ficheiro(fxAutos)
    clientes.clientes = util.ler_ficheiro(fxClientes)
    alugueres.alugueres = util.ler_ficheiro(fxalugueres)

def escrever_ficheiros():
    # adicionar todos ficheiros a guardar
    util.escrever_ficheiro(fxAutos, automoveis.automoveis)
    util.escrever_ficheiro(fxClientes, clientes.clientes)
    util.escrever_ficheiro(fxalugueres, alugueres.alugueres)



# Bloco Principal

ler_ficheiros()

terminar = False
while not terminar:
    op = menu.principal()
    
    if op == '1':
        automoveis.gerir()
    elif op == '2':
        clientes.gerir()
    elif op == '3':
        alugueres.gerir()
    elif op == '0':
        terminar = True


escrever_ficheiros()


