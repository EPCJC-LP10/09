# -*- coding: utf-8 -*-

from collections import namedtuple

import menu
clientesReg = namedtuple("clientesReg",  "nome, morada,bi,cartadeconducao")
clientes = []



def encontrar_posicao(bi):
    pos = -1
    for i in range (len(clientes)):
        if clientes[i].bi == bi:
            pos = i
            break
                            
    return pos


def inserir():
    bi= raw_input("qual o numero do bi?")

    pos = encontrar_posicao(bi)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    nome = raw_input("qual o nome  ?")
    morada = raw_input("Qual a morada ? ")
    cartadeconducao  = raw_input("Qual o numero da carta de conducao ?" )
    
    
    registo =clientesReg(bi,nome,morada,cartadeconducao)
    clientes.append(registo)


def pesquisar():
    bi = input("Qual o numero do bi ? ")

    pos = encontrar_posicao(bi)

    if pos == -1:
        print "Não existe bi com este nome"
        return
  
    print "nome: ", clientes[pos].nome
    print "morada: ", clientes[pos].morda
    print "cartadeconducao: ",clientes [pos].cartadeconducao
    
    
def listar():
    for i in range (len(clientes)):
        print "nome: ", clientes[i].nome
        print "morada: ", clientes[i].morada
        print "cartadeconducao: ",clientes[i].cartadeconducao


def eliminar():
    bi =raw_input ("bi  eliminar --> ")
    pos = encontrar_posicao(bi)

    if pos == -1:
        print "Não existe marca com esse matricula"
        return

    # TODO: Confirmar eliminação
    clientes.pop(pos)


    
def alterar():
    bi=raw_input( "bi alterar")
    pos = encontrar_posicao(bi)

    if pos == -1:
        print "NÃo existe nome este bi"
        return

    # sÃ³ altera o nome
    novonome=raw_input("qual o nome")
    novomorada=raw_input ("qual a morada ")
    novocartadeconducao = raw_input ("qual o numero da carta de condução")
    
    clientes[pos] = clientes[pos]._replace(nome=novonome,morada=novomorada,cartadeconducao=novocartadeconducao)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.clientes()

        if op == '1': 
            inserir()
        elif op == '2':
            listar()
        elif op == '3':
            alterar ()
        elif op ==  '4':
            eliminar ()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"










