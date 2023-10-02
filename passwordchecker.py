# password checker

username= input("Enter your Username : ")

password = input("Enter your password : ")
length = len(password)

print(f"{username}, your password { '*' * length } is {length} letters long ")

option= input("Would you like to view your password?  ")
if option == "yes" :
    print("Answer this riddle, What has many keys but can’t open a single lock?")
riddle = input()
if riddle.lower() == "piano" :
    print(f"Ding Ding Ding, Your password is: {password}")
else:
    print("Okay, wrong answer, you cant see the password")

if option == "no" :
    print ("Okay, have a good day")