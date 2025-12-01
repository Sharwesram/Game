import time
print("Welcome to the quiz game! ")

name=input("Enter your name:")
time.sleep(0.1)
print("Hello",name,"common let's begin with the quiz")
time.sleep(1)
print("Each correct answer carries 1 score")
time.sleep(2)

print("Each answer starting letter should be in capital")
time.sleep(3)
print("Don't give the answer in full caps!")
b=0

print("Q.1: What is India's national animal?")
a=input("Answer:")
if(a=="Tiger" or a=="tiger"):
    print("you are right!")
    b += 1
    
else:
    print("You are wrong. The answer is Tiger. Better luck next time!")

    
print("Q.2: What is 99*99?")
c=input("Answer:")

if(c=="9801"):
      print("You are right!")
      b += 1
      
else:
    print("You are wrong. The answer is 9801. Better luck next time!")

print("Q.3: Who is the richest person in the world?")
d=input("Answer:")
   
if(d=="Elon Musk" or d=="elon musk" or d=="Elon musk" or d=="Elonmusk" or d=="elonmusk"):
    print("You are right!")
    b += 1
    
else:
    print("You are wrong. The answer is Elon Musk. Better luck next time!")

print("Q.4: When is national sports day celebrated in India?")
e=input("Answer:")
if(e=="August 29" or e=="august 29" or e=="August29" or e=="august29"):
    print("you are right!")
    b += 1
else:
    print("You are wrong. The answer is August 29. Better luck next time!")

print("Q.5: What is square of 3,249? ")
f=input("Answer:")
if(f=="57"):
    print("you are right!")
    b += 1
else:
    print("You are wrong. The answer is 57. Better luck next time!")

print("Q.6: What is the world's largest lake?")
g=input("Answer:")
if(g=="Caspian Sea" or g=="Caspian sea" or g=="Caspiansea" or g=="caspian sea" or g=="caspiansea"):
    print("You are right!")
    b += 1
else:
    print("You are wrong. The answer is Caspian sea. Better luck next time!")

print("Q.7: Which continent contains most countries?")
h=input("Answer:")
if(h=="Africa" or h=="africa"):
    print("You are right!")
    b += 1
else:
    ("You are wrong. The answer is Africa. Better luck next time!")
    
print("Q.8: Which continent has the most people per square mile?")
i=input("Answer:")
if(i=="Asia" or i=="asia"):
    print("You are right!")
    b += 1
else:
    print("You are wrong. The answer is Asia. Better luck next time!")
    
print("Q.9: With which organ does a snake hear?")
j=input("Answer:")
if(j=="Tongue" or j=="tongue"):
    print("You are right!")
    b += 1
else:
    print("You are wrong. The answer is Tongue. Better luck next time!")

print("Q.10: How many stars are there in the american flag?")
k=input("Answer:")
if(k=="50"):
    print("You are right!")
    b += 1
else:
    print("You are wrong. The answer is 50. Better luck next time!")

print("Your score=",b)
percentage1=b/10
p2=percentage1*100
print("Your percentage=",p2)

if(p2>=50):
    print("YOU ARE GOOD AT GENRAL KNOWLEDGE QUIZ")
elif(p2<50):
    print("YOU ARE NOT GOOD AT GENRAL KNOWLEDGE QUIZ")



