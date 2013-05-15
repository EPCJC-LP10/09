# -*- coding: utf-8 -*-

#
# Exemplo utilização de array de registos
# Os elementos da lista NÃO são mantidos ordenados
# (a inserção é feita depois da última posição anterior)
# © EPCJC
#

def menu():
    print
    print "1: Inserir "
    print "2: Listar remover"
    print "3:ver os elementos"
    print
    print "0: Terminar"
    print

   

def inserir(fila):
    elemento=input("qual o elemento")    
    fila.insert(0, elemento)
    
    
def remover(fila):
    fila.pop()
    
def ver_todos(fila):
    for i in range(len(fila)):
        print fila[i], 

    
  
Fila =[]
  
quero_sair = False
while not quero_sair:
    menu()
    op = raw_input("Introduza opção: ")
    if op == '1':
        inserir(Fila)
    elif op == '2':
        remover(Fila)		
    elif op == '3':
        ver_todos(Fila)
   
    elif op == '0': 
        quero_sair = True
    else:
		print "Opção inválida"
        


