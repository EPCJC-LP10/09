# -*- coding: utf-8 -*-

#
# Exemplo utilização de array de registos
# Os elementos da lista NÃO são mantidos ordenados
# (a inserção é feita depois da última posição anterior)
# © EPCJC
#

def menu():
    print
    print "1: Inserir novo contato"
    print "2: Listar todos os contatos"
    print "3: Procurar contato por nome"
    print "4: Alterar dados de um livro"
    print "5: Eliminar livro"
    
    
    print "0: Terminar"
    print

def posicao_contato(codigo):
    ''' Encontra a posicao onde se encontra o livro com o código recebido
    
        Pesquisa por um código de livro nos livros
        já inseridos. Se NÃO encontra o código, devolve o valor -1; 
        caso contrário, devolve a posicão do livro dentro da lista
        
    '''
    
    for pos in range(len(Contatos)):
        if Contatos[pos].codigo == codigo:
            return pos
                    
    return -1   # não encontrou
    
    

def inserir():
    codigo = input("Introduza código: ")
    posicao = posicao_contato (codigo)
    if posicao != -1:
        print("Código já existente.\n")
        return
    
    # ler os restantes dados do registo
    nome = raw_input("Introduza nome: ")
    numero  = raw_input(" numero: ")
     
    
    # Criar o novo registo
    novo_registo = ContatoReg(codigo, nome, numero,)

    # Adicionar o registo à lista 
    Contatos.append(novo_registo)
    
    
def apresentar_registo(registo):
        print "Código: ", registo.codigo
        print "nome: ", registo.nome
        print " numero: ", registo.numero
       
        print "-------------------------------"


def contato_todos():
    if len(Contatos) == 0:
        print "Não existem livros inseridos"
        return

    for registo in Contatos:
        apresentar_registo(registo)
        

#Outra maneira de fazer a listagem
def listar_todos_alternativa():
    if len(Contatos) == 0:
        print "Não existem livros inseridos"
        return

    for i in range(len(Contatos)):
        apresentar_registo(Contatos[i])



def pesquisar_por_nome():
    nome = raw_input("Introduza nome: ")
    
    for pos in range(len(Contatos)):
        if Contatos[pos].nome == nome:
            apresentar_registo(Contatos[pos])
                    
    
    

    
    
def alterar():
    codigo = input("Introduza código do livro: ")
    posicao = posicao_contato(codigo)
    if posicao == -1:
        print "Esse código não existe."
        return

    apresentar_registo(Contatos[posicao])

    # A melhorar: perguntar qual o campo que se pretende alterar
    # Assim altera todos os campos com exceção do código

    #ler os novos dados
    novo_nome = raw_input("Introduza novo nome: ")
    novo_numero = input ("qual o numero: ")
   

    # Substituir o registo
    Contatos[posicao] = Contatos[posicao]._replace(novo_nome,novo_numero, 
    )

    
    
def eliminar():
    codigo = input("Introduza código do livro: ")
    posicao = posicao_contato(codigo)
    if posicao == -1:
        print "Esse código não existe."
        return

    apresentar_registo(Contatos[posicao])
    opcao = raw_input("Tem a certeza que deseja eliminar este registo (S/N)? ")
    if opcao.lower() == "s":
        #eliminar registo na posição posicao
        Contatos.pop(posicao)
        print "Registo eliminado"
    else:
        print "Registo não eliminado"


##################################

from collections import namedtuple

ContatoReg = namedtuple("contatos", "codigo, nome ,numero ")

Contatos = []
	
quero_sair = False
while not quero_sair:
    menu()
    op = raw_input("Introduza opção: ")
    if op == '1':
        inserir()
    elif op == '2':
        listar_todos_alternativa()		
    elif op == '3':
        pesquisar_por_nome()
    elif op == '4':
        alterar()
    elif op == '5':
        eliminar()
    elif op == '0': 
        quero_sair = True
    else:
		print "Opção inválida"
        
print 

