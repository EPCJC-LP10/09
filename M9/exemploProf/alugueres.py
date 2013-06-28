# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:13:45 2013

@author: i12201
"""
from collections import namedtuple
from datetime import datetime
from datetime import timedelta
import automoveis


import menu

aluguerReg = namedtuple("aluguerReg",  "Identificacaodoautomovel,Identificacaodocliente, Datadeinicio, Datadefim, valorPagar") 
alugueres = []



def encontrar_posicao(Identificacaodoautomovel):
    pos = -1
    for i in range (len(alugueres)):
        if alugueres[i].Identificacaodoautomovel == Identificacaodoautomovel:
            pos = i
            break
                            
    return pos


def inserir():
    Identificacaodoautomovel= raw_input("qual o identificao do automovel?")

    pos = encontrar_posicao(Identificacaodoautomovel)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    Identificacaodocliente = raw_input("qual o cliente ?")
    Datadeinicio= raw_input("Qual a data de inicio ? ")
    Datadefim = raw_input("Qual a data final ?" )
   
    valorAluguer =   automoveis.automoveis[Identificacaodoautomovel].valordealuguer      
    
    valorPagar =  calcularValorPagar(Datadeinicio, Datadefim, valorAluguer) 
    
    
    registo = aluguerReg(Identificacaodoautomovel,Identificacaodocliente, Datadeinicio, Datadefim, valorPagar)
    alugueres.append(registo)

        
def pesquisar():
    Identificacaodoautomovel = input("Qual a Identificação do automóvel ? ")

    pos = encontrar_posicao(Identificacaodoautomovel)

    if pos == -1:
        print "Não existe Identificação do automóvel com a Identificação  do cliente"
        return
  
    print "Identificacaodocliente: ", alugueres[pos].Identificacaodocliente
    print ":Datadeinicio ", alugueres[pos].Datadeinicio
    print " Datadefim: ", alugueres[pos]. Datadefim
    
    
def listar():
    for i in range (len(alugueres)):
       print "Identificacaodocliente: ", alugueres[i].Identificacaodocliente
       print ":Datadeinicio ", alugueres[i].Datadeinicio
       print " Datadefim: ", alugueres[i]. Datadefim



def eliminar():
    Identificacaodoautomovel =raw_input ("Identificação do automóvel da Identificação do cliente eliminar --> ")
    pos = encontrar_posicao(Identificacaodoautomovel)

    if pos == -1:
        print "NÃ£o existe  Identificação do automóvel com esse cliente "
        return

    # TODO: Confirmar eliminaÃ§Ã£o
    alugueres.pop(pos)


    
def alterar():
    Identificacaodoautomovel = raw_input ("Identificação do automóvel  alteracao --> ")
    pos = encontrar_posicao(Identificacaodoautomovel)
    
    if pos == -1:
        print "NÃo existe  Identificação do automóvel"
        return
    
    # sÃ³ altera o nome
    novoIdentificacaodocliente = raw_input("qual o cliente ?")
    novoDatadeinicio= raw_input("Qual a data de inicio ? ")
    novoDatadefim = raw_input("Qual a data final ?" )
    
    alugueres[pos] = alugueres[pos]._replace(Identificacaodocliente=novoIdentificacaodocliente,Datadeinicio=novoDatadeinicio,Datadefim=novoDatadefim)
   
   
   
def calcularValorPagar(di, df, valordiario):

    a = datetime.strptime(di, '%d-%m-%Y')
    b = datetime.strptime(df, '%d-%m-%Y')
    
    timedelta(7)
    ndias =  (b-a).days
    

    
    return ndias * valordiario
    


def gerir():

    terminar = False

    while not terminar:
        op = menu.alugueres()

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
