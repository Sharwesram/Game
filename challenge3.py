# class overload:
#     def __init__(self,x):
#         self.x=x
        
#     def __gt__(self, other):
#         if (self.x<other.x):
#           return(other.x)
#         else:
#             return(self.x)
        
# o=overload(5)
# o1=overload(3)
# print(o>o1)

# class falshcard:
#     def __init__(self,word,meaning):
#         self.word=word
#         self.meaning=meaning
#     def __str__(self):
#         return "(" +self.word  + self.meaning+")"
#     def dis(self):
#       while True:
       
        
#         print(f"Word:{self.word}\nMeaning of {self.word}:{self.meaning}")
#         break
# w=str(input("Enter a word:"))
# mean=str(input(f"Enter the meaning of the word {w}:"))
# ob1=falshcard(w,mean)
# ob1.dis()

class fruit:
    def __init__(self,f1,f2,f3,c1,c2,c3):
        self.f1=f1
        self.f2=f2
        self.f3=f3
        self.c1=c1
        self.c2=c2
        self.c3=c3
    def quiz(self):
        p=0
        ans=str(input(f"Enter the color of the fruit {self.f1}:"))
        if ans==(self.c1):
            p+=1
        a=str(input(f"Enter the color of the fruit {self.f2}:"))
        if a==(self.c2):
            p+=1
        a1=str(input(f"Enter the color of the fruit {self.f3}:"))
        if a1==(self.c3):
            p+=1
        print(f"Your points={p}")
o=fruit("apple","gauva","banana","red","green","yellow")
o.quiz()


    