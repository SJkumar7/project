""""" 1 conditional stmts"""""

"if stmt"



''''print("begin")
i=input("enter a integer number")
x=int(i)

if x<10:
    print("this a valiad number")
    print("end")
'''''


"""this is else stmt"""



"""print("begin")
i =input ("enter a singe digit number ")
x=int(i)

if x<10:
    print("this is 1 digit number")

else:
    print("this is a 2 digit number")
    print("end")"""


"""elif stmt"""

"""e=input("this is a positive no")
c=int(e)

if c<10:
    print("given no is 1 digit number")

elif c<100:
    print("given no is 2 digit no")

elif c<1000:
    print("given no is 3 digit no")

else :
    print("given no is >=4 digit no")
    print("end")"""



""" 2 . looping stmts """

"""  while loop """

"""print("begin")
i=1
while i<=100:
    print("welcome",i)
    i=i+1
print("end")"""



"""  while-else """

""""print("begin")
i=1
while i<=5:
    print("welcome",i)
    i=i+1
else :
    print("this is a else condition")
print("end")"""



""" while ex -2"""

"""print("begin")
i=1
sum=0

while i<=10:
    sum=sum+i
    i=i+1
print(sum)
print("end")"""




"""  break   """

"""print("begin")
i=1
while i<=10:
    print("jagadeesh",i)

    if i==5:
      break
    i=i+1

else :
    print("thi is a else condition")

print("end")"""



"""  continue  """

"""print("begin")
i=5
while i<10:
    i=i+1
    if i==6:
        continue
    print("jagadeesh",i)
print("end")"""

"""example"""

"""while True:
    name=input("enter user name")
    if name!='jagadeesh':
        continue

    password=input('hello what is a password')
    if password =='sjk':
        break

    print('acess granted')"""




"""   for loop  """

'''s='jagadeesh'
for p in s:
    print(p*8)'''



"""  range fun """

'''x=range(5)
for p in x:
    print(p)'''

'''h=range(20,30,2)
for p in h:
    print(p)'''


'''t=range(30,40,3)
for i in t:
    print(i)

t=range(60,50,-3)
for i in t:
    print(i)'''

t = range(50, 40, 3)
for i in t:
    print(i)
    