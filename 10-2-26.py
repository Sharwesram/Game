# 1 :
# n=int(input("Enter a num:"))
# on=[x for x in range(1,n+1) if x % 2 == 1]
# print(on)

# 2 :
fruits=["apple","orange","mango","pineapple","watermelon"]
upd_val=[x[0].upper() + x[1:] for x in fruits]


print(upd_val)