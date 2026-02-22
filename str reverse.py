class reverse:
    def __init__(self,s):
        self.s=s
    def rev(self):
        l=[self.s[::-1]]
        for i in l:
            print(i,end="")
    
st=str(input("enter a string:"))

ob1=reverse(st)
ob1.rev()