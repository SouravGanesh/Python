# Note 1: when taking user input using input() you can pass prompt to the user example
name=input("enter your name: ")


# 1- write a program which takes 2 inputs from the user : weight(kg) and height(meter) and prints the BMI in the output.

# BMI = weight / (square of height)

# solution:
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print("Your BMI is:", bmi)


# 2- write a program which takes the name of the user as input and replace all the occurence of character 'a' in the name to 'b' and print it.

# solution:
name = input("Enter your name: ")

new_name = name.replace('a', 'b')

print("Modified name:", new_name)


# 3- write a program which takes 2 inputs from user as principle amount (int) and rate of annual interest (float) and print the expected total amount  after  2 years.
#
# example : principle : 100 , interest percent 10  then amount after 2 years will be : 100*1.1*1.1 = 121
#
# solution:
principal = int(input("Enter the principal amount: "))
interest_rate = float(input("Enter the annual interest rate: "))

total_amount = principal * (1 + (interest_rate / 100)) ** 2

print("Expected total amount after 2 years:", total_amount)

# 4- write a program which takes city name from user input. irrespective of in which case user enters the city name, print the city name in camel case meaning first letter should be capital and rest in small.
#
# example : input : MYSORE ,  print - > Mysore
#
# solution 1:
city_name = input("Enter the city name: ")

# Convert the city name to lowercase
city_name = city_name.lower()

# Capitalize the first letter
city_name = city_name[0].upper() + city_name[1:]

print("City name in camel case:", city_name)



# solution 2:
city_name = input("Enter the city name: ")

# Convert the city name to lowercase
city_name = city_name.lower()

# Capitalize the first letter
city_name = city_name.capitalize()

print("City name in camel case:", city_name)



# 5- write a program which takes the name of the user as input and print the index of character 'a' in the string. if 'a' is not there then return -1.
#
# solution:

name = input("Enter your name: ")

index = name.find('a')


print("Index of 'a':" + str(index))



# 6-  Display the number of letters in the below string
my_word = "antidisestablishmentarianism"

solution : print(len(my_word))


# 7- take 3 inputs from user : first name , last name and age . Display the information in below format
# exmaple
# first name : MOhit
# last name : sharma
# age 32
#
#
# Display : my name is Mohit Sharma and I am 32 years old.
#
# note that first letter of first name and last name both should be in capital letters and rest in small.
#
# solution:
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")

# Format the first and last name with capitalizing the first letter
formatted_first_name = first_name.capitalize()
formatted_last_name = last_name.capitalize()

print("Display: My name is", formatted_first_name, formatted_last_name, "and I am", age, "years old.")

#please note above this is a new way to print along with variables using comma.


# 8-take 3 inputs from user : first name , last name and company name. create the email alias for the user and display it.  Email alias is first 2 letters of first name , last 3 letters of last name and @company.com
# example
# first name : MOhit
# last name : sharma
# company : infosys
#
# Display : morma@infosys.com
#
# note full email id should -be in lower case
#
# solution:

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
company_name = input("Enter your company name: ")

# Extract the required portions for the email alias
alias_first_name = first_name[:2].lower()
alias_last_name = last_name[-3:].lower()

# Create the email alias
email_alias = alias_first_name + alias_last_name + "@" + company_name.lower() + ".com"

print("Email alias:", email_alias)



# 9-  write a program that reverses a given string. For example, if the input is "Hello" from user, the output should be "olleH"

# solution 1 :
string = input("Enter a string: ")  # Get the string input from the user

reversed_string = ""
for char in string:
    reversed_string = char + reversed_string

print("Reversed string:", reversed_string)


# solution2 : using indexing (double colon):

string = input("Enter a string: ")  # Get the string input from the user

reversed_string = string[::-1]  # Use slicing to reverse the string

print("Reversed string:", reversed_string)




