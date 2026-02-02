t1=(4,3,2,2,-1,18)
t2=(2,4,8,8,3,2,9)
product=1
for i in t1:
    product *= i
print(f"The product of items in the tuple {t1} is {product}")
product2=1
for j in t2:
    product2 *= j
print(f"The product of items in the tuple {t2} is {product2}")