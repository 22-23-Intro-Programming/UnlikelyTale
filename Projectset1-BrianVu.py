

'''def isMultiple(a, b):
    if a%b == 0:
        print(b, "is a multiple of", a)
    else:
        print(b, "is not a multiple of", a)
for f in range(2):
    choose = int(input("type 1(Name) or 2(Number): "))

    if choose == 1:
        name = input("Please enter your name: ")
        print("Oh,"+name+", is it? It is nice to meet you!")
        print("Have a good day "+name)
 
    elif choose == 2:
        a = int(input("type the larger number: "))
        b = int(input("type the lower number: "))
        isMultiple(a, b)'''

def Palindrome(string):
    large = len(string)
    g = 0
    h = large - 1
    while g < h:
        if string[g]  != string[h]:
            print ("False")
            break
        g = g + 1
        h = h - 1
    print ("True")
def l():
            Palindrome("racecar")
l()

print("-----------------------")
    
