class Datagrama(object):
    def __init__(self,num,dado):
        self.num = num
        self.dado = dado

def swap(s1,s2):
    return s2,s1

def heapify(arr,n,i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i].num < arr[l].num:
        largest = l
    if r < n and arr[largest].num < arr[r].num:
        largest = r

    if largest != i:
        arr[i],arr[largest] = swap(arr[i],arr[largest])
        heapify(arr,n,largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0] = swap(arr[i],arr[0])
        heapify(arr,i,0)

def show(arr,cont,linha,out):
    n = len(arr)
    anti = cont
    aux = linha
    for i in range(n):
        if cont == arr[i].num:
            if cont == anti :
                out.write('%d: ' %(linha))
                linha += 1
            out.write('%s' %(arr[i].dado))
            cont += 1

    if linha != aux:
        out.write('\n')

    return cont,linha

def readFile():

    arq = open('input2.txt','r')
    arq2 = open('output.txt','w')
    dimensions = arq.readline().split(' ')
    ntotal, qpacote = int(dimensions[0]),int(dimensions[1])

    arr = []
    cont = 0
    linha = 0
    line = " "

    while len(line) is not 0:
        for i in range(qpacote):
            line = arq.readline().rstrip()
            if len(line) is not 0:
                numpac = int(line[0])
                dado = line[4:len(line)]
                pacote = Datagrama(numpac,dado)
                arr.append(pacote)

        heapsort(arr)
        cont,linha = show(arr,cont,linha,arq2)

def main():
    readFile()

if __name__ == "__main__":
    main()
