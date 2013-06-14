# -*- coding: utf-8 -*-

from collections import namedtuple

import menu



automoveisreg = namedtuple("automoveisReg", " marca, modelo ,cor,cilindrada,ano de aquisição,matricula,valor do aluguerpor dia")
automoveisreg = []



def encontrar_posicao(marca):
    pos = -1
    for i in range (len( automoviesreg )):
        if automoveisreg[i].id ==marca:
            pos = i
            break
                            
    return pos


def inserir_marca():
    marca = input("qual a marca? ")

    pos = encontrar_posicao(modelo)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    modelo = raw_input("Qual é a cor ? ")
    
    registo = automoviesReg(modelo,cor)
    automoviereg.append(registo)


def pesquisar_marca():
    marca = input("Qual o codigo do aluno a pesqu? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "NÃ£o existe aluno com esse cÃ³digo"
        return

    print "CÃ³digo: ", listaAlunos[pos].id
    print "Nome: ", listaAlunos[pos].nome
    


def listar_alunos():
    for i in range (len(listaAlunos)):
        print "CÃ³digo: ", listaAlunos[i].id
        print "Nome: ", listaAlunos[i].nome
        
  

def eliminar_aluno():
    cod = input ("CÃ³digo do aluno a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "NÃ£o existe aluno com esse cÃ³digo"
        return

    # TODO: Confirmar eliminaÃ§Ã£o
    listaAlunos.pop(pos)


    
def alterar_aluno():
    cod = input ("CÃ³digo do aluno a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "NÃ£o existe aluno com esse cÃ³digo"
        return

    # sÃ³ altera o nome
    novonome = raw_input("Qual o nome? ")
    listaAlunos[pos] = listaAlunos[pos]._replace(nome=novonome)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.alunos()

        if op == '1':
            inserir_marca()
        elif op =='2':
            listar_marca()
        elif op == '3':
            pesquisar_marca()
        elif op == '4':
            alterar_aluno()
        elif op == '5':
            eliminar_marca()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"










