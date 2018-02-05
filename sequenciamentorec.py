def inicializar(tab,m,j):
    for i in range(m):
        tab[i] = j

def kmp_process(tab,P,ini,fim):
    '''add significa o que alterei no codigo padrao'''
    m = ini+(fim-ini)
    j = ini - 1
    i = ini + 1
    inicializar(tab,m,j)
    while i < m:
        while j >= ini and P[j+1] != P[i]:
            j = tab[j]
        if(P[j+1] == P[i]):
            j += 1
        tab[i] = j
        i += 1

def checaPercent(x,s,j,i):
	return 0.9 * x <= (s + j - i)

def kmp_search(tab,T,P, ini,SUB_CAD, ini_t, soma):
    '''add significa o que alterei no codigo padrao'''
    n = len(T)
    m = len(P)
    j = ini-1
    i = ini_t
    inicializar(tab,m,j)
    kmp_process(tab,P,ini,m) #add
    for i in range(ini_t,n): #add
        if j+1-ini >= SUB_CAD:
            if checaPercent(len(P), soma, j+1, ini):
                return 1
            elif P[j+1] != T[i]: #chama recursivo kmp
                return kmp_search(tab,T,P,j+1, SUB_CAD, i, soma+j+1-ini)
        if j+1 >= len(P):
            break
        while j >= ini and P[j+1] != T[i]:
            j = tab[j]
        if P[j+1] == T[i]: j+=1

    return 0

def active_gene(x,y):
    return x/y

def openFile():
	file1 = open('entrada.txt','r') #abrindo arquivo
	file2 = open('saida.txt','w') #abrindo arquivo 
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
			tab = [-1] * len(sub)
			hit += kmp_search(tab,seq,sub,0,tamSubCad,0,0) #retorna 1 ou 0
		disease[name] = round(active_gene(hit,len(subSeq)) * 100) #salva a porcentagem
		hit = 0

	for item in sorted(disease, key=disease.get, reverse=True): #imprime o dicionario
		file2.write('%s: %d%%\n' %(item,disease[item]))	
		
openFile()
