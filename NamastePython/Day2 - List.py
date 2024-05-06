#method 1
ipl = ['CSK', 'MI', 'RCB', 'LSG']
print(type(ipl))
#indexing
print(ipl[1])

#slicing
print(ipl[1:])
ipl[1] = 'KKR'
ipl.append('KKR') #add element at the end
ipl.insert(2,'MI') #insert element at particular index
ipl.extend([1,2]) # extent list with another list

# method 2 to create list
ipl_string = "CSK,MI,KKR,LSG"
ipl_list= ipl_string.split(",")


#method 3
python_list = list('python ')

# to remove element at any index use pop..by default it removes last value
ipl.pop(2)

num = [1,2,3,5,4]
print(sum(num))
print(min(num))



# 1- write a program which takes single input from user contaning first name,last name and age as comma separated value and display then in 3 lines in given format below.

# example user input : Ankit,Bansal,35

# output:
# First name is Ankit
# last name is Bansal
# Ankit is 35 years old 

# note : do not hardcode name at any place

# solution:

user_input = input("Enter first name, last name, and age (comma-separated): ")

# Split the input into first name, last name, and age
first_name, last_name, age = user_input.split(',')

#Note how we can assign each element of list to 3 different variables with direct assignment. The number of variables and and length of list should be same. this is also known as unpacking and it works with tuples as well (tuples you will learn in next lecture)

# Alternatively we can do using indexing 
input_list=user_input.split(',')
first_name = input_list[0]
last_name = input_list[1]
age = input_list[2]


# Display the information
print("First name is", first_name)
print("Last name is", last_name)
print(first_name, "is", age, "years old.")



# 2- given 2 list as list1= [1,3,4] and list2 = [2,4,6]

# combined the 2 list and diplay the same without using extend method

# solution:

list1 = [1, 3, 4]
list2 = [2, 4, 6]

combined_list = list1 + list2

print("Combined list:", combined_list)


# 3- given a list list1=[1,2,3,4,5,6,7,8]
# display a new list which contains only odd position index values from above list.

# solution 1:
list1 = [1, 2, 3, 4, 5, 6, 7, 8]

odd_position_values = list1[1::2]

print("New list with odd position values:", odd_position_values)

# NOTE:

# Here's how the slicing notation [1::2] works:

# The first value before the first colon (1 in this case) represents the starting index of the slice. It indicates that the slicing should start from index 1.

# The second value after the first colon and before the second colon (empty in this case) represents the ending index of the slice. Since it is empty, it indicates that the slicing should continue till the end of the list.

# The third value after the second colon (2 in this case) represents the step size. It indicates that the slicing should select every second element in the specified range.

# Combining these values, [1::2] means that we start the slicing from index 1, continue till the end of the list, and select every second element along the way.

# solution 2: using loops that you will learn in day3 lecture.

list1 = [1, 2, 3, 4, 5, 6, 7, 8]

odd_position_values = []
for i in range(len(list1)):
    if i % 2 != 0:
        odd_position_values.append(list1[i])

print("New list with odd position values:", odd_position_values)



# 4- ipl= ['CSK','MI','KKR','LSG','PBKS']

# take a ipl team name as input from user and display a list of all elements from that name.

# example : input : KKR
# output : ['KKR','LSG','PBKS']

# solution:


team_name = input("Enter the IPL team name: ")

team_index= ipl.index(team_name)

print("List of elements from the team name:", ipl[team_index:])



# 5- ipl= ['CSK','MI','KKR','LSG','PBKS']

# take a ipl team name as input from user and display a list of all elements except input one

# example : input : KKR
# output : ['CSK','MI','LSG','PBKS']

# solution:
ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']

team_name = input("Enter the IPL team name: ")

team_elements = ipl.copy()
team_elements.pop(ipl.index(team_name))

print("List of elements except the input team:", team_elements)



# 6- ipl= ['CSK','MI','KKR','LSG','PBKS']
# take a user input contains 2 comma seprated values index,new_team . replace the index element of list with new value and display the same

# example : input : 2,SRH
# output : ['CSK','MI','SRH','LSG','PBKS']

# solution:

ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']

user_input = input("Enter the index and new team (comma-separated): ")
index, new_team = user_input.split(',')

index = int(index)

ipl[index] = new_team

print("Updated list:", ipl)



# 7- ipl= ['CSK','MI','KKR','LSG','PBKS']
# take ipl team name as user input. display True if the team exists in ipl list else display False.

ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']

team_name = input("Enter the IPL team name: ")

team_exists = team_name in ipl

print(team_exists)



# 8-ipl= ['CSK','MI','KKR','LSG','PBKS']
# take a user input contains 2 comma seprated values index,new_team . Add the new value at that index in the list. 
# Display the old list , new list,length of original and new list

# example : input : 2,SRH
# output : 
# old list : ['CSK','MI','KKR','LSG','PBKS'] and length 5
# new list : ['CSK','MI','SRH','KKR',LSG','PBKS'] and length 6


# solution:

ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']

user_input = input("Enter the index and new team (comma-separated): ")
index, new_team = user_input.split(',')

index = int(index)

# Display the old list and its length
print("Old list:", ipl)
print("Length of the original list:", len(ipl))

# Add the new team at the specified index
ipl.insert(index, new_team)

# Display the new list and its length
print("New list:", ipl)
print("Length of the new list:", len(ipl))


# 1- given a list of numbers, write a program to find the mean of the numbers in list

# solution:
# Example list of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the mean of the numbers
total = sum(numbers)
mean = total / len(numbers)

# Display the mean
print("Mean:", mean)


# 2- given a list of numbers unsorted, write a program to find the median of the numbers in list

# solution :
# Example list of numbers
numbers = [5, 1, 3, 2, 4]

# Sort the list in ascending order
numbers.sort()

# Calculate the median
length = len(numbers)
if length % 2 == 0:
    median = (numbers[length//2 - 1] + numbers[length//2]) / 2
else:
    median = numbers[length//2]

# Display the median
print("Median:", median)




# 3- from a list of numbers create 2 list , one containing only the even numbers and other only the odd numbers

# solution:

# Example list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Iterate through the numbers and classify them as even or odd
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# Display the even numbers list
print("Even numbers:", even_numbers)

# Display the odd numbers list
print("Odd numbers:", odd_numbers)




# 10- write a program that finds the largest number in a list(unsorted) of integers without using sort/sorted method.
# solution:

numbers = [9, 4, 7, 2, 1, 5, 8, 3, 6]  # Example list of numbers

largest_number = numbers[0]  # Assume the first number is the largest

for number in numbers:
    if number > largest_number:
        largest_number = number

print("Largest number:", largest_number)



# 7- consider the below list of list conatins following information :

# 1. The name of a university 
# 2. The total number of enrolled students
# 3. The annual tuition fees

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

# write a program to print follwoing information :
# 1- a list of all the universitites  : ['California Institute of Technology','Harvard',..so on]
# 2- total number of student entrolled in all the unversities together 
# 3- mean of tuition fees

# solution:
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

# 1. List of all universities
university_names = []
for university in universities:
    university_names.append(university[0])
print("List of all universities:", university_names)

# 2. Total number of students enrolled in all universities
total_students = 0
for university in universities:
    total_students += university[1]
print("Total number of students enrolled in all universities:", total_students)

# 3. Mean of tuition fees
tuition_fees = []
for university in universities:
    tuition_fees.append(university[2])
mean_tuition = sum(tuition_fees) / len(tuition_fees)
print("Mean of tuition fees:", mean_tuition)