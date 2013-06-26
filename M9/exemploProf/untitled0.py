# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:13:45 2013

@author: i12201
"""
from collections import namedtuple
from collections import namedtuple
from datetime import datetime
from datetime import timedelta
import automoveis


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

    pos = encontrar_posicao(Identificacaodoautomovel)

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
    Identificacaodoautomovel = input("Qual a Identificação do automóvel ? ")

    pos = encontrar_posicao(Identificacaodoautomovel)

    if pos == -1:
        print "Não existe Identificação do automóvel com a Identificação  do cliente"
        return
  
    print "Identificacaodocliente: ", alugueres[pos].Identificacaodocliente
    print ":Datadeinicio ", alugueres[pos].Datadeinicio
    print " Datadefim: ", alugueres[pos]. Datadefim
    
    
def listar():
    for i in range (len(automoveis)):
       print "Identificacaodocliente: ", alugueres[i].Identificacaodocliente
       print ":Datadeinicio ", alugueres[i].Datadeinicio
       print " Datadefim: ", alugueres[i]. Datadefim



def eliminar():
    Identificacaodoautomovel =raw_input ("Identificação do automóvel da Identificação do cliente eliminar --> ")
    pos = encontrar_posicao(Identificacaodoautomovel)

    if pos == -1:
        print "NÃ£o existe marca com esse Identificação d oautomóvel"
        return

    # TODO: Confirmar eliminaÃ§Ã£o
    alugueres.pop(pos)


    
def alterar():
    Identificacaodoautomovel = raw_input ("Identificação do automóvel da  marca a alterar --> ")
    pos = encontrar_posicao(Identificacaodoautomovel)

    if pos == -1:
        print "NÃo existe marca com Identificação do automóvel"
        return

    # sÃ³ altera o nome
    novoIdentificacaodocliente = raw_input("qual o cliente ?")
    novoDatadeinicio= raw_input("Qual a data de inicio ? ")
    novoDatadefim = raw_input("Qual a data final ?" )
   
   
   
   def calcularValorPagar(aluguer, idautomovel):

    a = datetime.strptime(aluguer.Datadeinicio, '%d-%m-%Y')
    b = datetime.strptime(aluguer.Datadefim, '%d-%m-%Y')
    
    timedelta(7)
    ndias =  (b-a).days
    
    
    #Ir buscar o valor a pagar do automovel
    valorAluguer =   automoveis.automoveis[idautomovel].valordealuguer  
    print valorAluguer
    
    print "Valor a pagar = ", ndias * valorAluguer
    
    
    
    
    alugueres[pos] = alugueres[pos]._replace(Identificacaodocliente=novoIdentificacaodocliente,Datadeinicio=novoDatadeinicio,Datadefim=novoDatadefim)
        

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
