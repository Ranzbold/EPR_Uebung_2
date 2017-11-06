__author__ = "6611082: Cedric Reuter"


def kontrollstrukturen():
    num = input('--> ')
    if(not num.isdigit()):
        print("ERROR")
        return
    num = int(num)
    strnum = str(num)
    if ((not num > 0) or (not num <= 999)):
        print("ERROR")
        return
    if (((num % 3 == 0) or ("3" in strnum)) and
            ((num % 7 == 0) or ("7" in strnum))):
        print("fizzbuzz")
        return
    elif ((num % 3 == 0) or ("3" in strnum)):
        print("fizz")
        return
    elif ((num % 7 == 0) or ("7" in strnum)):
        print("buzz")
        return
    else:
        print(num)

kontrollstrukturen()
