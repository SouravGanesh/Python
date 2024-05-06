# 1- create a txt file and put 4-5 lines. Now create another file from the previous file and at the end of each line put the count of words.

# example :
# file 1:
# this is namaste sql course
# this is python course
# this assinment is part of day4 lecture


# file2:this is namaste sql course:5
# this is python course:4
# this assignment is part of day4 lecture:7

# solution:
# Create the first file and write lines into it
with open('file1.txt', 'w') as file1:
    lines = [
        "this is namaste sql course",
        "this is python course",
        "this assignment is part of day4 lecture"
    ]
    for line in lines:
        file1.write(line + '\n')

# Create the second file with word count at the end of each line
with open('file1.txt', 'r') as file1, open('file2.txt', 'w') as file2:
    for line in file1:
        line = line.strip()
        word_count = len(line.split())
        file2.write(line + ':' + str(word_count) + '\n')

print("File creation and word count operation completed!")