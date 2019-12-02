s = "Hello"
def reverse(s): 
    str = "" 
    for i in s: 
        str = i + str 
    return str 

print(reverse(s))

# print 1 to 10 + huruf:
i = 16
for i in range(17):
  if (i%3==0):
   print(f'{i} Hello')
  elif(i%4==0):
   print(f'{i} word')
  elif(i%15==0):
   print(f'{i} Hello World')
  else:
    print(i)

# sorting:
b = [4,2,5,8,1,3]
b.sort()

print(b)

# palindrome:
string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")

# palindrome angka:

n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")