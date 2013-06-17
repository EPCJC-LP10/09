# -*- coding: utf-8 -*-

from collections import namedtuple

import menu
clientesReg = namedtuple("clientesReg",  "nome, morada,bi,cartadeconducao")
clientes = []



def encontrar_posicao(bi):
    pos = -1
    for i in range (len(clientes)):
        if clientesReg[i].bi == bi:
            pos = i
            break
                            
    return pos


def inserir_bi():
    bi= raw_input("qual o numero do bi?")

    pos = encontrar_posicao(bi)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    nome = raw_input("qual o nome  ?")
    morada = raw_input("Qual a morada ? ")
    cartadeconducao  = raw_input("Qual o numero da carta de conducao ?" )
    
    
    registo =clientesReg(nome,morada,cartadeconducao)
    clientes.append(registo)


def pesquisar_bi():
    bi = raw_input("Qual o numero do bi ? ")

    pos = encontrar_posicao(bi)

    if pos == -1:
        print "NÃ£o existe aluno com esse cÃ³digo"
        return

    print "nome: ", clientes[pos].nome
    print "morada: ", clientes[pos].morda
    print "cartadeconducao: ", clientes[pos].cartadeconducao


def listar_matricula():
    for i in range (len(clientes)):
        print "nome: ", clientes[i].nome
        print "morada: ", clientes[i].morada
        print "cartadeconducao: ",clientes[i].cartadeconducao
        
  

def eliminar_bi():
    bi =raw_input ("matricula da marca eliminar --> ")
    pos = encontrar_posicao(matricula)

    if pos == -1:
        print "NÃ£o existe marca com esse matricula"
        return

    # TODO: Confirmar eliminaÃ§Ã£o
    automoveis.pop(pos)


    
def alterar_matricula():
    matricula = raw_input ("matricula da  marca a alterar --> ")
    pos = encontrar_posicao(matricula)

    if pos == -1:
        print "NÃo existe marca com esse matricula"
        return

    # sÃ³ altera o nome
    novomarca = raw_input ("Qual o marca? ")
    novomodelo = raw_input ("qual o modelo ")
    novocor = raw_input ("qual a cor ")
    novocilidarada = raw_input ("qual  a cilidrada")
    novoano = raw_input ("qual o ano")
    novoaluguerdia = raw_input ("quantos dias aluguer")
    automoveis[pos] = automoveis[pos]._replace(marca=novomarca,modelo=novomodelo,cor=novocor,cilidrda=novocilidarada,ano=novoano,aluguerdia=novoaluguerdia)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.alunos()

        if op == '1':
            inserir_matricula()
        elif op =='2':
            listar_matricula()
        elif op == '3':
            pesquisar_matricula()
        elif op == '4':
            alterar_matricula()
        elif op == '5':
            eliminar_matricula()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"










