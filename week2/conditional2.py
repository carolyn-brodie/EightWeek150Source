## Conditional

score = int(input("Enter test score: "))
if score > 90:
    print("Your grade is A")
elif score > 80:
    print("Your grade is B")
    print("You missed an A by ", str(91 - score))
elif score > 70:
    print("Your grade is C")
    print("you missed an A by ", str(91 - score))
else:
    print("you missed an A by ", str(91 - score))
            
          
            
##score = int(input("Enter test score: "))
##if score > 90:
##    print("Your grade is A")
##elif score > 80:
##    print("Your grade is B")
##elif score > 70:
##    print("Your grade is C")  
##else:
##    print("Another Grade")
##if score <= 90:
##    print("You missed an A by ", str(91 - score))
    
