#LIST COMPREHENSIONS:
#GENERATE POSITIVE LIST OF NUMBERS FROM A GIVEN LIST OF INTEGERS
l=[]
n=int(input("Enter the number of elements:"))
print("Enter the elements:")
for i in range(0,n):
    e=int(input())
    l.append(e)
print(l)
n=0
print("The positive numbers are:")
while(n<len(l)):
     if l[n]>=0:
        print(l[n],end=" ") 
    n=n+1

#SQUARE OF N NUMBERS
m=int(input("\nEnter the limit:"))
s=[x**2 for x in range(m)]
print("Square of numbers is",s)

#FORM A LIST OF VOWELS SELECTED FROM A GIVEN WORD
a=input("Enter a word:")
x={x for x in a if x in 'aeiou'}
print("Vowels are:",x)

#LIST ORDINAL VALUE OF EACH ELEMENT OF A WORD
r=input("Enter the word:")
o=[ord(x) for x in r]
print("Ordinal values are:",o)
