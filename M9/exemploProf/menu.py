# -*- coding: utf-8 -*-

def principal():
    print
    print " **** MENU ****** "
    print
    print "   1. Gest�o de Autom�veis"
    print "   2. Registar Clientes"
    print 
    print "   0. Sair"
    print 

    op = raw_input("Op��o: ")
    return op


def automoveis():
    print
    print " *** Menu Autom�veis **** "
    print
    print "1. Inserir novo"    
    print "2. Alterar dados de um autom�vel"
    print "3. Eliminar autom�vel"
    print 
    print "0. Menu Anterior"

    op = raw_input("Op��o: ")
    return op



def clientes():
    print
    print"********MENU clientes*********"
    print "1,inserir novo bi"
    print "2,alterar dados do bi"
    print "3,eliminar bi"
    print
    print "0. Menu Anterior"

    op = raw_input("Opção: ")
    return op


if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"

