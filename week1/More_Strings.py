theString = "abc"

#To get the number of characters use the len function
print(len(theString))

#To access the first character use index 0
print(theString[0])

#To access the second character use index 1
print(theString[1])

#two ways to get to the last character -which is index 2
print(theString[2])  ##This only works for strings of length 3
print(theString[len(theString)-1])  #Length of the string -1
print(theString[-1])