print("Welcome to the quiz game")

ch=input("Do you want to play: yes/no")
if ch.lower()!="yes":
    quit()
print("Ok, then let's play")

count=0
q1=input("What is the full form of CPU?")
if q1.lower() =="central processing unit":
    count+=1
    print("Correct!")
else:
    print("Sorry, incorrect!")


q2=input("What is the full form of GPU?")
if q2.lower() =="graphics processing unit":
    count+=1
    print("Correct!")
else:
    print("Sorry, incorrect!")


q3=input("What is the full form of RAM?")
if q3.lower() =="random access memory":
    count+=1
    print("Correct!")
else:
    print("Sorry, incorrect!")

q4=input("What is the full form of ROM?")
if q4.lower() =="read only memory":
    count+=1
    print("Correct!")
else:
    print("Sorry, incorrect!")

print("You answered " + str(count) + " questions correct")
print("Your quiz percentage is "+ str((count/4)*100) +" %")
