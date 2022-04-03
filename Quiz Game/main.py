# --------------------------- Welcome To Python Quiz Game ---------------------------
name = input("Enter Your name: ")
gender = input("Enter your Gender(m/f)? ")
if gender == 'm':
    print("Welcome Mr." + name +" to quiz game!!\nWe'll try to defeat you so best of luck !!!!")
elif gender == 'f':
    print("Welcome Ms." + name + " to quiz game!!\nWe'll try to defeat you so best of luck !!!!")
total = 3 ; points = 0
qanswer = input("Q#1: What is your Favourite programming Language? ")
if qanswer.lower() == 'python':
    points += 1
    print("Correct Answer!!")
else:
    print("Wrong Answer!!")
qanswer = input("Q#2: Who is your Favourite Programmer? ")
if qanswer.lower() == 'junaid':
    points += 1
    print("Correct Answer!!")
else:
    print("Wrong Answer!!")
qanswer = input("Q#3: Can You understand Junaid's Codes? ")
if qanswer.lower() == 'yes':
    points += 1
    print("Correct Answer!!")
else:
    print("Wrong Answer!!")
print("Thanks!! For your Patience!!. You attempted ", points, " questions correctly!!")
score = (points/total)*100
print("Points Scored are: ", score)
print("See you Later!!!")