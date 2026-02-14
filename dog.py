class dog:
    animal="DOG"
    def __init__(self,b,c):
        self.b=b
        self.c=c
dog1=dog("BEAGLE","BROWN-WHITE")
dog2=dog("GOLDEN RETRIVER","GOLDEN")
print("BREED:",dog1.b,",","COLOR:",dog1.c)
print("BREED:",dog2.b,",","COLOR:",dog2.c)