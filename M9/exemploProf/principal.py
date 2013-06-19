# -*- coding: utf-8 -*-

import menu
import automoveis
import clientes
import util


# nome dos ficheiros
fxAutos = "fxAutos.dat"
fxClientes = "fxClientes.dat"

def ler_ficheiros():
    # adicionar todos ficheiros a ler
    automoveis.automoveis = util.ler_ficheiro(fxAutos)
    clientes.clientes = util.ler_ficheiro(fxClientes)
     

def escrever_ficheiros():
    # adicionar todos ficheiros a guardar
    util.escrever_ficheiro(fxAutos, automoveis.automoveis)
    util.escrever_ficheiro(fxClientes, clientes.clientes)



# Bloco Principal

ler_ficheiros()

terminar = False
while not terminar:
    op = menu.principal()
    
    if op == '1':
        automoveis.gerir()
    elif op == '2':
        pass    #por fazer
    elif op == '0':
        terminar = True


escrever_ficheiros()


