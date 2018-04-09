name = ''
while not name:
    print("Enter your name")
    name = input()
print("How many guests will you have?")
num_guests = int(input())
if num_guests:
    print("Be sure you have enough room")
print("Done")