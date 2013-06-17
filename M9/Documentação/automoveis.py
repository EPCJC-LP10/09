# -*- coding: utf-8 -*-

from collections import namedtuple

import menu



automoveisReg = namedtuple("automoveisReg",  "matricula, marca, modelo,cor, cilindrada, ano, aluguerdia")
automoveis = []



def encontrar_posicao(matricula):
    pos = -1
    for i in range (len( automoveis )):
        if automoveisReg[i].matricula == matricula:
            pos = i
            break
                            
    return pos


def inserir_matricula():
    matricula = raw_input("qual a matricula? ")

    pos = encontrar_posicao(matricula)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    marca = raw_input("qual a marca ?")
    modelo = raw_input("Qual é o modelo ? ")
    cor = raw_input("Qual a cor ?" )
    cilindrada = raw_input("qual  a cilidrada ?" )
    ano = raw_input ("qual o ano ?")
    aluguerdia = raw_input ("quantos dias aluguer ?")
   
    
    registo =automoveisReg(marca,modelo,cor,cilindrada,ano,aluguerdia)
    automoveis.append(registo)


def pesquisar_matricula():
    matricula = raw_input("Qual a matricula ? ")

    pos = encontrar_posicao(matricula)

    if pos == -1:
        print "NÃ£o existe aluno com esse cÃ³digo"
        return

    print "marca: ", automoveis[pos].marca
    print "modelo: ", automoveis[pos].modelo
    print "cor: ", automoveis[pos].cor
    print "cilindrada: ", automoveis[pos].cilidrada
    print "ano:",automoveis[pos].ano
    print "aluguer:",automoveis[pos].aluguerdia
    


def listar_matricula():
    for i in range (len(automoveis)):
        print "marca: ", automoveis[i].marca
        print "modelo: ", automoveis[i].modelo
        print "cor: ", automoveis[i].cor
        print "cilindrada:", automoveis[i].cilidrada
        print "ano:",automoveis[i].ano
        print "aluguer:",automoveis[i].aluguerdia
        
  

def eliminar_matricula():
    matricula =raw_input ("matricula da marca eliminar --> ")
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










