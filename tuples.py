# t1=(1,2.5,"abc")
# t2=(1,2,3)
# print(t1)
# print(t2)
# t3=(9,)
# print(t2+t3)
# c=0
# t4=(1,2,3,2,2)
# print(t4.count(2))
# t5=(1,2,3,4)
# print(t5[1:3])
# t6=(1,2,3,3,2,1)
# t7=(t6[::-1])

# if t6==(t7):
    # print("Palindrome")

wheather=(1, 0, 1,1, 1, 1, 0)
rainy=0
sunny=0
for i in wheather:
    if i==1:
        rainy += 1
    else:
        sunny += 1
if rainy > sunny:
    print("Todays wheather will be rainy.")
else:
    print("Todays wheather will be sunny.")