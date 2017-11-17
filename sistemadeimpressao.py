#!/usr/bin/python
# -*- coding: utf-8 -*-
# @authores Raul Andrade e Aryella Lacerda

class Node(object):
	def __init__(self, dado):
		self.dado = dado
		self.next = None

	def __str__(self):
		return str(self.dado)

class Pilha(object):

	def __init__(self):
		self.lista = []
		self.num = []

	def empty(self): #vazia
		if self.Size == 0:
			return True
		else:
			return False

	def size(self): #quantidade de elementos
		return len(self.lista)

	def push(self, dado,num): #empilhando
		self.lista += [dado]
		self.num += [num]

	def pop(self): #desempilhando
		if self.Empty():
			print("VAZIA pop")
			return None
		else:
			dado = self.lista[-1]
			del self.lista[-1]
			return dado

	def top(self): #acessar o topo da lista
		print(self.lista[-1])
		return self.lista[-1]

	def show(self): #mostrar todos
		i = len(self.lista)-1
		while i > -1:
			print("%s-%sp" %(self.lista[i],self.num[i]))
			i -= 1

class Fila(object):

	def __init__(self):
		self.length = 0
		self.head = None
		self.tail = None

	def empty(self): #vazia
		return self.length == 0

	def size(self): #quantidade de elementos
		return self.length

	def push_back(self, dado): #enfileirar
		node = Node(dado)
		if self.empty():
			self.head = self.tail = node
		else:
			temp = self.tail
			temp.next = node
			self.tail = node
		self.length += 1

	def pop_front(self): #desenfileirar
		temp = self.head
		self.head = self.head.next
		self.length -= 1
		if self.empty():
			self.tail = None
		return temp

	def front(self): #acessar o elemento inicial
		if self.empty():
			print("Fila Vazia")
		else:
			print("%s" %(self.head))

	def back(self): #acessar o elemento final
		if self.empty():
			print("Fila Vazia")
		else:
			print("%s" %(self.tail))

	def show(self): #mostrar todos
		if not self.empty():
			temp = self.head
			while(temp is not None):
				print("%s" %(temp))
				temp = temp.next

class Impressora(object):
	def __init__(self, nome, status, pages,acum,concat):
		self.nome = nome
		self.status = status
		self.pages = pages
		self.acum = acum
		self.concat = concat
		self.lista = []
		self.num = []

	def add(self,dado,num):
		self.lista += [dado]
		self.num += [num]



class Documento(object):
    def __init__(self, nome, pages):
        self.nome = nome
        self.pages = pages


arquivo = open('sistemadeimpressao.txt','r')
saida = open('saida.txt','w')

fila_documentos = Fila()
pilha_historico = Pilha()
lista = []

n = int(arquivo.readline()) #num impressoras
for i in range(n):
	entrada = arquivo.readline()
	entrada = entrada.strip('\n')
	impressora = Impressora(entrada,False, 0, 0,"")
	lista.append(impressora)

m = int(arquivo.readline()) #num documentos
for i in range(m):
	entrada = arquivo.readline()
	entrada = entrada.split(' ')
	documento = Documento(entrada[0],int(entrada[1]))
	fila_documentos.push_back(documento)

acumulador = 0
while not fila_documentos.empty():
	index = -1
	for i in range(n):
		if(not lista[i].status): #checando se esta disponivel
			index = i
			break

	if index is not -1:
		documento_atual = fila_documentos.pop_front()
		lista[index].add(documento_atual.dado.nome,documento_atual.dado.pages)
		lista[index].status = True
		lista[index].acum += documento_atual.dado.pages
		lista[index].pages = documento_atual.dado.pages
		nome = lista[index].nome
		historico =  documento_atual.dado.nome+"-"+str(documento_atual.dado.pages)+"p"+lista[index].concat
		print("[%s] %s" %(nome,historico)) #Imprimindo historico
		lista[index].concat = ", "+historico #pra imprimir formatado
		acumulador += documento_atual.dado.pages #acumulando as paginas

	else:
		menores = []
		for i in range(n):
			menores.append(lista[i].acum)
		menor = min(menores)
		index = menores.index(menor)
		lista[index].status = False
		string = lista[index].lista.pop(0)
		num = lista[index].num.pop(0)
		pilha_historico.push(string,int(num))

menores = []
for i in range(n):
	menores.append(lista[i].acum)
for j in range(len(lista)):
	menor = min(menores)
	index = menores.index(menor)
	menores[index] = 1000000000
	string = lista[index].lista.pop(0)
	num = lista[index].num.pop(0)
	pilha_historico.push(string,int(num))

print(acumulador)
pilha_historico.show()
