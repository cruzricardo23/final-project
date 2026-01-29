#Ricardo Ciruz
#Lab 6 



#function


def temp():
    question = int(input("enter current tempature in fahrenheit?"))
    celius = (question - 32) * (5/9) 
    print("this is convereted ",celius)




def question():
    while True:
        user_input = input("How old are you? (or type 'next question' to stop) ")
        if user_input == "next question":
            print("See you next time!")
            break
        age = int(user_input)
        if age < 50:  
            print("You are young")
        else:
            print("You are OLD")








name = input("What is your name")

print("_________MENU___________")
print("option 1")
print("option 2")
print("option 3")
print("option 4")
print("option 5") 
print("option 6")

answer = int(input("select an option"))

if (answer ==1):
    print("what is funnier than six seven?")
    print("a nine to five")


elif (answer ==2):
    for i in range(15):
        print(name,i)


elif (answer==3):
     number = int(input("enter a number"))
     for i in range(number):
      print("this is hard")

elif (answer ==4):
    x = 0
    secret = 8
    while x != secret:

         x = float(input("Guess a number between 1 and 20: "))
           
         if x < secret:
                print("go higher")
                  
           
         elif x > secret:
                 print("go lower")
           
         else:
             print("Correct......Game Over!")



elif (answer ==5):
     temp()


elif (answer ==6):
    question()


