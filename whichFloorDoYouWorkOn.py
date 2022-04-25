floor =  int(input("Which floor do you work on?: "))
maximumStories =  26

while floor >= maximumStories:
    print("You entered:", floor, "but there are only", maximumStories, "in this building. Try again.")
    floor =  int(input("Which floor do you work on?"))

print("Congrats! You work on floor", floor)