# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\i12201\.spyder2\.temp.py
"""

nome=raw_input("qual o nome")
idade=input ("qual a sua idade")
f=open("nome.txt","w")
f.write("Nome: " + nome + "\n")
f.write("idade:"+ str (idade))
f.close()