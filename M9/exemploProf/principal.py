# -*- coding: utf-8 -*-

import menu
import automoveis
import util


# nome dos ficheiros
fxAlunos = "fxAlunos.dat"

def ler_ficheiros():
	# adicionar todos ficheiros a ler
	automoveis.automoveis = util.ler_ficheiro(fxAlunos)
     

def escrever_ficheiros():
	# adicionar todos ficheiros a guardar
	util.escrever_ficheiro(fxAlunos, automoveis.automoveis)



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


