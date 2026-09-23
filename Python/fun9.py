def AMICABLE(n,m):
  sum=0
  add=0
  for i in range(1,n):
    if n%i==0:
      sum+=i
  print(sum)  
  for j in range(1,m):
    if m%j==0:
      add+=j
  print(add)  
  if sum==m and add==n:
    print("amicable numbers")
  else:
    print("not amicable numbers")
a=int(input("Enter a number: "))    
b=int(input("Enter a number: "))    
AMICABLE(a,b) 
