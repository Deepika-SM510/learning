def prime(a):
  prime=True
  for i in range(2,a):
    if a%i==0:
      prime=False
  if prime:
    print("Prime")
  else:
    print("Not prime")
def Pallindrome(a):
  rev=0
  m=a
  for i in range(1,100):
    if a==0:
      break
    k=a%10
    rev=(rev*10)+k
    a=a//10
  print(rev)  
  if m==rev:
    print("Pallindrome")
  else:
    print("Not pallindrome")
def Armstrong(a):
  sum=0
  cube=0
  m=a
  while a!=0:
    k=a%10
    cube=k**3 
    sum+=cube
    a=a//10
  print(sum)
  if sum==m:
    print("Armstrong")
  else:   
    print("Not armstrong")
def perfectnumber(a):
  add=0
  for i in range(1,a):
    if a%i==0:
      add+=i
  print(add)
  if add==a:
    print("Perfect number")             
  else:   
    print("Not perfect number")
def maths():
  def menu():
    print("____Maths____\n1.Prime\n2.Pallindrome\n3.Armstrong\n4.Perfect number")
  menu()
  while True:
    choice=int(input("Enter your choice: "))
    if choice==1:
      a=int(input("Enter a number: "))
      prime(a)
    elif choice==2:
      a=int(input("Enter a number: "))
      Pallindrome(a)
    elif choice==3:
      a=int(input("Enter a number: "))
      Armstrong(a)
    elif choice==4:
      a=int(input("Enter a number: "))
      perfectnumber(a)
    elif choice==5:
      print("EXIT")
      break  
    else:
      print("Invalid choice")
 
maths()  
