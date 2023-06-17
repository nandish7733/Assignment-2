n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number"))
#Arithmetic operators
print("Arithmetic operators:")
print("Addition=",n1+n2)
print("Subtraction=",n1-n2)
print("Multiplication=",n1*n2)
print("Division=",n1/n2)
print("Modulus=",n1%n2)
print("Floor division=",n1//n2)
print("Exponential=",n1**n2)
#Assignment operators
print("Assignment operator:")
n3=int(input("Enter number for Assignment operator:"))
print("'=' operator=",n3)    
n3+=15
print("'+=' n3+=15=",n3)
n3-=10
print("'-=' n3-=10=",n3)
n3*=2
print("'*=' n3*=2=",n3)
n3/=2
print("'/=' n3/=2=",n3)
n3%=2
print("'%=' n3%=2=",n3)
n3//=2
print("'//=' n3//=2=",n3)
#Comparison operators
print("Comparison Operators:")
print("'>' n1>n2=",n1>n2)
print("'<' n1<n2=",n1<n2)
print("'==' n1==n2=",n1==n2)
print("'!=' n1!=n2=",n1!=n2)
#Logical operators
print("Logical operators:")
print("'and' n1 and n2=",n1 and n2)
print("'or' n1 or n2==",n1 or n2)
print("'not' not n3=",not n3)
#Bitwise operators
print("Bitwise operators:")
print("'|' n1|n2=",n1|n2)
print("'&' n1&n2=",n1&n2)
print("'^' n1^n2=",n1^n2)
print("'<<' n1<<2=",n1<<2)
print("'>>' n2>>2=",n2>>2)
#Identity operators
print("Identity operator:")
Y="yousuf"
print("String Y=",Y)
print("'is' 'y' is Y=", 'y' is Y)
print("'is not' 'a' is not Y=",'a' is not Y)
#Membership operators
print("Membership operator:")
Z="yousuf"
print("String Y=",Y)
print("String Z=",Z)
print("'in' 'y' in Z=",'y' in Z)
print("'not in' 'e' not in Z=",'e' not in Z)