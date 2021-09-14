##ver a maior len

arq1=open("lenL8Sc.txt",'r')
L = []
for line in arq1:
  a = int(line)
  L.append(a)
i = 0
ind = 1
y = L[0]
while i < len(L):
  if y < L[i]:
    y = L[i]
    #ind = i

  i = i + 1


print("Há %d sequências nesse arquivo" %(len(L)))
print("A maior len possui %d na posição %d" % (y, ind))


#########ver a menor

arq1=open("lenL1Sc.txt",'r')
L = []
for line in arq1:
  a = int(line)
  L.append(a)
i = 0
ind = 0
y = L[0]
while i < len(L):
  if y > L[i]:
    y = L[i]
    ind = i

  i = i + 1


print("Há %d sequências nesse arquivo" %(len(L)))
print("A menor len possui %d na posição %d" % (y, ind))