Herança:

	A herança é a capacidade de uma classe filha derivar ou herdar as características e comportamentos da classe pai(base).
Fornece reutilização de código, não precisamos escrever o mesmo código. Além disso, permite adicionar mais recursos a uma classe sem modificá-la.
Possui natureza transitiva. Se a classe B herda da classe A, todas as subclasses de B herdarão da classe A.
Se eu criar uma Classe C, irá herdar da classe B e A e assim, sucessivamente. 
A sintaxe é simples:

	class A:
	pass
	class B(A):
	pass

Herança simples é o que ocorre acima.
Agora a herança múltipla a classe filha herda de várias classes pai. Python implementa heranças múltiplas.

	class A:
	pass
	class B:
	pass
	class C(A,B):
	pass
