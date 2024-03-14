# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 18:47:19 2024

@author: US
"""

#Faça um programa que tenha uma função notas() que pode receber várias 
#notas de alunos e vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas
#– A maior nota
#– A menor nota                                                                                                                                                              
#– A média da turma                                                                                                                                                      
#– A situação (opcional)
    
def notas(*n,sit=False):
    d=dict()
    d['Total']=len(n)
    d['Maior']=max(n)
    d['Menor']=min(n)
    d['Média']=sum(n)/len(n)
    if sit: 
        if d['Média']>=7:
           d['Situação']='BOA'
        elif d['Média']>=5:
             d['Situação']='RAZOÁVEL'
        else:
             d['Situação']= 'RUIM'
    return d

# Programa Principal:
resp = notas(5.5,2.5,9,8.2,sit=True)
print(resp)    
