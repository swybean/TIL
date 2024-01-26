# N = 3
# M = 16

# for numb in range(N,M+1):
#   for a in range(2,N):
#     if numb % (a) !=0:
#       print(numb)

N, M = list(map(int,input().split()))


num_list1 = []

for numb in range(N,M+1):
   for a in range(2,N):
     if numb % (a) !=0:
       num_list1.append(numb)


for numbb in num_list1:
  if numbb % (3) ==0:
    num_list1.remove(numbb)
    
    
num_list1.insert(0, 3)

for i in num_list1:
  print(i)
