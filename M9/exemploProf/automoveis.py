# -*- coding: utf-8 -*-

from collections import namedtuple

import menu
automoveisReg = namedtuple("automoveisReg",  "matricula,marca,modelo,cor,cilindrada,anodeaquisicao,valordealuguer")
automoveis = []



def encontrar_posicao(matricula):
    pos = -1
    for i in range (len(automoveis)):
        if automoveis[i].matricula == matricula:
            pos = i
            break
                            
    return pos


def inserir():
    matricula= raw_input("qual a matricula?")

    pos = encontrar_posicao(matricula)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    marca = raw_input("qual a marca  ?")
    modelo = raw_input("Qual o modelo ? ")
    cor  = raw_input("Qual a cor ?" )
    cilindrada = raw_input("qual a cilidrada")
    anodaaquisicao=raw_input("qual o ano da aquisição")
    valordealuguer=raw_input("qual o preço de aluguer")
    
    
    
    registo = automoveisReg(matricula,marca, modelo, cor, cilindrada, anodaaquisicao, valordealuguer)
    automoveis.append(registo)

        
def pesquisar():
    matricula = input("Qual a matricula ? ")

    pos = encontrar_posicao(matricula)

    if pos == -1:
        print "Não existe matricula com essa marca"
        return
  
    print "marca: ", automoveis[pos].marca
    print "cor: ", automoveis[pos].cor
    print "cilidrada: ", automoveis[pos].cilindrada
    print ":anodaaquisicao ", automoveis[pos].anodeaquisicao
    print "varlordealuguer: ", automoveis[pos].valordealuguer
    
def listar():
    for i in range (len(automoveis)):
        print "marca: ", automoveis[i].marca
        print "cor: ", automoveis[i].cor
        print "cilidrada: ", automoveis[i].cilindrada
        print ":anodaaquisicao ", automoveis[i].anodeaquisicao
        print "varlordealuguer: ", automoveis[i].valordealuguer



def eliminar():
    matricula =raw_input ("matricula da marca eliminar --> ")
    pos = encontrar_posicao(matricula)

    if pos == -1:
        print "NÃ£o existe marca com esse matricula"
        return

    # TODO: Confirmar eliminaÃ§Ã£o
    automoveis.pop(pos)


    
def alterar():
    matricula = raw_input ("matricula da  marca a alterar --> ")
    pos = encontrar_posicao(matricula)

    if pos == -1:
        print "NÃo existe marca com esse matricula"
        return

    # sÃ³ altera o nome
    novomarca = raw_input ("Qual o marca? ")
    novomodelo = raw_input ("qual o modelo ")
    novocor = raw_input ("qual a cor ")
    novocilindrada = raw_input ("qual  a cilidrada")
    novoano = raw_input ("qual o ano")
    novoaluguerdia = raw_input ("quantos dias aluguer")
    automoveis[pos] = automoveis[pos]._replace(marca=novomarca,modelo=novomodelo,cor=novocor,cilidrda=novocilindrada,ano=novoano,aluguerdia=novoaluguerdia)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.automoveis()

        if op == '1':
            inserir()
        elif op == '2':
            listar()
        elif op == '3':
            alterar()
        elif op == '4':
            eliminar()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"










