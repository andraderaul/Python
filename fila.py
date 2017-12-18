#!/usr/bin/python
# -*- coding: utf-8 -*-
class Fila(object):

    def __init__(self):
        self.fila = []
        self.size = 0

    def Empty(self):
        return len(self.fila) == 0

    def Push(self, dado):
        self.fila += [dado]
        self.size += 1

    def Pop(self):
        if self.Empty():
            print("A fila esta vazia")
        else:
            self.fila = [self.fila[i] for i in range(1,self.size)]
            self.size -= 1

    def Show(self):
        n = self.size - 1
        while n > -1:
            print("[%d] => %d" %(n,self.fila[n]))
            n -= 1

    def Front(self):
        if self.Empty():
            print("Fila Vazia")
        else:
            print("Primeiro dado: %d" %(self.fila[0]))


fila = Fila()


fila.Push(12)
fila.Push(23)
fila.Push(56)
fila.Push(78)

fila.Show()
