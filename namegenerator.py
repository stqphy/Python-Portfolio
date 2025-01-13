#Name Generator Project
#Stephy

print("Welcome to Crumbl Cookie 2000!")
print("Answer the questions to find out which Crumbl Cookie you are!")
ans = input("chocolate or vanilla?")
if ans == "chocolate":
    ans = input("cookie or brownie?")
    if ans == "cookie":
        ans = input("includes chocolate chip cookie (yes) or doesn't include chocolate chip cookie (no)?")
        if ans == "yes":
            print("You are a Brookie!")
        else:
            print("You are a Cookie Dough Cookie!")
    else:
        ans = input("rainbow or no rainbow?")
        if ans == "rainbow":
            print("You are a Cosmic Brownie!")
        else:
            print("You are a Double Fudge Brownie!")



if ans == "vanilla":
    ans = input("ice cream or cake?")
    if ans == "ice cream":
        ans = input("strawberry or mint?")
        if ans == "strawberry":
            print("You are a Strawberry Ice Cream Bar Cookie!")
        if ans == "mint":
            print("You are a Mint Chip Ice Cream Bar Cookie!")
    if ans == "cake":
            ans = input("milk or berry?")
            if ans == "berry":
                print("You are a Berry Trifle Cake Cup!")
            else:
                print("You are a Tres Leches Cake!")
