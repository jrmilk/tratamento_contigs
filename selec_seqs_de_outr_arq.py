arq1 = open('ctgs_grandes_Sc.fasta', 'r') #contem sequencias
arq2 = open('ctgs_maiores_Sc.txt', 'r')
arq3 = open('teste.txt', 'w')
a1 = []
a2 = []
lista = []

for line in arq1:
  line = str(line)
  a1.append(line)


for line in arq2:
  line = str(line)
  a2.append(line)

ind = 0
for line in a1:
  for contig in a2:
    if line == contig:
      lista.append(a1[ind])
      lista.append(a1[ind+1])
  ind = ind + 1

for line in lista:
  arq3.write(line)
print(lista)

arq1.close()
arq2.close()
arq3.close()
