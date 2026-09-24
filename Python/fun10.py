
def Largest(n): 
  largest=0
  count=0
  m=0
  for i in range(1,n+1):
    count=0
    for j in  range(1,i+1):
      if i%j==0:
        count+=1

    if count>largest:
         largest=count
         m=i
  return largest,m 
print("largest factor numbers")
a=int(input("Enter a number: "))    
res=Largest(a) 
print(res)
