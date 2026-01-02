a=5
b=""
for i in range(1,a+1):
    b += str(i)
    print(b)
b1 = ""
z=" "

s=( a//2 ) + 1
f=" "

for j in range(1,a+1):
    b1 += str(j)
    y=" "*s
    z = y
    s -= 1
    y.replace(" ","")
    
    print(z,b1[::-1])
