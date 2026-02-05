d={"Codingnal":3,"is":2,"best":2,"for":2,"coding":1}
c=int(input("Enter the number you want to check 1/2/3:"))
ch=0
for key,value in d.items():
    if d[key] == c :
        ch += 1
print(ch)