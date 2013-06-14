# -*- coding: utf-8 -*-

def principal():
    print
    print " **** MENU ****** "
    print
    print "   1. Gest„o de Alunos"
    print "   2. Registar PresenÁa (n„o implementado)"
    print 
    print "   0. Sair"
    print 

    op = raw_input("Op√ß√£o: ")
    return op


def alunos():
    print
    print " *** Menu Alunos **** "
    print
    print "1. Inserir novo aluno"
    print "2. Listar todos alunos"
    print "3. Pesquisar aluno"
    print "4. Alterar dados de um aluno"
    print "5. Eliminar aluno"
    print 
    print "0. Menu Anterior"

    op = raw_input("Op√ß√£o: ")
    return op



if __name__ == "__main__":
    print "Este programa n√£o deve ser executado diretamente"

