num=int(input("Enter a number:"))
d=0
while num>0:
    digit=num%10
    if str(digit).isdigit():
        d += 1
    num //= 10
print(d)
