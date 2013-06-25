# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 13:10:44 2013

@author: i12201
"""


from datetime import date
from datetime import datetime
from datetime import timedelta

data_inicio = raw_input("Data de inicio: ")
data_fim = raw_input("Data de fim: ")


a = datetime.strptime(data_inicio,'%d-%m-%Y')
b = datetime.strptime(data_fim,'%d-%m-%Y')

timedelta(7)
print (b-a).days

