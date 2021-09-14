##Contando tamanho de sequências

file=open("ARQUIVO.fasta",'r')
list_codes=[]
for line in file:
  if line[0] != '>':
    x = (len(line) -1)
    list_codes.append(x) 

file.close()
#print(list_codes)
out_file = open("result.txt", "w")

for line in list_codes:
  line = str(line)
  out_file.write(line)
  out_file.write("\n")

out_file.close()