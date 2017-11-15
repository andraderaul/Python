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

	def empty(self): #vazia
		if self.Size == 0:
			return True
		else:
			return False

	def size(self): #quantidade de elementos
		return len(self.lista)

	def push(self, dado): #empilhando
		self.lista += [dado]

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
			print("[%d] = %d" %(i,self.lista[i]))
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


fila = Fila()
pilha = Pilha()
fila.push_back(11)
fila.front()
fila.back()
#pilha.show()
#fila.show()

'''
arquivo = open('entrada.txt','r')
saida = open('saida.txt','w')

impressora = Fila()

n = int(arquivo.readline())

for i in range(n):
	entrada = arquivo.readline()
	entrada = entrada.strip('\n') #fila
	impressora.Inserir(entrada)
	print(entrada)

m = int(arquivo.readline())

for i in range(m):
	entrada = arquivo.readline()
	entrada = entrada.split(' ')
	documento,numero = entrada[0], int(entrada[1])
	print("%s %d" %(documento,numero))
'''
