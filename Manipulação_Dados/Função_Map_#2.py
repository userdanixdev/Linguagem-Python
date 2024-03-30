# Reescreva o código abaixo, usando a função map(). 

palavras = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil.'.split()
print(palavras)
resultado = [[w.upper(),w.lower(),len(w)]for w in palavras]
for item in resultado:
  print(item)

Resultado:  
['A', 'Data', 'Science', 'Academy', 'oferece', 'as', 'melhores', 'cursos', 'de', 'análise', 'de', 'dados', 'do', 'Brasil.']
['A', 'a', 1]
['DATA', 'data', 4]
['SCIENCE', 'science', 7]
['ACADEMY', 'academy', 7]
['OFERECE', 'oferece', 7]
['AS', 'as', 2]
['MELHORES', 'melhores', 8]
['CURSOS', 'cursos', 6]
['DE', 'de', 2]
['ANÁLISE', 'análise', 7]
['DE', 'de', 2]
['DADOS', 'dados', 5]
['DO', 'do', 2]
['BRASIL.', 'brasil.', 7]

======================//==================================//=================================================//==============================
# Usando a função MAP:
palavras = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil.'.split()
resultado = map(lambda w: [w.upper(),w.lower(),len(w)], palavras)
for item in resultado:
  print(item)

# Chega-se ao mesmo resultado.

=============//====================//=======================//=====================//======
