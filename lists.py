# empty list :
# a=[]

# list with elements:
# b=["a",1,1.5]

# using a operator *
# c=[1,3,5]
# print(c*3)

# reversing a list
# d=["b",2,3,4]

# print(d[::-1])

# l=["a","b","aba","aaa","abc"]
# n=0
# c=[]
# for i in l:
#     if len(i) >= 2 and i[0]==i[-1]:
#         c.append(i)
#         n += 1
# print(c)
# print(f"No of string with the last letter and the first letter same is {n}.")

a=[2,1,4,3,5,7,6]
sum=0
for i in a:
    sum += i
aver=sum/len(a)
print(f"Sum={sum}")
print("Average=",aver)
b=[]

print(a.sort())
b = b+a
print(b)
print(a[0])
print(a[-1])

        