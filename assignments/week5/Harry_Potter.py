print("We are in the Gryffindor dorm. Despite of Harry's first day of school he overslept. \n "
      "Ron is freaking out, just imagining McGonagall's reaction on their delay. \n"
      "You need to help them ")


user_items = []
#dictonary with rooms
room_riddles_solved = {
    "Great Hall": False,
    "Forbidden Corridor": False,
    "Moaning Myrtle' Bathroom": False,
}

#setting room requirements
room_requirements = {
    "Great Hall" : {},
    "Forbidden Corridor": {"required_item": "Wand", "riddle_required": True},
    "Moaning Myrtle' Bathroom": {},
}

#Structure
if "Wand" in user_items:
    print ("Congratulations! You have entered the Forbidden Corridor. Footsteps appear in the distance\n"
           "It'll be Flinch. Let's see if you can find something useful to hide before he is coming")

user_input = 0
turns = 0

def command(user_input):
    global turns
    turns += 1
while turns < 10:
    user_input = input("What do you do? ")
    command(user_input)





