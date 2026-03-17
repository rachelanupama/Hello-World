#list comprehension
#every list comprehension can be rewritten as a for loop but every for loop cant be rewritten in list comprehension

#a = ['rachel','anupama']
'''b= str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=" ")'''

#syntax
#a = [expression for var in collection/range]

'''b = [i.upper() for i in a]
print(b)'''

'''a =  ["vja","hyd","vsg"]
b = [i.title() for i in a]
print(b)'''

'''a = [2,4,6,8,12,13]
b = [ i*i for i in a]
b = [i ** 2 for i in a]
b = [pow(i,2) for i in a]
print(b)'''

#if in list comprehension
'''a = [i for i in range(16) if i%2==0]
print(a)'''

'''fruits = ["apple", "banana","mango","kiwi","berry","grapes"]
b = [i for i in fruits if "a" in i ]
print(b)'''

#no elif usage in list comprehension
#if else

'''a = [i*i if i%2 == 0 else i*5 for i in range(21)]
print(a)'''

'''a = [1,2,3,4,5]
b = [5,4,3,2,1]
c = [a[i]+b[i] for i in range(len(a))]
d = [a[i]+b[i] for i in range(5)]
print(c)'''

#max,min,sum
'''print(max(3,4,5,6))

print(min(2,3,4,5,6))

print(sum(1,2,3,4))''' #error

'''a=1,2,3,4,5
print(sum(a))
print(sum([1,2,3,4,5]))'''
































