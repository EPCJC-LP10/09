# -*- coding: utf-8 -*-

def principal():
    print
    print " **** MENU ****** "
    print
    print "   1. Gestão de Automóveis"
    print "   2. Registar Clientes"
    print "   3. Gestao de alugueres"

    print "   0. Sair"
    print 

    op = raw_input("Opção: ")
    return op


def automoveis():
    print
    print " *** Menu Automóveis **** "
    print
    print "1. Inserir novo"    
    print "2. Listar todos"    
    print "3. Alterar dados de um automóvel"
    print "4. Eliminar automóvel"
    print 
    print "0. Menu Anterior"

    op = raw_input("Opção: ")
    return op



def clientes():
    print
    print"********MENU clientes*********"
    print "1,inserir novo bi"
    print "2,alterar dados do bi"
    print "3,eliminar bi"
    print
    print "0. Menu Anterior"

    op = raw_input("OpÃ§Ã£o: ")
    return op
    
    

def alugueres():
    print
    print"********MENU alugueres*********"
    print "1. inserir novo aluguer"
    print "2. Ver todos alugueres"
    print "3. Ver alugueres por automovel"
    print "4. Ver alugueres por cliente"
    print
    print "0. Menu Anterior"

    op = raw_input("OpÃ§Ã£o: ")
    return op
    
    
    


if __name__ == "__main__":
    print "Este programa nÃ£o deve ser executado diretamente"

