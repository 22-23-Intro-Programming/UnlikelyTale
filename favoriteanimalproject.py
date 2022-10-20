class Dog:

    def __init__(self, Name, Age):
        self.size = "small"
        self.age = 2
        self.color = "black"
        self.name = "Annie"

    def getAge(self):
        return self.age

    def getName(self):
        return self.name
    def getSize(self):
        return self.size
    def getColor(self):
        return self.color
    
def main():

    D = Dog()

    print("Hi dog, what is your name")

    print(D.getName())

    print("what is your age")

    print(D.getAge())

    print("what is your size")

    print(D.getSize())

    print("what is your color")

    print(D.getColor())
    
    
if __name__== "__main__":
    main()
