# a=[1,23,4,5]
# pn=[x for x  in a if all(x%d!=0 for d in range (2,(x//2)+1))]
# print(pn)
# def square(n):
#     return n*n
# num=[1,3,5,99]
# s=map(square,num)
# print(list(s))
# def sum(x,y):
#     return x+y 
# a=[1,2]
# b=[3,4]
# print(list(map(sum,a,b)))
# for i in range(1,11):
#     if i == 5 :
#         exit()
#    print(i)
# l=[1,2,3,44,5,6]
# l2=[4,5,6,7]
# l3=zip(l,l2)
# print(list(l3))
# l1=[1,2,3,4,5]
# l2=[10,100,1100,123,145]


# print(list(zip(l1,l2[::-1])))


d=[1,2,3]
d2=[4,5,6]
print(dict(zip(d,d2)))