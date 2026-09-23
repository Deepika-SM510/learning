def Factor(n,m):
  for i in range(max(n,m),(n*m)+1):
    if i%n==0 and i%m==0:
         print()
    print(i)        
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
res=Factor(a,b)
print(res)


