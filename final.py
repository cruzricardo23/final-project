#Ricardo Cruz
#Final 1/28/26


print("option 1")
print("option 2")
print("option 3") 



answer = int(input ("select an option"))


if (answer ==1):
    name =input ("what is your name?")
    print (name, "what kind of name is that?") 




elif (answer ==2):
    for i in range (20):
     print ("pizza", i)

elif (answer ==3):
    x = 0
    secret = 6
    while x != secret: 
        x = float(input("guess a number between zero and ten..."))


        if x < secret:
            print ("go higher") 

        elif x > secret: 
            print("Go lower") 
            
        else:
            print("GOT IT") 
            

