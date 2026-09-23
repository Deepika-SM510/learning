def Largest(n):
  largest=0
  for i in range(1,n+1):
    count=0
    for j in  range(1,i+1):
      if i%j==0:
        count+=1
  print(count)  
  if count>largest:
    largest=count
    print("largest factor numbers")
a=int(input("Enter a number: "))    
Largest(a) 
