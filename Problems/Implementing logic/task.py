try:
    name, surname = input().split()
except:
    print("You need to enter exactly 2 words. Try again!")
else:
    print("Welcome to our party, " + name + " " + surname)
