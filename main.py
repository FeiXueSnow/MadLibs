# Points to Start
points = 0

# Instructions
print("This is a Would - You - Rather - like game. Choose a letter and see if your choice was popular or unpopular.")

# Questions and Answers
question_1 = input("Cats (c) or Dogs (d)? ")
question_1 = question_1.lower
 
if question_1 == "c":
   print("Unpopular")
elif question_1 == "d":
   print("Popular!")
   points += 1
else:
   print("...")
   exit()
 
question_2 = input("Toilet Paper Under (u) or Toilet Paper Over (o)? ")
question_2 = question_2.lower
 
if question_1 == "u":
   print("Unpopular")
elif question_1 == "o":
   print("Popular!")
   points += 1
else:
   print("...")
   exit()
 
question_3 = input("Wii (W) or Xbox (X)? ")
question_3 = question_3.lower
 
if question_3 == "x":
   print("Unpopular!")
elif question_3 == "w":
   print("Popular!")
   points += 1
else:
   print("...")
   exit()

# Winning, Wosing, and Losing Status
if points == 3:
 print("You are totally in the mainstream!")
elif points == 2:
 print("You've got one outlier, but that's completely fine!")
else:
 print("You wanted to avoid the mainstream, huh?")