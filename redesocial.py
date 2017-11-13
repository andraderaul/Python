#!/usr/bin/python
# -*- coding: utf-8 -*-
class Nodo(object):
    def __init__(self,nome):
        self.nome = nome
        self.anterior = None
        self.proximo = None

class RedeSocial(object):
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def vazia(self):
        if self.primeiro == None:
            return True
        else:
            return False

    def __unir_amizade(self):
        if self.primeiro != None:
            self.primeiro.anterior = self.ultimo
            self.ultimo.proximo = self.primeiro

    def __buscar(self,nome):
        aux = self.primeiro
        while aux:
            if aux.nome == nome:
                return True
            else:
                aux = aux.proximo
                if aux == self.primeiro:
                        return False

    def inserir(self,nome):
        if self.vazia(): #caso a lista esteja vazia
            self.primeiro = self.ultimo = Nodo(nome)
            self.__unir_amizade()
            saida.write("[%s] ADD-OK\n" %nome)
        else:
            if self.__buscar(nome): # caso o nome ja exista
                saida.write("[%s] ADD-ERROR\n" %nome)
            else: #caso a lista seja maior que 1
                user = Nodo(nome)
                user.proximo = self.primeiro
                self.primeiro.anterior = user
                self.primeiro = user
                self.__unir_amizade()
                saida.write("[%s] ADD-OK\n" %nome)

    def mostrar(self,nome):
        aux = self.primeiro
        while aux:
            if aux.nome == nome: #achamos
                saida.write("[%s]<-[%s]->[%s]\n" %(aux.proximo.nome,aux.nome,aux.anterior.nome))
                break
            else:#nao achamos
                aux = aux.proximo #proximo
                if aux == self.primeiro: #caso o usuario nao esteja na rede social
                    saida.write("[%s] SHOW-ERROR\n" %(nome))
                    break

    def remover(self,nome):
        if self.vazia(): #caso a lista seja vazia
            saida.write("[%s] REMOVE-ERROR\n" %(nome))
        elif self.primeiro == self.ultimo: #caso so tenha um elemento
            self.primeiro = self.ultimo = None
            saida.write("[%s] REMOVE-OK\n" %(nome))
        else: #caso a lista seja maior que 1
            aux = self.primeiro
            while aux:
                if aux.nome == nome: #achamos
                    aux.anterior.proximo = aux.proximo
                    aux.proximo.anterior = aux.anterior
                    saida.write("[%s] REMOVE-OK\n" %(nome))
                    break
                else: #nao achamos
                    aux = aux.proximo #proximo
                    if aux == self.primeiro: #nao esta na lista
                        saida.write("[%s] REMOVE-ERROR\n" %(nome))
                        break
        self.__unir_amizade()


arquivo = open('entrada.txt','r') #leitura
saida = open('saida.txt','w') #escrita
lista = RedeSocial()

while True:
    line = arquivo.readline()
    if len(line) == 0:
        break
    else:
        if line[0] is 'A':
            add = line[4:]
            add = add.strip('\n') #remover o \n
            lista.inserir(add)
        elif line[0] is 'S':
            show = line[5:]
            show = show.strip('\n') #remover o \n
            lista.mostrar(show)
        elif line[0] is 'R':
            remove = line[7:]
            remove = remove.strip('\n') #remover o \n
            lista.remover(remove)

arquivo.close()
saida.close()
