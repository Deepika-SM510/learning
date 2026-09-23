def Factor(n):
  add=0
  for i in range(1,n):
    if n%i==0:
      add+=i
  return(add)
m=int(input("Enter a number: "))
res=Factor(m)    
if res==m:
  print("perfect number")
  print(res)
else:
  print("Not perfect number")
  
      