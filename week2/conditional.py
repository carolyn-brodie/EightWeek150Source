## Conditional

score = int(input("Enter test score: "))
if score > 90:
    print("Your grade is A")
else:
    if score > 80:
        print("Your grade is B")
        print("You missed an A by ", str(91 - score))
    else:
        if score > 70:
            print("Your grade is C")
            print("you missed an A by ", str(91 - score))
        else:
            print("you missed an A by ", str(91 - score))
input("Press enter to end")
            
          
            
