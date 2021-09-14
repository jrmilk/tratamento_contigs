##Selecionando sequências e seus cabeçalhos por tamanhos de seqs

arq = open("ctg_L8_Sc_iii.fasta", "r")
cabec = []
indices = []
total_seq = [] #contem TODAS as sequencias
seqs = [] #seq CORRETAS
cabeçalhos = []
q = 0
for line in arq:
  if line[0] != '>':
    total_seq.append(line)
    q = q + 1

  if line[0] == '>':
    cabec.append(line)
#print(cabec)
print(q)
i = 0

for seq in total_seq:
  if len(seq) > 1390:
    indices.append(i)
    seqs.append(seq)
  i = i + 1
#print(seqs)

#print(cabec)
#print(indices)

w = 0
s = 0
soma = 0
for line in cabec:
  i = i + 1
  #(line)

lista = [] #CONTEM OS CABEÇALHOS CORRETOS
print(indices)
for ind in indices:
  s = s + 1
  ind = int(ind)
  for x in cabec:
    if x == cabec[ind]:
      w = w + 1
      print(cabec[ind])
      lista.append(cabec[ind])
print(s) #total de indices
print(w)
print(lista)

z = 0
arqf = open("ctgs_grandes_L8_Sc_iii.fasta", "w")
while z < 53:
  #ATENÇÃO: O VALOR DO WHILE ÉÉ VARIÁVEL. DEVE SER O NUMERO TOTAL DE SEQS GRANDES JÁÁ VISTO ANTES SENÃÃO O PROGRAMA NÃÃO RODA
  arqf.write(lista[z])
  arqf.write(seqs[z])
  z = z + 1

arqf.close()
arq.close()
#print(list_codes)




