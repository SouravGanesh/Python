#control flow using if else
# less than 30 -> fail , else pass
marks=-20
if marks < 30 :
    print("fail")
    print(f"marks are {marks}")
elif marks >=30 and marks < 60:
    print("pass with second division")
elif marks >=60 and marks < 75:
    print("pass with first division")
else:
    print("pass with distinction")
print("this is outside if")

if "CSK" in ipl :
    print("CSK is there")
else:
    print("CSk is not there")
print("this is outside if")



# loops
num_square=[]
num=[1,2,3]


#while
num_square=[]
n=0
while n < len(num) :
    print(f"it is still less than 5 iteration number {n}")
    num_square.append(pow(num[n],2))
    n=n+1
# for loops

num_square=[]
for n in num :
    num_square.append(pow(n, 2))
    print(n)

#[1,2,3]
num_square=[]
for n in range(len(num)):
    print(f"it is still less than 5 iteration number {n}")
    num_square.append(pow(num[n], 2))


# 6- write a program to take a positive number as input from user. if the user enters negative number then keep promting him to enter positive number until he enters the positive number and then print the same:

# solution:
# Prompt the user to enter a positive number
number = int(input("Enter a positive number: "))

# Keep prompting until a positive number is entered
while number <= 0:
    print("Invalid input. Please enter a positive number.")
    number = int(input("Enter a positive number: "))

# Print the positive number
print("The positive number you entered is:", number)







# 2- given below dictonaries of states and their capital:

# capitals_dict = {
# 'Alabama': 'Montgomery',
# 'Alaska': 'Juneau',
# 'Arizona': 'Phoenix',
# 'Arkansas': 'Little Rock',
# 'California': 'Sacramento',
# 'Colorado': 'Denver',
# 'Connecticut': 'Hartford',
# 'Delaware': 'Dover',
# 'Florida': 'Tallahassee',
# 'Georgia': 'Atlanta',
# }

# pick a state from above dictonary and ask user to enter the capital of the state.If the user answers incorrectly, then repeatedly ask them
# for the capital until they either enter the correct answer or type "exit".
# If the user answers correctly, then display "Correct" and end the program. However, if the user exits without guessing correctly, display
# the correct answer and the word "Goodbye".

# Note: Make sure the user isn’t punished for case sensitivity. In other words, a guess of "Denver" is the same as "denver". Do the same for exiting—"EXIT" and "Exit" should work the same as "exit".

# solution:
capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta'
}

state = input("Pick a state from the dictionary: ")
state = state.capitalize()  # Convert the input to capitalize for case insensitivity

while True:
    if state in capitals_dict:
        capital = capitals_dict[state]
        guess = input("Enter the capital of {}: ".format(state))
        guess = guess.capitalize()  # Convert the guess to capitalize for case insensitivity

        if guess == capital:
            print("Correct!")
            break
        elif guess.lower() == 'exit':
            print("The correct answer was: {}".format(capital))
            print("Goodbye!")
            break
        else:
            print("Incorrect. Try again or type 'exit' to quit.")
    else:
        print("Invalid state. Please pick a state from the dictionary.")
    
    state = input("Pick a state from the dictionary: ")
    state = state.capitalize()



# 3- write a program to take state as input from user and print the capital of the state using above dictonary. If the state is not there in dictonary then print "sorry , information not available"

capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta'
}

state = input("Enter a state: ")
capital = capitals_dict.get(state.capitalize())

## note here we are using capitals_dict.get function instead of capitals_dict['state']. the advantage of using this method it wont throw error if key is not present in the dictonary. it will only return None.

if capital:
    print("The capital of {} is {}.".format(state, capital))
else:
    print("Sorry, information not available.")


# 4- Let say You have one 100 cats.
# One day, you decide to arrange all your cats in a giant circle. Initially,none of your cats has a hat on.
# You walk around the circle a 100 times, always starting with the first cat (cat #1). 
# Each time you stop at a cat, you check if it has a hat on. If it doesn’t, then you put a hat on it. If it does, then you take the hat off.

# 1. The first round, you stop at every cat, placing a hat on each one.
# 2. The second round, you stop only at every second cat (#2, #4, #6,
# #8, and so on).
# 3. The third round, you stop only at every third cat (#3, #6, #9, #12,
# and so on).
# 4. You continue this process until you’ve made one hundred rounds
# around the cats. On the last round, you stop only at cat #100.


# Write a program that simply outputs which cats have hats at the end.

# solution:

# by default all are set to false since none have been visited
array_of_cats = [False] * (100 + 1)
cats_with_hats_on = []
# We want to walk around the circle 100 times
for num in range(1, 100 + 1):
    # Each time we walk around, we visit 100 cats
    for cat in range(1, 100 + 1):
        # Determine whether to visit the cat
        # Use modulo operator to visit every 2nd, 3rd, 4th,... etc.
        if cat % num == 0:
            # Remove or add hat depending on
            # whether the cat already has one
            if array_of_cats[cat] is True:
                array_of_cats[cat] = False
            else:
                array_of_cats[cat] = True

    # Add all number of each cat with a hat to list
    for cat in range(1, 100 + 1):
        if array_of_cats[cat] is True:
            cats_with_hats_on.append(cat)
