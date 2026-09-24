def Factor(n,m):
  gcd=0
  for i in range(1,min(n,m)+1):
    if n%i==0 and m%i==0:
      gcd=i
  print(gcd)  
    
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
Factor(a,b)    


