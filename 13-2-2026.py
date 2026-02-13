import random
password=""
alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m", "n","o","q","r","s","t","u","v","w","x","y","z"]
upp_alpha=["A","B","C","D","E","F","G","H","I","J","K","L","M", "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
char=["*","#","_","-","@"]
for i  in range(1,5):
   num=random.randint(0,9)
   alp=random.choice(alphabets)
   upalp=random.choice(upp_alpha)
   c=random.choice(char)
   password += str(num)
   password += alp
   password += upalp
   password += c
print(f"Random password : {password}")