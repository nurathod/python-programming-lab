x=input()
L=len(x)
sum=0
for j in range (0,L):
 sum+=int(x[j])**L
if int(x)==sum:
 print('armstrong number')
else:
 print('Not')
