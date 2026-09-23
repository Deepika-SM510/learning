def Factor(n):
  cube=0
  total=0
  while n!=0:
    k=n%10
    cube=(k**3)
    total+=cube
    n//=10
  return(total)
m=int(input("Enter a number: "))
res=Factor(m)    
print(res)

    