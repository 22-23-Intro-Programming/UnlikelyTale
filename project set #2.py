'''def factorial():
    num = int(input("enter your number: "))
    output = 1
    i = 0
    for i in range(num):
        output = output * (i+1)

    print(output)

    
factorial()'''


'''def double_char():
    
    char1 = input("enter a phrase")
    char2 = ""
    for i in char1:
        char2 = char2+ i*2
        print(char2)
double_char()'''

'''def camel_case():
    filename = ("classnotes 10/24/22")
    result = filename[-1]

    i = 0
    while (i < 11):

         if filename[i] == "/":
             filename = filename.replace(filename[i], "-") 
         i = i+1
    print(filename)
camel_case()'''

'''def main():
     newS = str(20/11)

    
     i = 0
     while (i < 11):

         while "/" in newS:
             newS = newS.replace(newS[i], "-") 
         i = i+1

     print(newS)'''


def main():
    newS = input("please enter your filename: ")
    length = len(newS)
    for i in range(length):
        a=0
        b = newS[a:a+1]
        if b=="/":
            newS.replace(newS,"-")
            print(newS)
                 
                 
                 









     
     

if __name__ == "__main__":
    main()
