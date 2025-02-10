import random
d = ["+","-","*","/"]
Grade = int(input("Enter your grade\n"))
if Grade > 6 and Grade < 10:
    Attendannce = int(input("Enter your attendance out of 200 days\n"))
    Medical = int(input("How many of these days were medical leaves?\n"))
    if 200 - (Attendannce + Medical) < 51:
        print("You may take the examination.")
        for i in range (6):
            a =(random.randint(1,200))
            b =(random.randint(1,200))
            c =(d[random.randint(0,3)])
            print(a,c,b)
    else:
        print("You are not eligible for the examination.")
else:
    print("You are not eligible for the examination.")