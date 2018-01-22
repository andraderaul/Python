def kmp_process(P):
    '''add significa o que alterei no codigo padrao'''
    m = len(P)
    tab = [-1] * m #add
    j = - 1
    for i in range(1,m):
        while j >= 0 and P[j+1] != P[i]:
            j = tab[j]

        if(P[j+1] == P[i]):
            j += 1
        tab[i] = j
    return tab #add

def kmp_search(T,P, SUB_CAD):
    '''add significa o que alterei no codigo padrao'''
    n = len(T)
    m = len(P)
    j = -1
    i = 0
    temp = 0 #add
    su_m = 0 #add
    tab = kmp_process(P) #add
    while i < n and len(P) >= SUB_CAD: #add
        while j >= 0 and P[j+1] != T[i]: j = tab[j]
        if P[j+1] == T[i]:
            j += 1
            temp += 1 #add
        else: # add
            if temp >= SUB_CAD: #add
                su_m += temp#temp
                P = P[SUB_CAD:]+'$' #add
                tab = kmp_process(P) #add
                j = - 1   #add
        temp = j + 1 #add

        if j == m - 1:
            su_m += j + 1
            P = P[j:]+'$' #add
            j = tab[j]
            break #add

        i += 1 #add

    return gene_mutation(su_m,m)

def gene_mutation(x,y):
    return x/y >= 0.9

def active_gene(x,y):
    return x/y

def openFile():
    file1 = open('input.txt','r') #abrindo arquivo
    tamSubCad = int(file1.readline()) #lendo o tamanho minimo da subcadeia
    seq = file1.readline() #lendo a string com a sequencia do DNA
    size = int(file1.readline()) #quantas doenças foram selecionados
    disease = dict()
    hit = 0 # hit é sinal foi encontrado a subcadeia minima dentro do padrao, foi encontrado no dna o gene
    for i in range(size):
        line = file1.readline().rstrip().split()
        name = line[0] # codigo da doença
        subSeq = line[2:] #genes
        for sub in subSeq: #todos genes
            if kmp_search(seq,sub,tamSubCad): #retorna true ou false
                hit += 1
        disease[name] = int(active_gene(hit,len(subSeq)) * 100) #salva a porcentagem
        hit = 0

    for item in reversed(sorted(disease,key=disease.get)): #imprime o dicionario
        print('%s: %d%%' %(item,disease[item]))

openFile()
