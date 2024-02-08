'''
We have 2 variables, a and b, and we want to swap their values.
variable a = 10 and variable b = 20

rules:
1. variable a and b can't be directly assgined an integer 
    example: a = 20, and b = 10

result:
print(a) # 20
print(b) # 10
'''

a = 10
b = 20

#1st solution

##a = a+ b # a=30
##b = a- b # b= 10
##a = a-b # a=20
##
##print(a)
##print(b)
##
###2nd solution
##
##c = (a+b)/2 #c=15
##d = (a-b)/2 #d=-5
##a = c-d # a = 20
##b = c+d # b=10
##print(a)
##print(b)

#3rd solution
a,b = b,a
print(a)
print(b)

#4th solution

c = a #c=10
a = b #a=20
b = c #b= 10

print(a)
print(b)

