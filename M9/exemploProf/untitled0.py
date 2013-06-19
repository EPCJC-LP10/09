# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:13:45 2013

@author: i12201
"""
from collections import namedtuple

import menu
aluguerReg = namedtuple("aluguerReg",  "Identificacaodoautomovel,Identificacaodocliente,Datadeinicio,Datadefim") 
alugueres = []



def encontrar_posicao(Identificacaodoautomovel):
    pos = -1
    for i in range (len(alugueres)):
        if aluguerReg[i].Identificacaodoautomovel == Identificacaodoautomovel:
            pos = i
            break
                            
    return pos


def inserir():
    Identificacaodoautomovel= raw_input("qual o automovel?")

    pos = encontrar_posicao(Identificaçãodoautomóvel)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    Identificacaodocliente = raw_input("qual o cliente ?")
    Datadeinicio= raw_input("Qual a data de inicio ? ")
    Datadefim = raw_input("Qual a data final ?" )
   
    
    
    registo = aluguerReg(Identificacaodoautomovel,Identificacaodocliente,Datadeinicio,Datadefim)
    alugueres.append(registo)

        
def pesquisar():
    Identificaçãodoautomóvel = input("Qual a Identificação do automóvel ? ")

    pos = encontrar_posicao(Identificacaodoautomovel)

    if pos == -1:
        print "Não existe Identificação do automóvel com a Identificação  do cliente"
        return
  
    print "Identificacaodocliente: ", alugueres[pos].Identificacaodocliente
    print ":Datadeinicio ", alugueres[pos].Datadeinicio
    print " Datadefim: ", alugueres[pos]. Datadefim
    
    
def listar():
    for i in range (len(automoveis)):
        print "marca: ", automoveis[i].marca
        print "cor: ", automoveis[i].cor
        print "cilid: ", automoveis[i].cilidrada
        print ":anodaaquisicao ", automoveis[i].anodaaquisicao
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
            alterar()
        elif op == '3':
            eliminar()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"
