check2=int(input())
valid2=list(map(int,input().split()[:check2]))
valid2.sort()
for i in valid2:
  print(i,end=" ")
