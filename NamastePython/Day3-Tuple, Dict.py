#tuple
a = (1,2,3)
# tuples are immutable
#a[1] = 5
a=('CSK','MI')



#dictionaries
ipl = {
"CSK" : "Chennai Super Kings",
"MI" : "Mumbai Indians"
}

ipl["CSK"]

ipl["GT"] ="Gujrat Titans"
ipl["CSK"]="Chennai"

del ipl["CSK"]

ipl = {
"CSK" : {"Name":"Chennai Super Kings","captain":"MSD"},
"MI" : {"Name":"Mumbai Indians","captain":"Rohit"},
"RCB" : {"Name":"Royal Challengers bangalore"}
}

ipl1 = {
"CSK" : {"Name":"Chennai Super Kings","captain":["MSD","Jadeja"]},
"MI" : {"Name":"Mumbai Indians","captain":"Rohit"},
"RCB" : {"Name":"Royal Challengers bangalore"}
}



# 4- create a dictionary to store following attributes of CSK 
# key "CSK" ; attributes : team full name , captain , playing 11 for each match(name of players), oppenont name (assume there are 3 matches only against MI, RCB , GT ) and result won/loss

# solution:

# Create a dictionary for CSK
csk = {
    "team_name": "Chennai Super Kings",
    "captain": "MS Dhoni",
    "playing_11": [
        ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11"],  # Match 1
        ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11"],  # Match 2
        ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11"],  # Match 3
    ],
    "opponents": ["MI", "RCB", "GT"],
    "results": ["Won", "Loss", "Won"]
}

#Note: there can be other way of storing the same information and that is also fine based on your end goal.

# 5- in the previous dictonary add one more item for RCB. you can choose any 3 opponents.

IPL = {"CSK":{
    "team_name": "Chennai Super Kings",
    "captain": "MS Dhoni",
    "playing_11": [
        ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11"],  # Match 1
        ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11"],  # Match 2
        ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11"],  # Match 3
    ],
    "opponents": ["MI", "RCB", "GT"],
    "results": ["Won", "Loss", "Won"]
},
"RCB":{
    "team_name": "Royal Challengers Bangalore",
    "captain": "Virat Kohli",
    "playing_11": [
        ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11"],  # Match 1
        ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11"],  # Match 2
        ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11"],  # Match 3
    ],
    "opponents": ["MI", "CSK", "GT"],
    "results": ["Loss", "Loss", "Loss"]
}

}



# 8- write a program to convert above universities list to a dictionary. the keys should be the name of the university

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

universities_dict = {}
for university in universities:
    name = university[0]
    attributes = {
        'total_students': university[1],
        'tuition_fees': university[2]
    }
    universities_dict[name] = attributes




