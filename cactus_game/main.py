import time 
import pygame
import random
import sys 
import math

import sys
import os

import asyncio


if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cactus")

#LISTS
weather = ["hot", "unbearable", "extremly hot"]
sound = ["a wolf", "the wind", "a strange noise", "a snake"]
food = ["camel meat and bread",
        "lamb and bread",
        "plain bread, you are hungry you can't complain",
        "fruit salad",
        "plate of rice",
        "salad",
        "chicken and bread",
        "a strange sandwich, it smells like goat cheese, let's hope it tastes good.",
        "goat cheese"]

drink = ["warm water",
         "water",
         "cold water",
         "a..smoothie? How did it come here?",
         "orange juice",
         "coconut water",
         "tea? that may do",
         "green juice.. you are thiristy, you can't complain"]

pet = ["a cat",
       "a rabbit",
       "a turtle",
       "a..goat?",
       "a bird",
       "a monkey",
       "a cactus, it may be your imagination or dehydration but.."]

pet_condition =["it looks hungry",
                "it looks like it has a broken bone",
                "it looks like it likes you",
                "it is trying hard to keep up with your wide footsteps",
                "It looks lonely",
                "It is still a baby",
                "it looks like it loves you now",
                "it looks hungry",
                "it is hopping behind you happily",
                "it is tired.",
                "it loves you.",
                "it is happy.",
                "It is happy to be with you.",
                "it is chewing on a random stick on the ground"
                ".. it is an ice-cream stick, yuck.",
                "it is just chilling",
                "it is eating.. your backup food"]


trivia_questions = [
    {"question":"What do you use to write on a blackboard?",
     "answer":"chalk", "wrong":["marker pen", "crayons", "pencil"]},
    {"question":"What's the name of the organ that helps you breathe?",
     "answer":"lungs", "wrong":["kidney", "langs", "toes"]},
    {"question":"What's the colored part of your eye called?",
     "answer":"iris", "wrong":["cornea", "pupil", "retina"]},
    {"question":"What do you call a house made of ice?",
     "answer":"igloo", "wrong":["ice-house", "housed-ice", "iqloo"]},
    {"question":"What is the hardest natural substance on Earth?",
     "answer":"diamond", "wrong":["iron", "copper", "uranium"]},
    {"question":"What planet is known for it's rings?",
     "answer":"saturn", "wrong":["uranus", "neptune", "pluto"]},
    {"question":"What is H2O more commonly known as?",
     "answer":"water", "wrong":["air", "oxygen", "hydrochloric acid"]},
    {"question":"What part of the body pumps blood?",
     "answer":"heart", "wrong":["liver", "spleen", "red blood cells"]},
    {"question":"What tool tells you which direction is north?",
     "answer":"compass", "wrong":["clock", "map", "tracking device"]},
    {"question":"In a website browser address bar, what does 'www' stand for?",
     "answer":"world wide web", "wrong":["we wove websites <3", "wide world web", "web world wide"]},
    {"question":"In what year was the Internet opened to the public?",
     "answer":"1993", "wrong":["1994", "1899", "1983"]},
    {"question":"What's the largest animal on Earth?",
     "answer":"blue whale", "wrong":["white whale", "dolphin", "elephant"]},
    {"question":"What is the largest desert on Earth?",
     "answer":"antarctica", "wrong":["sahara", "shara", "the arctic desert"]},
    {"question":"What color do you get if you mix red and yellow?",
     "answer":"orange", "wrong":["blue", "black", "purple"]},
    {"question":"What do cows drink?",
     "answer":"water", "wrong":["milk", "orange juice", "grass"]},
    {"question":"What season comes after winter?",
     "answer":"spring", "wrong":["summer", "winter", "autumn"]},
    {"question":"What has hands but no arms or legs?",
     "answer":"clock", "wrong":["gloves", "pans", "chairs"]},
    {"question":"What plant is famous for surviving in deserts?",
     "answer":"cactus", "wrong":["floating cactus", "grass", "roses"]},
    {"question":"What animal is known as the 'ship of the desert'?",
     "answer":"camel", "wrong":["lizard", "snake", "tiger"]},
    {"question":"What's the main gas in the air we breathe?",
     "answer":"nitrogen", "wrong":["oxygen", "carbon dioxide", "hydrogen"]},
    {"question":"What's the name of the red planet?",
     "answer":"mars", "wrong":["mercury", "venus", "earth"]},
    {"question":"What is full of holes but still holds water?",
     "answer":"sponge", "wrong":["strainer", "colander", "cup"]},
    {"question":"What's something you break before you use it?",
     "answer":"egg", "wrong":["pencil", "knife", "microwave"]},
    {"question":"What language do people speak in Brazil?",
     "answer":"portuguese", "wrong":["brazilian", "english", "spanish"]},
    {"question":"What fruit has it's seeds on the outside?",
     "answer":"strawberry", "wrong":["tomatoes", "peaches", "raspberries"]},
    {"question":"What's the term for an oasis-dwelling nomadic group?",
     "answer":"bedouins", "wrong":["arabs", "beduoins", "oasisens"]},
    {"question":"What kind of reptile often lives in deserts?",
     "answer":"lizard", "wrong":["snakes", "salamanders", "ostriches"]},
]
#VARIABLES 
endings_shown = False
cactus_intro_done = False
endings = False
points_poor_visible = False
refuse_cactus_visible = False
collapsed_sand_visible = False
collapse_exhaustion_visible = False
refuse_woman_visible = False
best_pet_visible = False
best_visible = False
mid_pet_visible = False
mid_visible = False
bad_pet_visible = False
bad_visible = False

cactus_points = False
rare_event_mirage = random.randint(1, 10)
food_added = False
drink_added = False
score_minus_twenty = False
trivia_2_started = False
trivia_3_started = False
pet_visible = False
the_pet = random.choice(pet)
the_food = random.choice(food)
the_drink = random.choice(drink)
pet_name_input = ""
pet_condition_1 = random.choice(pet_condition)
pet_condition_2 = random.choice(pet_condition)
pet_condition_3 = random.choice(pet_condition)
total_score = 0
round_score = 0
lose_count = 0 
inventory_items = []
inventory_visible = True
pet_name = ""
naming_active = False
pet_taken = False
endings = []
dialogue_box_visible = False
game_state = "dialogue"
dialogue_time = pygame.time.get_ticks()
desert_weather = random.choice(weather)
intro_started = False
right_choice = ""
left_choice = ""
right_choice_pos = (80, 600)
left_choice_pos = (780, 600)
selected_choice = ""
choice_character_visible = False
cactus_width = 10
cactus_height = 17
cactus_visible = False
cactus_1st_dialogue_started = False
intro_done = False
cactus_1st_dialogue_done = False
cactus_questions_started = False

trivia_active = False
trivia_question_num = 0
current_question = None
option_positions = {}
correct_position = ""
trivia_showing_result = False
trivia_done = False
trivia_selected = "A"

result_timer = 0
showing_trivia_result = False

cactus_bonus = False

cactus_last_line = ""
narrator_last_line =""
lines = ["That was soooo much fun!", "Till next time!", "Fun, right?", "Bye!"]
narrator_lines = ["That was weird.", "You are planning to play again next time, aren't you?", "Well, that is your life now."]

cactus_line_done = False
narrator_line_done = False
score_line_done = False

bucket_taken = False 
bucket_scene_started = False
bucket_choice_started = False

trivia_dialogue = []

bucket_timer = 0 
bucket_scene_started = False

trivia_3_timer = 0
trivia_3_done = False
trivia_3_started = False

jeep_man_visible = False
bro_visible = False
trivia_round = 1

man_back_timer = 0
man_back = False
man_back_bonus = False

post_trivia_1_done = False 

strange_sound = random.choice(sound)
player_pet_status = random.choice(pet_condition)

coin_added = False

#DIALOGUE
intro = ["You find yourself in the middle of the desert. (press Z)",
        "You don’t remember how you got here. Your head is foggy, "
        f"and the weather is {random.choice(weather)}.",
        "You’re thirsty.",
        "Hungry.",
        "Dizzy.",
        "The sand stretches endlessly in every direction.",
        "You hear a strange sound, you look and"
        " " "spot a grinning floating cactus.",
        "Yes, it has a face.",
        "You don't know whether it is just dehydration"
        " " "or if you have lost your mind"]

cactus_intro = ["Hi there! You are new here, aren't you?",
                "I'm The Floating Cactus! Your new best friend here!",
                "You look confused..",
                "Well, I will help you settle in!",
                "First, the game is simple, just choose whatever you feel is right. but remember, your choices matter!",
                "For the controls, just press Z to progress through the game like you have been doing,",
                "The arrows to move around when possible,",
                "And E to see your unlocked endings!",
                "You will rarely need to use the ENTER button, other than that it is pretty simple.",
                "If you want a bigger screen, press F11!",
                "Also, a tip: never ignore me. We are friends and I really hate being ignored.",
                "Now for the fun part!",
                "nothing"]

cactus_1st_dialogue = ["Do you want to play"
                      " " "a little trivia game? :D",
                      "3 trivia questions,"
                      " " "if you get 1 right you will earn 5 points!"
                      " " "That is a great way to increase your total score!",
                      "fun right? :D"]

cactus_happy = ["You agree to the floating cactus offer" 
                " " ", it grins widely and askes:"]

cactus_sad = ["You refuse as a normal sane human being.",
              "Fine! I will"
              " " "be back!",
              "That was weird."]
bucket_dialogue = ["You looked around and there was an empty bucket.",
                 "You remembered something about having to fill it.", 
                 "nothing"]
jeep_vs_pond = ["In the distance, you spot two things:",
               "-A shimmering water pond far to your left.",
               "-A black jeep, strange and unmoving, off to the right.",
               "You have to choose. You can’t just sit here"
                " " "and wait for the sun to finish you off.",
                "nothing"]
jeep_vs_pond_main = [] 
jeep_dialogue = ["You walk towards the jeep.",
               "After reaching it, you see a man inspecting the engine.",
               "It looks like the jeep is broken.",
               "nothing"]
pond_dialogue = ["You start walking towards the water pond.",
               "But with every step, the distance"
                " " "seems to stretch further away.",
                "You keep walking... and walking...",
                "nothing"]
pond_back_dialogue = ["You lost 5 points for coming here from the beginning!",
                    "You went back to where you were."] + jeep_vs_pond
cactus_rare_dialogue = ["You heard a strange sound", 
                      "as you looked, it turned out to be the"
                       " " "floating cactus again..",
                       "Hi there!",
                       "What are you doing here? As far"
                        " " "as I know, this place is empty.",
                        "Need a lift to the jeep?"
                        " " "there is a guy there who might help you!",
                        "nothing"]
#EDITING
cactus_rare_happy = ["It holds you happily, and flies away with you humming.",
                     "you arrive in a couple of minutes.",
                     "Here you go!",
                     "Also, here is 20 points! They might help"
                     " " "you :D",
                     f"Your total score now is {total_score}.",
                     "Well, it turned out to be helpful.",
                     "nothing"]
cactus_rare_sad = ["fine! I shouldn't have offered you help from the start",
                   "It vanishes looking upset.",
                   "It is your fault.",
                   "You continue walking."
                   "And walking",
                   "The pond never gets any closer.",
                   "It was a mirage.",
                   "You're more lost than before,"
                    " " "the heat pressing down"
                    " " "on you like a weight.",
                    "Exhausted, dizzy, and drained"
                    " " "from the endless walk",
                    "You collapse in the sand."]
mirage_dialogue = ["The pond never gets any closer.",
                 "It was a mirage.",
                 "You're more lost than before,"
                 " " "the heat pressing down on you like a weight.",
                 "Exhausted, dizzy, and"
                 " " "drained from the endless walk",
                 "You collapse in the sand."]

jeep_back_dialogue = []

jeep_man_talk = ["You call for him and he walks towards you with a questioning look",
                 "You explain that you're lost and don’t remember how you got here.",
                "I was headed to a nearby village, but the jeep broke down.",
                 "The jeep needs water to start again",
                 "There is a well nearby, but I have nothing to fetch water with.",
                 "If you help him, he might help you in return.",
                 "nothing"]

bucket_given_dialogue = ["You hand him the bucket",
                       "He takes it, walks off towards the well.",
                       "As you wait you hear a strange sound. Looking up, you spot it again.",
                       "The Floating Cactus.",
                       "Hey there again!",
                       "Do you want to play another trivia game?",
                       "Just like the last time, you earn 5 points for each correct question and lose 5 for each wrong one!",
                       "Remember that can easily increase your score if you are smart enough!",
                       "nothing"]

bucket_thrown_dialogue= ["You threw the bucket directly at his head.",
                        "OW! What is wrong with you!?",
                        "You lost the bucket.",
                        "You know what? I am taking this and leaving you.",
                        "You called after him.",
                        "What?",
                        "You offered to help him. He sighed deeply.",
                        "Fine. Come make yourself useful",
                        "You were just going after him but a strange sound stopped you.",
                        "You look up.",
                        "It is The Floating Cactus.",
                        "Hey there again!",
                        "Do you want to play another trivia game?",
                        "Just like the last time you earn 5 points for each correct question and lose 5 for each wrong one!",
                        "Remember that can easily increase your score if you are smart enough!",
                        "nothing"]

man_back_dialogue = ["The man comes back with the bucket full of water",
                  "He walks to the jeep.",
                  "After pouring the water into the engine, he fiddles with it for a while"
                   " " "and the jeep starts.",
                   "You have earned 10 points for choosing right!",
                   f"Your total score now is {total_score} points!",
                   "Get in",
                   "You hop into the jeep",
                   "As soon as he began driving, you started feeling sleepy.",
                   "...",
                   "...",
                   "...",
                   "You opened your eyes and you were at the entrance of a village.",
                   "Here we are",
                   "I've got some business to take care of. I have to go. See you around.",
                   "nothing"]
stare_man_dialogue = ["You stared at him.",
                    "...",
                    "...",
                    "Stop looking at me like that",
                    "...",
                    "Stop.",
                    "Ok. Ok. Just.. come help me, let's find a way to make it work.",
                    "nothing"]
                    
help_dialogue = ["You offered to help",
               "I told you. I need something to fetch the water with.",
               "You offered your shoe.",
               "Are you serious?",
               "You nodded. He sighed",
               "That will take forever. Just come help me, let's find a way to make it work.",
               "nothing"]

man_die = ["You both try everything to fix" #BACK
            " " "the jeep, but nothing works.",
            "You're too hungry to think straight.",
            "The man crawls into the jeep.",
            "He looks exhausted—maybe he"
            " " "passed out, maybe worse.",
            "You hear a strange sound in the distance -SOUND, you think.",
            "It doesn't look safe to stay here.",
            "Night falls.",
            "You lie on the sand, eyes"
            " " "heavy, body aching.",
            "The stars blur.",
            "Everything fades.",
            "You don’t hear anything anymore.",
            "You really should've gotten that bucket."]

pet_dialogue = ["You get off the jeep.",
              "You have no idea what to do.",
              "You walk aimlessly.",
              "You don't see anyone but you can spot some houses in a distance.",
              "you walk",
              "...",
              "...",
              "As you walk through the dusty streets, you hear footsteps behind you",
              "You stop.",
              "You turn around—it’s PET",
              "pet_condition_1.",
              "nothing"]
pet_accepted_dialogue = ["You decided to adopt it!",
                       "What are you going to name it?",
                       "nothing"]

pet_rejected_dialogue = ["You leave it behind.",
                        "It looks… kind of sad.",
                        "You turn around",
                        "You can feel it watching you walk away.",
                        "nothing"]

pet_name_done = [f"Your pet name is {pet_name}",
                 "PET STATUS",
                 "nothing"]

village_walking = ["You walk through the village streets, stomach growling, throat dry.",
                   "You are desperate for anything to eat or drink",
                   "nothing"]


shop_dialogue = ["Just when you are about to drop..",
                     "You spot a small shop.",
                     "You rush towards it.",
                     "...",
                     "...",
                     "An old woman sits behind the counter.",
                     "How can I help you?",
                     "nothing"]

coin_given_dialogue = ["Sorry..",
                     "It is a part of my job, I can't take you with me but..",
                     "Here take that",
                     "He hands you a strange looking coin.",
                     "That is the currency here. You look hungry, buy yourself something to eat.",
                     "You pocket the coin and thank him, he nods at you.",
                     "You start exploring the village.",
                     "nothing"]

thanked_dialogue = ["You thank him.",
                  "He nods at you.",
                  "You decide to explore the village on your own",
                  "nothing"]

no_coin_dialogue = ["You remember that you don't have any money.",
                  "Too weak to care anymore, you ask the woman for help anyway.",
                  "I think I can help you",
                  "But..",
                  "I will have to take 20 points from your score instead of money.",
                  "In exchange, I will give you some food and something to drink",
                  "nothing"]

no_money_shop = ["...",
                 "It seems like you don’t have enough points.",
                 "You look at her hoping that she helps you anyway.",
                 "Fine, I will help you. Just because you look like you really need it",
                 "She hands you FOOD and DRINK",
                 "Here you go.",
                 "You thank her and say that you will pay her later when you can.",
                 "Don't worry about it, son. It is on the house.",
                 "You thank her again and walk away, searching for a shadowed place to rest.",
                 "nothing"]

score_food = ["You agreed.",
              "Here you go..",
              "she hands you smth",
              "That was a good deal.",
              "You thank her and walk away, searching for a shadowed place to rest.",
              "nothing"]

refuse_food = ["As you like, then. Take care.",
               "You leave the shop empty-handed..",
               "You’re too weak to go on.",
               "The village blurs around you.",
               "You can’t hear, can’t think.",
               "Everything fades..",
               "You collapse."]

eating_dialogue = ["The sun begins to sit..",
                 "You set down under a palm tree to eat and drink in peace.",
                 "You eat and drink.",
                 "nothing"]
eating_pet_dialogue = ["Your pet sneaks a few crumbs too, of course.",
                     "You look at it, PET_CONDITION",
                     "You pat it's head and look back at the sunset",
                     "The sky looks beautiful..",
                     "The weather is cooler..",
                     f"{pet_name} is sleeping on your lap..",
                     "It is almost.. peaceful.",
                     "nothing"]
cactus_eating_dialogue = ["Hiiii again~~!",
                        "You look around searching for something to throw at it, it only grins wider",
                        "Wanna play a trivia game?",
                        "nothing"]



only_one = ["You asked for a drink only because you were too thiristy",
            "Here you go, son",
            "She hands you DRINK and gives you some change.",
            "You use the change to buy yourself something to eat, she hands you FOOD",
            "You thank her and walk away, searching for a shadowed place to rest.",
            "nothing"]

both_dialogue = ["You ask for both food and a drink, not knowing whether the coin can cover both.",
               "The woman surprisingly hands you STUFF",
               "Here you go, son. Take care.",
               "You thank her and walk away, searching for a shadowed place to rest.",
               "nothing"]

best_ending = ["After finishing your meal, you thank God for surviving this and stand up, heading for whatever comes next",
                "You walk back through the village streets.",
                "You are still exhausted, your steps feel heavy.",
                "You stop as you hear someone calling your name..",
                "You turned around reaching for a rock half-expecting that weird floating cactus again",
                "..who is that?",
                "Thank God! Finally, you are alive!",
                "You took a step back. He doesn't seem to notice",
                "We were all so worried. We have been for hours.",
                "He was breathless but looked genuinely relieved to see you",
                "He takes a deep breath..",
                "Are you hurt? We should go, I have the car with me. We should-",
                "You flinch away when he reachs for your shoulder, he pulls away.",
                "What is wrong? Why are you acting weird?",
                "You ask him who he is and how he knows you.",#14
                "I am Adam, your brother. Don't you remember me?",
                "I was searching for you with Dad and saw a guy in a Jeep. I asked if he had seen someone lost. He said he had met a lost traveller, and I knew it had to be you.",
                "I asked him and got directions to this village.",
                "You stare at him.",
                "You're not sure if you should trust him, but.. there is something familiar about his face.",
                "He looks concerned..",
                "You look exhausted.. Mom and Dad are worried sick. Let's just get you home.", #20
                "He holds out his hand, you hesitate. He notices. He sighs and tries again, his tone becomes gentle:",
                "Do you remember the bucket?",
                "Dad told you to fill it and you never came back. We were camping in the desert-me, you, Mom, Dad, and Lily, our little sister?",
                "That rings a bell", #24
                "Memories flood back, hazy at first… then clearer.",
                "You remember.",
                "You remember everything.",
                "nothing"]

best_ending_pet = [f"You glance down at your side, you see {pet_name}.", 
                    "pet_condition_3.",
                    "There's no way you are leaving without it, so you take it with you",
                    "You hop into your brother’s car, then your pet hops into your lap.",
                    "He doesn't seem to be complaining, he gets in the driver seat and asks you to rest till you reach home",
                    "You close your eyes..",
                    "You feel safe..",
                    "You feel at home."]

best_ending_no_pet = ["You hop into your brother’s car",
                      "He gets in the driver seat and tells you to rest till you reach home",
                      "You close your eyes..",
                      "You feel safe..",
                      "You feel at home."]

mid_ending = ["After finishing, you stand up.",
              "Just as you are ready to start wandering again, a familiar voice calls you.",
              "Hey! Still wandering, huh? I’ve been looking for you.",
              "There’s a small shop nearby looking for help",
              "Room and food are included.",
              "First person I thought of was you. You in?",
              "...",
              "You think about it.",
              "You still don't know you why were in the desert.",
              "Also.."
              "You don't have anything better to do, do you?",
              "You accept the offer",
              "nothing"]

transition = ["A week passes..",
              "still nothing"]

mid_ending_pet = [f"You and {pet_name} now work in the cozy little shop.",
                  "pet_condition_3.",
                  "You’ve built a new rhythm, a quiet joy.",
                  "The past is still foggy, but at least you've finally gotten some peace",
                  "You are happy."]

mid_ending_no_pet = ["You spend your day working in the shop.",
                     "You have a place to go to at night.",
                     "You are alone but.. you’ve built a new rhythm, a quiet joy.",
                     "The past is still foggy, but at least you've finally gotten some peace",
                     "You are happy."]

bad_ending = ["A little more energy returns to you after eating.",
              "You stand up.",
              "Just as you're about to decide where to go next…",
              "Hey there~! Still lost? :D",
              "You look up.",
              "It is there again.",
              "You walk away..",
              "You walk away.",
              "You-",
              "I am not done talking yet, idiot. That is very rude.",
              "You listen to the floating cactus.",
              "nothing"]

bad_ending_pet = ["Soooo here’s the thing—you’ve got, like, no money, no family around, no idea where you are…",
                  "OH!",
                  f"But you at least do have {pet_name}! Cute little thing!",
                  "You tense up.",
                  "You try to walk away but your feet are rooted to the ground.",
                  "You listen to the cactus.",
                  "Here’s the deal, I know a nearby shop that needs a worker.",
                  "You get a room and one meal a day!",
                  "Pretty sweet, huh?",
                  "Buuuuuut—",
                  "(Dramatic pause)",
                  f"—I get to keep {pet_name}.",
                  "I’m already attached. Cactus stuff. You understand.",
                  "nothing"]

bad_ending_pet_no = ["Oh, never mind! You don’t get to choose this time. It is my turn now!",
                     "...",
                     "...",
                     "You are inside a small shop.",
                     f"Alone. No {pet_name} in sight.",
                     "A week passes..",
                     "You work every day.",
                     "You eat.",
                     "You are alive."]

bad_ending_pet_yes = ["I was going to take it either way, but thanks for the effort!",
                     "...",
                     "...",
                     "You are inside a small shop.",
                     f"Alone. No {pet_name} in sight.",
                     "A week passes..",
                     "You work every day.",
                     "You eat.",
                     "You are alive."]

bad_ending_no_pet = ["Soooo here’s the thing—you’ve got, like, no money, no family around, no idea where you are… OH!",
                     "It sighs dramatically",
                     "You really don't have anything worth taking, but I can still think of a deal...",
                     "You tense up",
                     "You try to walk away but your feet are rooted to the ground.",
                     "You listen to the catus.",
                     "Here’s the deal, I know a nearby shop that needs a worker.",
                     "You get a room and one meal a day!",
                     "Pretty sweet, huh?",
                     "Buuuuuut—",
                     "(Dramatic pause)",
                     "—I get to keep all your points! I can buy that cool cap I've always wanted now!",
                     f"{total_score} points, right?",
                     "That is a decent amount. Not bad. Not good either but I think this will buy me the cap",
                     "nothing"]

bad_ending_no_pet_no = ["Oh, never mind! You don’t get to choose this time. It is my turn now!",
                        "...",
                        "...",
                        "You are inside a small shop.",
                        "Alone.",
                        "You have no points.",
                        "A week passes..",
                        "You work every day.",
                        "You eat.",
                        "You are alive."]

bad_ending_no_pet_yes = ["I was going to take them either way, but thanks for the effort!",
                         "...",
                         "...",
                         "You are inside a small shop.",
                         "Alone.",
                         "You have no points.",
                         "A week passes..",
                         "You work every day.",
                         "You eat.",
                         "You are alive."]




current_dialogue = intro
current_index = 0

#IMAGES
endings_screen = pygame.image.load("Images/endings_bg.jpg").convert_alpha()

inventory_bg = pygame.image.load("Images/inventory.png").convert_alpha()

bg1 = pygame.image.load("Images/bg1.jpg").convert_alpha()
dialogue_box_visible = pygame.image.load("Images/dialogue_box.png").convert_alpha()
dialogue_box_invisible = pygame.image.load("Images/dialogue_box_invisible.png").convert_alpha()
dialogue_box = dialogue_box_visible
dialogue_ch = pygame.image.load("Images/dialogue_ch_symbol.png").convert_alpha()
choice_character = pygame.image.load("Images/choice_character.png").convert_alpha()
dialogue_cactus = pygame.image.load("Images/dialogue_cactus_symbol.png").convert_alpha()
dialogue_man = pygame.image.load("Images/dialogue_man_symbol.png").convert_alpha()
dialogue_bro = pygame.image.load("Images/dialogue_bro.png").convert_alpha()
dialogue_woman = pygame.image.load("Images/dialogue_woman_symbol.png").convert_alpha()
cactus_normal = pygame.image.load("Images/cactus_character.png").convert_alpha()
cactus_shocked = pygame.image.load("Images/cactus_shocked.png").convert_alpha()
cactus_evil = pygame.image.load("Images/cactus_evil.png").convert_alpha()
cactus_dissappointed = pygame.image.load("Images/cactus_dissappointed.png").convert_alpha()
cactus_points_won = pygame.image.load("Images/cactus_points_won.png").convert_alpha()
cactus_points_loss = pygame.image.load("Images/cactus_points_loss.png").convert_alpha()
cactus_happy = pygame.image.load("Images/cactus_happy.png").convert_alpha()
cactus_angry = pygame.image.load("Images/cactus_angry.png").convert_alpha()
cactus = cactus_normal
dialogue_character = dialogue_ch
bg2 = pygame.image.load("Images/bg2.jpg").convert_alpha()
bg_pond = pygame.image.load("Images/bg_pond.jpg").convert_alpha()
bg_jeep = pygame.image.load("Images/bg_jeep.jpg").convert_alpha()
bucket_img = pygame.image.load("Images/bucket_empty.png").convert_alpha()
bucket_icon = pygame.transform.scale(bucket_img, (60, 60))
bg_flying = pygame.image.load("Images/bg_flying.jpg").convert_alpha()
bg_walking_1 = pygame.image.load("Images/bg_walking_1.jpg").convert_alpha()
bg_walking_2 = pygame.image.load("Images/bg_walking_2.jpg").convert_alpha()
bg_walking_3 = pygame.image.load("Images/bg_walking_3.jpg").convert_alpha()
bg_shop_far1 = pygame.image.load("Images/bg_shop_far1.jpg").convert_alpha()
bg_shop_far2 = pygame.image.load("Images/bg_shop_far2.jpg").convert_alpha()
bg_shop_far3 = pygame.image.load("Images/bg_shop_far3.jpg").convert_alpha()
bg_shop_far4 = pygame.image.load("Images/bg_shop_far4.jpg").convert_alpha()
bg_shop = pygame.image.load("Images/bg_shop.jpg").convert_alpha()
bg_collapse = pygame.image.load("Images/bg_collapse.jpg").convert_alpha()
bg_sunset = pygame.image.load("Images/bg_sunset.jpg").convert_alpha()
bg_sunset_walk_1 = pygame.image.load("Images/bg_sunset_walk_1.jpg").convert_alpha()
bg_sunset_walk_2 = pygame.image.load("Images/bg_sunset_walk_2.jpg").convert_alpha()
bg_sunset_sitting = pygame.image.load("Images/bg_sunset_sitting.jpg").convert_alpha()
bg_week = pygame.image.load("Images/bg_week.jpg").convert_alpha()
bg_mid_pet = pygame.image.load("Images/bg_mid_pet.jpg").convert_alpha()
bg_mid_no_pet = pygame.image.load("Images/bg_mid_no_pet.jpg").convert_alpha()
bg_white = pygame.image.load("Images/bg_white.jpg").convert_alpha()
bg_bad_ending = pygame.image.load("Images/bg_bad_ending.jpg").convert_alpha()
jeep_man_normal = pygame.image.load("Images/jeep_man_normal.png").convert_alpha()
bro_normal = pygame.image.load("Images/bro_normal.png").convert_alpha()
bro_sad = pygame.image.load("Images/bro_sad.png").convert_alpha()
bro_concerned = pygame.image.load("Images/bro_concerned.png").convert_alpha()
bg_jeep_man_inspecting = pygame.image.load("Images/bg_jeep_man_inspecting.jpg").convert_alpha()
jeep_man_angry = pygame.image.load("Images/jeep_man_angry.png").convert_alpha()
jeep_man_bucket = pygame.image.load("Images/jeep_man_bucket.png").convert_alpha()
bg_in_jeep = pygame.image.load("Images/bg_in_jeep.jpg").convert_alpha()
bg_jeep_night_1 = pygame.image.load("Images/bg_jeep_night_half.jpg").convert_alpha()
bg_jeep_night_2 = pygame.image.load("Images/bg_jeep_night_half2.jpg").convert_alpha()
bg_jeep_night_3 = pygame.image.load("Images/bg_jeep_night_full.jpg").convert_alpha()
bg_stars = pygame.image.load("Images/bg_stars.jpg").convert_alpha()
bg_stars_blur = pygame.image.load("Images/bg_stars_blur.jpg").convert_alpha()
bg_village_entrance = pygame.image.load("Images/bg_village_entrance.jpg").convert_alpha()
pet_cat = pygame.image.load("Images/pet_cat.png").convert_alpha()
pet_rabbit = pygame.image.load("Images/pet_rabbit.png").convert_alpha()
pet_turtle = pygame.image.load("Images/pet_turtle.png").convert_alpha()
pet_goat = pygame.image.load("Images/pet_goat.png").convert_alpha()
pet_bird = pygame.image.load("Images/pet_bird.png").convert_alpha()
pet_monkey = pygame.image.load("Images/pet_monkey.png").convert_alpha()
pet_cactus = pygame.image.load("Images/pet_cactus.png").convert_alpha()
coin_img = pygame.image.load("Images/coin.png").convert_alpha()
coin_icon = pygame.transform.scale(coin_img, (60, 60))

#FOOD
c_m_b = pygame.image.load("Images/camel_meat_and_bread.png").convert_alpha()
s_m_b = pygame.image.load("Images/sheep_meat_and_bread.png").convert_alpha()
bread = pygame.image.load("Images/bread.png").convert_alpha()
fruit_salad = pygame.image.load("Images/fruit_salad.png").convert_alpha()
salad = pygame.image.load("Images/salad.png").convert_alpha()
rice = pygame.image.load("Images/rice.png").convert_alpha()
chicken_and_bread = pygame.image.load("Images/chicken_and_bread.png").convert_alpha()
sandwich = pygame.image.load("Images/sandwich.png").convert_alpha()
goat_cheese = pygame.image.load("Images/goat_cheese.png").convert_alpha()

c_m_b_icon = pygame.transform.scale(c_m_b, (60, 60))
s_m_b_icon = pygame.transform.scale(s_m_b, (60, 60))
bread_icon = pygame.transform.scale(bread, (60, 60))
fruit_salad_icon = pygame.transform.scale(fruit_salad, (60, 60))
salad_icon = pygame.transform.scale(salad, (60, 60))
rice_icon = pygame.transform.scale(rice, (60, 60))
chicken_and_bread_icon = pygame.transform.scale(chicken_and_bread, (60, 60))
sandwich_icon = pygame.transform.scale(sandwich, (60, 60))
goat_cheese_icon = pygame.transform.scale(goat_cheese, (60, 60))

#DRINK
warm_water = pygame.image.load("Images/warm_water.png").convert_alpha()
cold_water = pygame.image.load("Images/cold_water.png").convert_alpha()
water = pygame.image.load("Images/water.png").convert_alpha()
smoothie = pygame.image.load("Images/smoothie.png").convert_alpha()
orange_juice = pygame.image.load("Images/orange_juice.png").convert_alpha()
coconut_water = pygame.image.load("Images/coconut_water.png").convert_alpha()
tea = pygame.image.load("Images/tea.png").convert_alpha()
green_juice = pygame.image.load("Images/green_juice.png").convert_alpha()

warm_water_icon = pygame.transform.scale(warm_water, (60, 60))
cold_water_icon = pygame.transform.scale(cold_water, (60, 60))
water_icon = pygame.transform.scale(water, (60, 60))
smoothie_icon = pygame.transform.scale(smoothie, (60, 60))
orange_juice_icon = pygame.transform.scale(orange_juice, (60, 60))
coconut_water_icon = pygame.transform.scale(coconut_water, (60, 60))
tea_icon = pygame.transform.scale(tea, (60, 60))
green_juice_icon = pygame.transform.scale(green_juice, (60, 60))

#SLOTS
slot1 = pygame.image.load("Images/slot1.png").convert_alpha()
slot2 = pygame.image.load("Images/slot2.png").convert_alpha()
slot3 = pygame.image.load("Images/slot3.png").convert_alpha()
slot4 = pygame.image.load("Images/slot4.png").convert_alpha()
slot5 = pygame.image.load("Images/slot5.png").convert_alpha()
#RECTS
slot1_rect = slot1.get_rect(topleft=(420, 610))
slot2_rect = slot2.get_rect(topleft=(510, 610))
slot3_rect = slot3.get_rect(topleft=(600, 610))
slot4_rect = slot4.get_rect(topleft=(690, 610))
slot5_rect = slot5.get_rect(topleft=(780, 610))

#ENDINGS IMAGES
points_poor_text =  pygame.image.load("Images/points_poor.png").convert_alpha()
refuse_cactus =  pygame.image.load("Images/refuse_cactus.png").convert_alpha()
collapsed_sand =  pygame.image.load("Images/collapse_on_sand.png").convert_alpha()
collapse_exhaustion =  pygame.image.load("Images/collapse_exhaustion.png").convert_alpha()
refuse_woman =  pygame.image.load("Images/refuse_woman.png").convert_alpha()
best_pet =  pygame.image.load("Images/best_ending_pet.png").convert_alpha()
best =  pygame.image.load("Images/best_ending.png").convert_alpha()
mid_pet =  pygame.image.load("Images/mid_ending_pet.png").convert_alpha()
mid =  pygame.image.load("Images/mid_ending.png").convert_alpha()
bad_pet =  pygame.image.load("Images/bad_ending_pet.png").convert_alpha()
bad =  pygame.image.load("Images/bad_ending.png").convert_alpha()


current_bg = bg1
jeep_man = jeep_man_normal
bro = bro_normal


the_pet_img = pet_cat
the_food_img = c_m_b_icon
the_drink_img = water_icon

#FONT
font = pygame.font.Font("fonts/messages.ttf", 30)

#FUNCTIONS
def check_score():
    global game_state, dialogue_box_visible, current_dialogue, current_index, trivia_active, points_poor_visible
    if total_score < 0:
        current_dialogue = ["You have less than 0 points! Sorry, that means game over for you!"]
        dialogue_box_visible = True
        current_index = 0
        trivia_active = False
        game_state = "game_over"
        points_poor_visible = True

def draw_inventory():
    screen.blit(inventory_bg, (0, 600))
    
    screen.blit(slot1, slot1_rect.topleft)
    screen.blit(slot2, slot2_rect.topleft)
    screen.blit(slot3, slot3_rect.topleft)
    screen.blit(slot4, slot4_rect.topleft)
    screen.blit(slot5, slot5_rect.topleft)

    draw_inventory_items()

def inventory_add(found_thing):
    inventory_items.append(found_thing)

def draw_inventory_items():

    if len(inventory_items) > 0:
        item_rect = inventory_items[0].get_rect(center=slot1_rect.center)
        screen.blit(inventory_items[0], item_rect)

    if len(inventory_items) > 1:
        item_rect = inventory_items[1].get_rect(center=slot2_rect.center)
        screen.blit(inventory_items[1], item_rect)
    
    if len(inventory_items) > 2:
        item_rect = inventory_items[2].get_rect(center=slot3_rect.center)
        screen.blit(inventory_items[2], item_rect)

    if len(inventory_items) > 3:
        item_rect = inventory_items[3].get_rect(center=slot4_rect.center)
        screen.blit(inventory_items[3], item_rect)

    if len(inventory_items) > 4:
        item_rect = inventory_items[4].get_rect(center=slot5_rect.center)
        screen.blit(inventory_items[4], item_rect)

def restart():
    global total_score, round_score, lose_count, inventory_items, pet_name
    global dialogue_box_visible, game_state, dialogue_time, intro_started
    global selected_choice, choice_character_visible
    global cactus_width, cactus_height, cactus_visible
    global cactus_1st_dialogue_started, intro_done, cactus_1st_dialogue_done, cactus_questions_started
    global trivia_active, trivia_question_num, current_question, option_positions
    global correct_position, trivia_done, trivia_selected, result_timer, showing_trivia_result
    global cactus_last_line, narrator_last_line, cactus_line_done, narrator_line_done, score_line_done
    global current_dialogue, current_index, cactus, dialogue_character
    global bucket_taken, bucket_scene_started, bucket_choice_started, bucket_timer
    global current_bg, collapse, points_poor, cactus_points, jeep_man_visible
    global jeep_vs_pond_main, jeep_man, jeep_back_dialogue
    global trivia_round, man_back, man_back_timer, man_back_bonus
    global cactus_bonus, trivia_showing_result, post_trivia_1_done
    global trivia_2_started, trivia_3_started, trivia_3_done, trivia_3_timer
    global food_added, drink_added, score_minus_twenty, pet_taken, naming_active
    global pet_name_input, pet_visible, coin_added
    global bro_visible, bro, inventory_visible
    global desert_weather, strange_sound, the_food, the_drink, the_pet
    global pet_condition_1, pet_condition_2, pet_condition_3, the_food_img, the_drink_img, the_pet_img
    global player_pet_status, endings, left_choice, right_choice
    global lines, narrator_lines, score_line, trivia_dialogue, rare_event_mirage

    pet_condition_1 = random.choice(pet_condition)
    pet_condition_2 = random.choice(pet_condition)
    pet_condition_3 = random.choice(pet_condition)

    # scores and counts
    total_score = 0
    round_score = 0
    lose_count = 0
    score_line = ""
    endings = []
    rare_event_mirage = random.randint(1, 10)

    # inventory
    inventory_items = []
    inventory_visible = True

    # pet
    pet_name = ""
    pet_name_input = ""
    pet_taken = False
    pet_visible = False
    naming_active = False
    the_pet = random.choice(pet)
    the_pet_img = pet_cat
    player_pet_status = random.choice(pet_condition)

    # food and drink
    food_added = False
    drink_added = False
    score_minus_twenty = False
    the_food = random.choice(food)
    the_drink = random.choice(drink)
    the_food_img = c_m_b_icon
    the_drink_img = water_icon
    coin_added = False

    # random world elements
    desert_weather = random.choice(weather)
    strange_sound = random.choice(sound)

    # dialogue state
    dialogue_box_visible = False
    game_state = "dialogue"
    dialogue_time = pygame.time.get_ticks()
    current_dialogue = intro
    current_index = 0
    dialogue_character = dialogue_ch
    left_choice = ""
    right_choice = ""
    selected_choice = ""
    choice_character_visible = False

    # intro flags
    intro_started = False
    intro_done = False
    cactus_1st_dialogue_started = False
    cactus_1st_dialogue_done = False
    cactus_questions_started = False

    # cactus
    cactus = cactus_normal
    cactus_width = 10
    cactus_height = 17
    cactus_visible = False
    cactus_points = False
    cactus_bonus = False
    cactus_last_line = ""
    narrator_last_line = ""
    cactus_line_done = False
    narrator_line_done = False
    score_line_done = False
    lines = ["That was soooo much fun!", "Till next time!", "Fun, right?", "Bye!"]
    narrator_lines = ["That was weird.", "You are planning to play again next time, aren't you?", "Well, that is your life now."]

    # trivia
    trivia_active = False
    trivia_question_num = 0
    trivia_round = 1
    current_question = None
    option_positions = {}
    correct_position = ""
    trivia_done = False
    trivia_selected = "A"
    result_timer = 0
    showing_trivia_result = False
    trivia_showing_result = False
    trivia_dialogue = []
    post_trivia_1_done = False
    trivia_2_started = False
    trivia_3_started = False
    trivia_3_done = False
    trivia_3_timer = 0

    # bucket
    bucket_taken = False
    bucket_scene_started = False
    bucket_choice_started = False
    bucket_timer = 0
    jeep_vs_pond_main = []
    jeep_back_dialogue = []

    # jeep man
    jeep_man = jeep_man_normal
    jeep_man_visible = False
    man_back = False
    man_back_timer = 0
    man_back_bonus = False


    # brother
    bro = bro_normal
    bro_visible = False

    # background
    current_bg = bg1
    

def draw_message(message, x, y):
    text_surface = font.render(message, True, (0, 0, 0))
    screen.blit(text_surface, (x, y))

def timer_reset():
    global dialogue_time
    dialogue_time = pygame.time.get_ticks()

def text(message, width, x, y):
    current_line = ""
    lines = []
    test_line = ""
    words = message.split()
    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] < width: 
            current_line = test_line
        else:
            lines.append(current_line )
            current_line = word + " "
    lines.append(current_line)
    for line in lines:
        draw_message(line, x, y)
        y = y + 5 + font.size("a")[1]

def dialogue_check():
    if dialogue_box_visible:
        if jeep_man_visible: #EDIT
            screen.blit(jeep_man, (480, 280))
            screen.blit(dialogue_box, (50, 20))
            screen.blit(dialogue_character,(103, 47))
            text(current_dialogue[current_index], 1000, 185, 47)

        elif bro_visible: 
            screen.blit(bro, (480, 280))
            screen.blit(dialogue_box, (50, 20))
            screen.blit(dialogue_character,(103, 47))
            text(current_dialogue[current_index], 1000, 185, 47)
        else:
            screen.blit(dialogue_box, (50, 20))
            screen.blit(dialogue_character,(103, 47))
            text(current_dialogue[current_index], 1000, 185, 47)

def choices(left_choice, right_choice):
    global choice_character_visible
    if dialogue_box_visible:
        screen.blit(dialogue_box, (50, 20))
        if selected_choice == "left_choice":
            screen.blit(choice_character, (200, 95))
        elif selected_choice == "right_choice":
            screen.blit(choice_character, (970, 95))
        else:
            screen.blit(choice_character, (590, 95))
        choice_character_visible = True
        text(left_choice, 550, 100, 95)
        text(right_choice, 480, 750, 95)
        


def start():
    screen.blit(current_bg, (0, 0))

def cactus_questions(comment, cactus_last_line):
    choices("Agree to play", "Cancel the offer")

def trivia_question_setup():
    global option_positions
    global correct_position
    global current_question
    the_trivia_q = random.choice(trivia_questions)
    current_question = the_trivia_q
    wrong_answers = the_trivia_q["wrong"]
    right_answer = the_trivia_q["answer"]
    answers = []
    answers.append(right_answer)
    answers = answers + wrong_answers
    random.shuffle(answers)
    option_positions = {"A":answers[0], "B":answers[1], "C":answers[2], "D":answers[3]}
    
    for position, answer in option_positions.items():
        if answer == right_answer:
            correct_position = position


def draw_trivia():
    if trivia_active:
        screen.blit(dialogue_box, (50, 20))
        text(current_question["question"], 1050, 80, 45)
        text(option_positions["A"], 500, 70, 100)
        text(option_positions["B"], 500, 935, 100)
        text(option_positions["C"], 500, 70, 155)
        text(option_positions["D"], 500, 935, 155)

        if trivia_selected == "B":
            screen.blit(choice_character, (880, 100))
        elif trivia_selected == "C":
            screen.blit(choice_character, (60, 155))
        elif trivia_selected == "D":
            screen.blit(choice_character, (880, 155))
        else:
            screen.blit(choice_character, (60, 100))

def draw_naming():
    global pet_name_input
    pygame.draw.rect(screen, (255, 255, 255), (340, 560, 600, 50))
    draw_message(pet_name_input, 340, 568)

async def main():
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11: 
                    pygame.display.toggle_fullscreen()

            
                if event.key == pygame.K_e:
                    if not endings and not naming_active:
                        endings = True
                    else:
                        endings = False

                if event.key == pygame.K_z and not endings_shown: 
                    if dialogue_box_visible and game_state == "dialogue":
                        if current_index < len(current_dialogue) - 1:
                            current_index += 1
                        else:
                            dialogue_box_visible = False

                    if game_state == "game_over":
                        if current_index < len(current_dialogue) - 1:
                            current_index += 1
                        else:
                            restart()        

                    elif dialogue_box_visible and game_state == "choice_cactus_1":
                        if selected_choice == "right_choice":
                            selected_choice = "nothing"
                            game_state = "dialogue"
                            current_dialogue = cactus_sad
                            cactus = cactus_angry
                            current_index = 0
                            dialogue_box_visible = True
                        elif selected_choice == "left_choice":
                            selected_choice = "nothing"
                            game_state = "dialogue"
                            trivia_active = True
                            trivia_question_num = 0
                            round_score = 0
                            trivia_question_setup()
                            current_index = 0
                            dialogue_box_visible = False

                    
                    

                    elif trivia_active:
                        if trivia_selected == correct_position:
                            cactus = cactus_points_won
                            total_score += 5
                            round_score += 5
                            trivia_question_num += 1

                            if trivia_question_num >= 3:
                                trivia_done = True
                                trivia_active = False
                                cactus_last_line = random.choice(lines)
                                narrator_last_line = random.choice(narrator_lines)
                                score_line = f"You got {round_score} points. Your total score is {total_score}!"
                                showing_trivia_result = True
                                dialogue_box_visible = False
                                result_timer = pygame.time.get_ticks()
                                
                            else:
                                trivia_question_setup()
                        elif trivia_selected != correct_position:
                            cactus = cactus_points_loss
                            total_score -= 5
                            round_score -= 5
                            trivia_question_num += 1
                            check_score()
                            if total_score >= 0:
                                if trivia_question_num >= 3:
                                    trivia_done = True
                                    trivia_active = False
                                    lines = ["That was soooo much fun!", "Till next time!", "Fun, right?", "Bye!"]
                                    narrator_lines = ["That was weird.", "What was that?", "Well, that is your life now."]
                                    cactus_last_line = random.choice(lines)
                                    narrator_last_line = random.choice(narrator_lines)
                                    score_line = f"You got {round_score} points. Your total score is {total_score}!"
                                    showing_trivia_result = True
                                    dialogue_box_visible = False
                                    result_timer = pygame.time.get_ticks()
                                else:
                                    trivia_question_setup()     

                    elif game_state == "bucket_choice" and not bucket_taken:
                        if selected_choice == "right_choice":
                            selected_choice = "nothing"
                            game_state = "dialogue"
                            jeep_vs_pond_main = ["You left the bucket"] + jeep_vs_pond
                            current_dialogue = jeep_vs_pond_main
                            current_index = 0
                            dialogue_box_visible = True
                        elif selected_choice == "left_choice":
                            selected_choice = "nothing"
                            game_state = "dialogue"
                            inventory_add(bucket_icon)
                            bucket_taken = True
                            
                            jeep_vs_pond_main = ["You took the bucket"] + jeep_vs_pond
                            current_dialogue = jeep_vs_pond_main
                            current_index = 0
                            dialogue_box_visible = True

                    elif game_state == "jeep_vs_pond_choice":
                        if selected_choice == "right_choice":
                            selected_choice = "nothing"
                            game_state = "dialogue"
                            current_dialogue = jeep_dialogue
                            current_bg = bg_jeep
                            current_index = 0
                            dialogue_box_visible = True
                        elif selected_choice == "left_choice":
                            selected_choice = "nothing"
                            game_state = "dialogue"
                            current_dialogue = pond_dialogue
                            current_bg = bg_pond
                            current_index = 0
                            dialogue_box_visible = True
    
                    elif game_state == "pond_choices":
                        if selected_choice == "right_choice":
                            selected_choice = "nothing"
                            total_score -= 5
                            check_score()
                            if total_score >= 0:
                                current_dialogue = pond_back_dialogue
                                game_state = "dialogue"
                                current_index = 0
                                dialogue_box_visible = True
                        elif selected_choice == "left_choice":
                            selected_choice = "nothing" 
                            if rare_event_mirage == 1:
                                current_dialogue = cactus_rare_dialogue
                                game_state = "dialogue"
                                current_index = 0
                                dialogue_box_visible = True
                            else:
                                current_dialogue = mirage_dialogue
                                game_state = "dialogue"
                                current_index = 0
                                dialogue_box_visible = True

                        
                            
                            

                    elif game_state == "cactus_rare_choices":
                        if selected_choice == "right_choice":
                            selected_choice = "nothing"
                            current_dialogue = cactus_rare_sad
                            game_state = "dialogue"
                            current_index = 0
                            dialogue_box_visible = True
                        elif selected_choice == "left_choice":
                            selected_choice = "nothing"
                            current_dialogue = cactus_rare_happy
                            game_state = "dialogue"
                            current_index = 0
                            dialogue_box_visible = True

                    elif game_state == "jeep_choices": 
                        if selected_choice == "right_choice":
                            selected_choice = "nothing"
                            total_score -= 5
                            check_score()
                            if total_score >= 0:
                                jeep_back_dialogue = ["You lost 5 points for changing your choice!", f"Your score now is {total_score}.", "nothing"] 
                                game_state = "dialogue"
                                current_dialogue = jeep_back_dialogue
                                current_index = 0
                                dialogue_box_visible = True
                        elif selected_choice == "left_choice":
                            selected_choice = "nothing"
                            current_dialogue = jeep_man_talk
                            game_state = "dialogue"
                            current_index = 0
                            dialogue_box_visible = True    
    #HERE
                    elif game_state == "jeep_bucket_choices":
                        if selected_choice == "left_choice":
                            selected_choice = "nothing"
                            current_dialogue = bucket_given_dialogue
                            inventory_items.remove(bucket_icon)
                            game_state = "dialogue"
                            current_index = 0
                            dialogue_box_visible = True
                        elif selected_choice == "right_choice":
                            selected_choice = "nothing"
                            total_score -= 5
                            check_score()
                            if total_score >= 0:
                                current_dialogue = bucket_thrown_dialogue
                                inventory_items.remove(bucket_icon)
                                game_state = "dialogue"
                                current_index = 0
                                dialogue_box_visible = True

                    elif dialogue_box_visible and game_state == "trivia_game_2":
                        if selected_choice == "left_choice":
                            current_bg = bg_jeep
                            selected_choice = "nothing"
                            trivia_round = 2
                            trivia_active = True
                            trivia_question_num = 0
                            round_score = 0
                            trivia_question_setup()
                            game_state = "dialogue"
                            dialogue_box_visible = False
                        elif selected_choice == "right_choice":
                            selected_choice = "nothing"
                            cactus = cactus_angry
                            current_dialogue = ["You refuse.",
                                            "Fine! FINE. I won't help you next time!",
                                            "That cactus is weird"]
                            current_index = 0
                            dialogue_box_visible = True
                            game_state = "dialogue"
                            man_back = True
                            man_back_timer = pygame.time.get_ticks()
                            bucket_scene_started = False  

                    elif game_state == "jeep_no_bucket_choices":
                        if selected_choice == "right_choice":
                            selected_choice = "nothing"
                            current_dialogue = stare_man_dialogue
                            game_state = "dialogue"
                            current_index = 0
                            dialogue_box_visible = True
                        elif selected_choice == "left_choice":
                            selected_choice = "nothing"
                            current_dialogue = help_dialogue
                            game_state = "dialogue"
                            current_index = 0
                            dialogue_box_visible = True
                    
                    elif game_state == "pet_choices":
                        if selected_choice == "right_choice":
                            selected_choice = "nothing"
                            current_dialogue = pet_rejected_dialogue
                            game_state = "dialogue"
                            current_index = 0
                            dialogue_box_visible = True
                        elif selected_choice == "left_choice":
                            selected_choice = "nothing"
                            current_dialogue = pet_accepted_dialogue
                            game_state = "dialogue"
                            current_index = 0
                            dialogue_box_visible = True

                    elif game_state == "coin_choices":
                        jeep_man_visible = False
                        if selected_choice == "right_choice":
                            selected_choice = "nothing"
                            current_dialogue = coin_given_dialogue
                            game_state = "dialogue"
                            current_index = 0
                            dialogue_box_visible = True
                        elif selected_choice == "left_choice":
                            selected_choice = "nothing"
                            current_dialogue = thanked_dialogue
                            game_state = "dialogue"
                            current_index = 0
                            dialogue_box_visible = True
                        
                    elif game_state == "buy":
                        if selected_choice == "right_choice":
                            selected_choice = "nothing"
                            current_dialogue = only_one
                            game_state = "dialogue"
                            current_index = 0
                            dialogue_box_visible = True
                        elif selected_choice == "left_choice":
                            selected_choice = "nothing"
                            current_dialogue = both_dialogue
                            game_state = "dialogue"
                            current_index = 0
                            dialogue_box_visible = True
                    
                    elif game_state == "buy_score":
                        if selected_choice == "right_choice":
                            selected_choice = "nothing"
                            current_dialogue = refuse_food
                            game_state = "dialogue"
                            current_index = 0
                            dialogue_box_visible = True
                        elif selected_choice == "left_choice":
                            selected_choice = "nothing"
                            current_dialogue = score_food
                            game_state = "dialogue"
                            current_index = 0
                            dialogue_box_visible = True

                    elif dialogue_box_visible and game_state == "cactus_eating_choices":
                        if selected_choice == "left_choice":
                            current_bg = bg_sunset_sitting   
                            selected_choice = "nothing"
                            trivia_round = 3
                            trivia_active = True
                            trivia_question_num = 0
                            round_score = 0
                            trivia_question_setup()
                            game_state = "dialogue"
                            dialogue_box_visible = False
                        elif selected_choice == "right_choice":
                            selected_choice = "nothing"
                            cactus = cactus_angry
                            current_dialogue = ["You throw the cup at it.",
                                            "OW! That was really unnecessary! I was going anyway!",
                                            "It vanishes looking deeply offended.",
                                            "Really weird."]
                            current_index = 0
                            dialogue_box_visible = True
                            game_state = "dialogue"
                            trivia_3_done = True
                            trivia_3_timer = pygame.time.get_ticks()
                    
                if game_state == "pet_naming":
                    inventory_visible = False
                    if event.key == pygame.K_BACKSPACE:
                        pet_name_input = pet_name_input[:-1]
                    if event.key == pygame.K_RETURN and pet_name_input != "":
                        endings = False
                        inventory_visible = True
                        pet_name = pet_name_input
                        pet_name_input = ""
                        pygame.key.stop_text_input()
                        game_state = "dialogue"
                        dialogue_box_visible = True
                        naming_active = False
                        pet_name_done[0] = f"Your pet name is {pet_name}"
                        current_index = 0
                        current_dialogue = pet_name_done

                elif game_state == "evil_cactus_choices":
                        if selected_choice == "right_choice":
                            selected_choice = "nothing"
                            current_dialogue = bad_ending_pet_no
                            game_state = "dialogue"
                            current_index = 0
                            dialogue_box_visible = True
                        elif selected_choice == "left_choice":
                            selected_choice = "nothing"
                            current_dialogue = bad_ending_pet_yes
                            game_state = "dialogue"
                            current_index = 0
                            dialogue_box_visible = True

                elif game_state == "evil_cactus_choices_no_pet":
                        if selected_choice == "right_choice":
                            selected_choice = "nothing"
                            current_dialogue = bad_ending_no_pet_no
                            game_state = "dialogue"
                            current_index = 0
                            dialogue_box_visible = True
                        elif selected_choice == "left_choice":
                            selected_choice = "nothing"
                            current_dialogue = bad_ending_no_pet_yes
                            game_state = "dialogue"
                            current_index = 0
                            dialogue_box_visible = True
                        

                if event.key == pygame.K_RIGHT:
                    if choice_character_visible:
                        selected_choice = "right_choice"
                    if trivia_active:
                        if trivia_selected == "A":
                            trivia_selected = "B"
                        elif trivia_selected == "C":
                            trivia_selected = "D"
                            
                        

                if event.key == pygame.K_LEFT:
                    if choice_character_visible:
                        selected_choice = "left_choice"
                    if trivia_active:
                            if trivia_selected == "B":
                                trivia_selected = "A"
                            elif trivia_selected == "D":
                                trivia_selected = "C"

                if event.key == pygame.K_UP:
                    if trivia_active:
                            if trivia_selected == "C":
                                trivia_selected = "A"
                            elif trivia_selected == "D":
                                trivia_selected = "B"

                if event.key == pygame.K_DOWN:
                    if trivia_active:
                        if trivia_selected == "A":
                            trivia_selected = "C"
                        elif trivia_selected == "B":
                            trivia_selected = "D"

            elif event.type == pygame.TEXTINPUT:
                if game_state == "pet_naming":
                    if font.size(pet_name_input + event.text)[0] < 580:
                        pet_name_input += event.text
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
        
        start()
        current_time = pygame.time.get_ticks()

        if current_time - dialogue_time > 3000 and not intro_started:
            dialogue_box_visible = True
            intro_started = True
        

        if current_dialogue == intro:
            if current_index >= 6:
                cactus_visible = True
            if current_index == len(current_dialogue) - 1:
                current_index = 0
                game_state = "dialogue"
                if cactus_intro_done:
                    current_dialogue = cactus_1st_dialogue
                else:   
                    current_dialogue = cactus_intro

        if current_dialogue == cactus_intro:
            cactus_intro_done = True
            dialogue_character = dialogue_cactus
            if current_index == 1:
                cactus = cactus_happy
            if current_index == 2:
                cactus = cactus_dissappointed
            if current_index == 3:
                cactus = cactus_happy
            if current_index == 4:
                cactus = cactus_normal
            if current_index == 11:
                cactus = cactus_happy
            if current_index == len(current_dialogue) - 1:
                cactus = cactus_normal
                current_index = 0
                game_state = "dialogue"
                current_dialogue = cactus_1st_dialogue
        

        if cactus_visible:
            if cactus_width < 300:
                cactus_width += 1
                cactus_height += 1.67

        scaled_cactus = pygame.transform.scale(cactus, (int(cactus_width), int(cactus_height)))
        x = (WIDTH - int(cactus_width)) // 2
        y = 680 - int(cactus_height) + math.sin(pygame.time.get_ticks() / 500) * 10
        if cactus_visible:
            screen.blit(scaled_cactus, (x, y))
        if not cactus_1st_dialogue_started and intro_done:
            dialogue_box_visible = True
            cactus_1st_dialogue_started = True
            current_dialogue = cactus_1st_dialogue
            dialogue_character = dialogue_cactus
            current_index = 0

        if current_dialogue == cactus_1st_dialogue:
            if current_index == len(current_dialogue) - 1 and not cactus_questions_started:
                cactus_1st_dialogue_done = True
                game_state = "choice_cactus_1"
                cactus_questions_started = True


        if current_dialogue == cactus_sad:
            if current_index == len(current_dialogue) - 1:
                cactus_visible = False
                cactus = cactus_normal
                dialogue_character = dialogue_ch
                if not dialogue_box_visible and not bucket_scene_started:
                    bucket_timer = pygame.time.get_ticks()
                    bucket_scene_started = True
                if current_index == 1:
                    dialogue_character = dialogue_cactus
                if current_index == 2:
                    dialogue_character = dialogue_ch
        
        if current_dialogue == trivia_dialogue:
            if current_index == 2:
                cactus_visible = False
                dialogue_character = dialogue_ch
            if trivia_round == 1:
                if current_index == len(trivia_dialogue) - 1 and not dialogue_box_visible and not post_trivia_1_done:
                    post_trivia_1_done = True
                    bucket_timer = pygame.time.get_ticks()
                    bucket_scene_started = True
                #TRIVIA ROUND 2
            elif trivia_round == 2:
                if current_index == len(trivia_dialogue) - 1 and not dialogue_box_visible and not man_back:
                    man_back = True
                    man_back_timer = pygame.time.get_ticks()
                    bucket_scene_started = False

            elif trivia_round == 3:
                if current_index == len(trivia_dialogue) - 1 and not dialogue_box_visible and not trivia_3_done:
                    trivia_3_done = True
                    trivia_3_timer = pygame.time.get_ticks()

        if current_dialogue == bucket_dialogue:
            if current_index == 1:
                current_bg = bg2 
            if current_index == len(current_dialogue) - 1:
                game_state = "bucket_choice"
                bucket_choice_started = True

        if current_dialogue == jeep_vs_pond_main:
            if current_index == 0 or current_index == 1:
                current_bg = bg2
            elif current_index == 2:
                current_bg = bg_pond
            elif current_index == 3:
                current_bg = bg_jeep
            elif current_index == 4:
                current_bg = bg2

            if current_index == len(current_dialogue) - 1:
                game_state = "jeep_vs_pond_choice"
        
        
        if current_dialogue == pond_dialogue:
            if current_index == 3:
                game_state = "pond_choices"
        
        if current_dialogue == pond_back_dialogue:
            if current_index == 2:
                current_bg = bg2
            if current_index == len(current_dialogue) - 1:
                game_state = "jeep_vs_pond_choice"

        if current_dialogue == cactus_rare_dialogue:
            if current_index == 1:
                cactus_visible = True
            if current_index == 2:
                dialogue_character = dialogue_cactus
            if current_index == len(current_dialogue) - 1:
                game_state = "cactus_rare_choices"
                dialogue_character = dialogue_ch

        if current_dialogue == cactus_rare_happy:
            cactus_visible = False
            if not cactus_points:
                total_score += 20
                cactus_points = True
                cactus_rare_happy[4] = f"Your total score now is {total_score}."
            if current_index == 0:
                current_bg = bg_flying
            if current_index == 1:
                current_bg = bg_jeep
            if current_index == 2:
                dialogue_character = dialogue_cactus
                cactus_visible = True
            if current_index == 3:
                cactus_visible = True
            if current_index == 5:
                cactus_visible = False
                dialogue_character = dialogue_ch
            if current_index == len(current_dialogue) - 1:
                current_index = 2
                current_dialogue = jeep_dialogue

        if current_dialogue == cactus_rare_sad:
            cactus = cactus_angry
            if current_index == 0:
                dialogue_character = dialogue_cactus
            if current_index == 1:
                dialogue_character = dialogue_ch
                cactus_visible = False
            if current_index == 3:
                current_bg = bg_walking_1
            if current_index == 4:
                current_bg = bg_walking_2
            if current_index == 5:
                current_bg = bg_walking_1
            if current_index == 6:
                current_bg = bg_collapse
            if current_index == 8:
                current_bg = bg_flying
            if current_index == len(current_dialogue) - 1:
                game_state = "game_over"
                refuse_cactus_visible = True

        if current_dialogue == mirage_dialogue:
            if current_index == 0:
                current_bg = bg_walking_2
            if current_index == 1:
                current_bg = bg_walking_3
            if current_index == 2:
                current_bg = bg_collapse
            if current_index == len(current_dialogue) - 1:
                current_dialogue = ["You collapsed in the desert heat.."]
                current_index = 0
                game_state = "game_over"
                collapsed_sand_visible = True

        if current_dialogue == jeep_dialogue:
            if current_index == 0:
                current_bg = bg_walking_3
            if current_index == 1:
                current_bg = bg_jeep_man_inspecting
            if current_index == 2:
                current_bg = bg_jeep_man_inspecting
            if current_index == len(current_dialogue) - 1:
                game_state = "jeep_choices" 
            
        if current_dialogue == jeep_back_dialogue:
            if current_index == 1:
                current_bg = bg2
            if current_index == len(current_dialogue) - 1:
                current_dialogue = jeep_vs_pond_main
                current_index = 1  
                dialogue_box_visible = True

        if current_dialogue == jeep_man_talk:
            if current_index == 1:
                current_bg = bg_jeep
                jeep_man_visible = True
            if current_index == 2:
                dialogue_character = dialogue_man
            if current_index == 5:
                dialogue_character = dialogue_ch
            if current_index == len(current_dialogue) - 1:
                if bucket_icon in inventory_items:
                    game_state = "jeep_bucket_choices"
                else:
                    game_state = "jeep_no_bucket_choices"

        elif current_dialogue == bucket_given_dialogue:
            if current_index == len(current_dialogue) - 1 and not trivia_2_started:
                game_state = "trivia_game_2"
                trivia_2_started = True
                dialogue_box_visible = True
            if current_index == 0:
                if bucket_icon in inventory_items:
                    inventory_items.remove(bucket_icon)
            if current_index == 1:
                jeep_man_visible = False
                current_bg = bg_jeep
            if current_index == 3:
                cactus_visible = True
            if current_index == 4:
                dialogue_character = dialogue_cactus

        elif current_dialogue == bucket_thrown_dialogue:
            if current_index == len(current_dialogue) - 1:
                game_state = "trivia_game_2"
                dialogue_box_visible = True
            if current_index == 0:
                if bucket_icon in inventory_items:
                    inventory_items.remove(bucket_icon)
            if current_index == 1:
                jeep_man = jeep_man_angry
                dialogue_character = dialogue_man
            if current_index == 2:
                dialogue_character = dialogue_ch
            if current_index == 3:
                dialogue_character = dialogue_man
            if current_index == 4:
                jeep_man_visible = False
                dialogue_character = dialogue_ch
            if current_index == 5:
                jeep_man_visible = True
                dialogue_character = dialogue_man
            if current_index == 6:
                dialogue_character = dialogue_ch
            if current_index == 7:
                dialogue_character = dialogue_man
                jeep_man = jeep_man_normal
            if current_index == 8:
                dialogue_character = dialogue_ch
                jeep_man_visible = False
            if current_index == 10:
                cactus_visible = True
            if current_index == 11:
                dialogue_character = dialogue_cactus


            

        elif current_dialogue == man_back_dialogue:
            if current_index == 0:
                jeep_man = jeep_man_bucket
                jeep_man_visible = True
            if current_index == 1:
                jeep_man_visible = False
                current_bg = bg_jeep_man_inspecting
            if current_index == 3 and not man_back_bonus:
                man_back_bonus = True
                total_score += 10
                man_back_dialogue[4] = f"Your total score now is {total_score}."
                check_score()
            if current_index == 5:
                jeep_man = jeep_man_normal
                jeep_man_visible = True
                dialogue_character = dialogue_man
                current_bg = bg_jeep
            if current_index == 6:
                dialogue_character = dialogue_ch
                jeep_man_visible = False
                current_bg = bg_in_jeep
            if current_index == 7:
                current_bg = bg_flying
            if current_index == 11:
                current_bg = bg_village_entrance
            if current_index == 12:
                dialogue_character = dialogue_man
            if current_index == len(current_dialogue) - 1:
                dialogue_character = dialogue_ch
                jeep_man_visible = False
                game_state = "coin_choices"
                dialogue_box_visible = True
                man_back = False

        elif current_dialogue == coin_given_dialogue:
            jeep_man_visible = False
            if current_index == 0:
                dialogue_character = dialogue_man
            if current_index == 3:
                dialogue_character = dialogue_ch
            if current_index == 4:
                dialogue_character = dialogue_man
            if current_index == 5:
                dialogue_character = dialogue_ch
                if not coin_added:
                    inventory_items.append(coin_icon)
                    coin_added = True
            if current_index == len(current_dialogue) - 1:
                current_dialogue = pet_dialogue
                current_index = 0
                dialogue_box_visible = True

        elif current_dialogue == thanked_dialogue:
            jeep_man_visible = False
            if current_index == len(current_dialogue) - 1:
                current_dialogue = pet_dialogue
                current_index = 0
                dialogue_box_visible = True
                


        elif current_dialogue == pet_dialogue:
            pet_dialogue[9] = f"You turn around—it’s {the_pet}"
            pet_dialogue[10] = f"{pet_condition_1}"
            if current_index == 0:
                current_bg = bg2
            if current_index == 2:
                current_bg = bg_walking_1
            if current_index == 3:
                current_bg = bg_walking_2
            if current_index == 4:
                current_bg = bg_walking_3
            if current_index == 5:
                current_bg = bg2
            if current_index == 6:
                current_bg = bg_walking_3
            if current_index == 7:
                current_bg = bg2
            if current_index == 9:
                pet_visible = True
            if current_index == len(current_dialogue) - 1:
                game_state = "pet_choices"
                dialogue_box_visible = True

        elif current_dialogue == ["You refuse.", "Fine! FINE. I won't help you next time!", "That cactus is weird"]:
            if current_index == 1:
                dialogue_character = dialogue_cactus
            if current_index == 2:
                dialogue_character = dialogue_ch
                cactus_visible = False
            if current_index == len(current_dialogue) - 1:
                cactus = cactus_normal
            
        elif current_dialogue == stare_man_dialogue:
            if current_index == 3:
                dialogue_character = dialogue_man
            if current_index == 4:
                dialogue_character = dialogue_ch
            if current_index == 5:
                dialogue_character = dialogue_man
            if current_index == len(current_dialogue) - 1:
                current_dialogue = man_die
                current_index = 0

        elif current_dialogue == help_dialogue:
            if current_index == 1:
                dialogue_character = dialogue_man
            if current_index == 2:
                dialogue_character = dialogue_ch    
            if current_index == 3:
                dialogue_character = dialogue_man
            if current_index == 4:
                dialogue_character = dialogue_ch
            if current_index == 5:
                dialogue_character = dialogue_man
            if current_index == len(current_dialogue) - 1:
                current_dialogue = man_die
                current_index = 0
                dialogue_character = dialogue_ch
            
        elif current_dialogue == man_die:
            man_die[4] = f"You hear a strange sound in the distance —{strange_sound}, you think."
            if current_index == 0:
                jeep_man_visible = False
                current_bg = bg_jeep_man_inspecting
            if current_index == 2:
                current_bg = bg_jeep_night_1
            if current_index == 3:
                current_bg = bg_jeep_night_2
            if current_index == 6:
                current_bg = bg_jeep_night_3
            if current_index == 7:
                current_bg = bg_stars  
            if current_index == 8:
                current_bg = bg_stars_blur
            if current_index == 9:
                current_bg = bg_flying
            if current_index == len(current_dialogue) - 1:
                game_state = "game_over"
                collapse_exhaustion_visible = True
        
        if current_dialogue == pet_rejected_dialogue:
            if current_index == 2:
                pet_visible = False
            if current_index == 3:
                current_bg = bg_walking_2
            if current_index == len(current_dialogue) - 1:
                current_dialogue = village_walking
                current_index = 0

        if current_dialogue == pet_accepted_dialogue:
            if current_index == len(current_dialogue) - 1 and not naming_active:
                pet_taken = True
                game_state = "pet_naming"
                pygame.key.start_text_input()
                pet_name_input = ""
                naming_active = True

        if current_dialogue == pet_name_done:
            pet_name_done[1] = f"{player_pet_status}"
            if current_index == len(current_dialogue) - 1:
                current_index = 0 
                current_dialogue = village_walking

        if current_dialogue == village_walking:
            pet_visible = False
            if current_index == 0:
                current_bg = bg_walking_1
            if current_index == 1:
                current_bg = bg2
            if current_index == len(current_dialogue) - 1:
                current_index = 0
                dialogue_box_visible = True
                current_dialogue = shop_dialogue

        if current_dialogue == shop_dialogue:
            if current_index == 0:
                current_bg = bg_walking_3
            if current_index == 1:
                current_bg = bg_shop_far1
            if current_index == 2:
                current_bg = bg_shop_far2
            if current_index == 3:
                current_bg = bg_shop_far3
            if current_index == 4:
                current_bg = bg_shop_far4
            if current_index == 5:
                current_bg = bg_shop
            if current_index == 6:
                dialogue_character = dialogue_woman
            if current_index == len(current_dialogue) - 1:
                current_bg = bg_shop
                current_index = 0
                dialogue_box_visible = True
                if coin_icon in inventory_items:
                    game_state = "buy"
                else:
                    current_dialogue = no_coin_dialogue

        if current_dialogue == no_coin_dialogue:
            current_bg = bg_shop
            if  current_index == 0:
                dialogue_character = dialogue_ch
            if current_index == 2:
                dialogue_character = dialogue_woman
            if current_index == len(current_dialogue) - 1:
                dialogue_character = dialogue_ch
                current_index = 0
                dialogue_box_visible = True
                if total_score > 20:
                    game_state = "buy_score"
                else:
                    current_dialogue = no_money_shop

        if current_dialogue == no_money_shop:
            no_money_shop[4] = f"She hands you {the_food} and {the_drink}"
            current_bg = bg_shop
            if current_index == 0:
                dialogue_character = dialogue_woman
            if current_index == 1:
                dialogue_character = dialogue_ch
            if current_index == 3:
                dialogue_character = dialogue_woman
            if current_index == 4:
                dialogue_character = dialogue_ch
                if not food_added:
                    inventory_items.append(the_food_img)
                    food_added = True
                if not drink_added:
                    inventory_items.append(the_drink_img)
                    drink_added = True
            if current_index == 5:
                dialogue_character = dialogue_woman
            if current_index == 6:
                dialogue_character = dialogue_ch
            if current_index == 7:
                dialogue_character = dialogue_woman
            if current_index == 8:
                dialogue_character = dialogue_ch
            if current_index == len(current_dialogue) - 1:
                dialogue_character = dialogue_ch
                current_index = 0
                dialogue_box_visible = True
                current_dialogue = eating_dialogue


        if current_dialogue == score_food:
            score_food[2] = f"She hands you {the_food} and {the_drink}"
            current_bg = bg_shop
            if current_index == 0:
                dialogue_character = dialogue_ch
            if current_index == 1:
                dialogue_character = dialogue_woman
            if current_index == 2:
                dialogue_character = dialogue_ch
                if not food_added:
                    inventory_items.append(the_food_img)
                    food_added = True
                if not drink_added:
                    inventory_items.append(the_drink_img)
                    drink_added = True
            if current_index == 3 and not score_minus_twenty:
                total_score -= 20
                score_food[3] = f"Your total score is now {total_score}"
                score_minus_twenty = True 
            if current_index == len(current_dialogue) - 1:
                dialogue_character = dialogue_ch
                current_index = 0
                dialogue_box_visible = True
                current_dialogue = eating_dialogue

        if current_dialogue == only_one:
            only_one[2] = f"She hands you {the_drink} and gives you some change."
            only_one[3] = f"You use the change to buy yourself something to eat, she hands you {the_food}"
            if coin_icon in inventory_items:
                inventory_items.remove(coin_icon)
            current_bg = bg_shop
            if current_index == 1:
                dialogue_character = dialogue_woman
            if current_index == 2:
                dialogue_character = dialogue_ch
                if not drink_added:
                    inventory_items.append(the_drink_img)
                    drink_added = True
            if current_index == 3:
                if not food_added:
                    inventory_items.append(the_food_img)
                    food_added = True
            if current_index == len(current_dialogue) - 1:
                dialogue_character = dialogue_ch
                current_index = 0
                dialogue_box_visible = True
                current_dialogue = eating_dialogue

        if current_dialogue == both_dialogue:
            both_dialogue[1] = f"The woman surprisingly hands you {the_food} and {the_drink}"
            if coin_icon in inventory_items:
                inventory_items.remove(coin_icon)
            current_bg = bg_shop
            if current_index == 0:
                dialogue_character = dialogue_ch
            if current_index == 1:
                if not food_added:
                    inventory_items.append(the_food_img)
                    food_added = True
                if not drink_added:
                    inventory_items.append(the_drink_img)
                    drink_added = True
            if current_index == 2:
                dialogue_character = dialogue_woman
            if current_index == 3:
                dialogue_character = dialogue_ch 
            if current_index == len(current_dialogue) - 1:
                dialogue_character = dialogue_ch
                current_index = 0
                dialogue_box_visible = True
                current_dialogue = eating_dialogue

        if current_dialogue == refuse_food:
            if current_index == 0:
                dialogue_character = dialogue_woman
                current_bg = bg_shop
            if current_index == 1:
                dialogue_character = dialogue_ch
                current_bg = bg2
            if current_index == 2:
                current_bg = bg_walking_1
            if current_index == 3:
                current_bg = bg_collapse
            if current_index == 4:
                current_bg = bg_flying
            if current_index == len(current_dialogue) - 1:
                current_index = 0
                game_state = "game_over"
                refuse_woman_visible = True

        if current_dialogue == eating_dialogue:
            if current_index == 0:
                current_bg = bg_sunset
            if current_index == 1:
                current_bg = bg_sunset_sitting
            if current_index == len(current_dialogue) - 1:
                inventory_items.remove(the_food_img)
                inventory_items.remove(the_drink_img)
                current_index = 0
                dialogue_box_visible = True
                if pet_taken:
                    current_dialogue = eating_pet_dialogue
                else:
                    current_dialogue = cactus_eating_dialogue

        if current_dialogue == eating_pet_dialogue:
            eating_pet_dialogue[1] = f"You look at it, {pet_condition_2}"
            if current_index == 1:
                pet_visible = True
            if current_index == 3:
                pet_visible = False
            if current_index == 5:
                eating_pet_dialogue[5] = f"{pet_name} is sleeping on your lap.."
            if current_index == len(current_dialogue) - 1:
                current_index = 0
                dialogue_box_visible = True
                current_dialogue = cactus_eating_dialogue

        if current_dialogue == cactus_eating_dialogue:
            if current_index == 0:
                cactus_visible = True
                dialogue_character = dialogue_cactus
            if current_index == 1:
                dialogue_character = dialogue_ch
            if current_index == 2:
                dialogue_character = dialogue_cactus
            if current_index == len(current_dialogue) - 1 and not trivia_3_started:
                dialogue_character = dialogue_ch
                game_state = "cactus_eating_choices"
                trivia_3_started = True
                dialogue_box_visible = True

        if current_dialogue == ["You throw the cup at it.", "OW! That was really unnecessary! I was going anyway!", "It vanishes looking deeply offended.", "Really weird."]:
            if current_index == 0:
                dialogue_character = dialogue_ch
            if current_index == 1:
                dialogue_character = dialogue_cactus
            if current_index == 2:
                dialogue_character = dialogue_ch
                cactus_visible = False
            if current_index == len(current_dialogue) - 1:
                cactus = cactus_normal
                cactus_visible = False
                current_index = 0
                dialogue_box_visible = True
                if total_score >= 75: #ENDING
                    current_dialogue = best_ending
                elif 75 > total_score >= 35:
                    current_dialogue = mid_ending 
                elif 35 > total_score:
                    current_dialogue = bad_ending

        if current_dialogue == "weird":
            if total_score >= 75: #ENDING
                    current_dialogue = best_ending
            elif 75 > total_score >= 35:
                    current_dialogue = mid_ending 
            elif 35 > total_score:
                    current_dialogue = bad_ending

        if current_dialogue == best_ending:
            if current_index == 0:
                current_bg = bg_sunset
            if current_index == 1:
                current_bg = bg_sunset_walk_1
            if current_index == 2:
                current_bg = bg_sunset_walk_2
            if current_index == 3:
                current_bg = bg_sunset
            if current_index == 5:
                bro_visible = True
            if current_index == 6:
                dialogue_character = dialogue_bro
            if current_index == 7:
                dialogue_character = dialogue_ch
            if current_index == 8:
                dialogue_character = dialogue_bro
            if current_index == 9:
                dialogue_character = dialogue_ch
            if current_index == 11:
                bro = bro_concerned
                dialogue_character = dialogue_bro
            if current_index == 12:
                bro = bro_sad
                dialogue_character = dialogue_ch
            if current_index == 13:
                dialogue_character = dialogue_bro
            if current_index == 14:
                dialogue_character = dialogue_ch
            if current_index == 15:
                dialogue_character = dialogue_bro
            if current_index == 16:
                bro = bro_concerned
            if current_index == 18:
                dialogue_character = dialogue_ch
            if current_index == 21:
                dialogue_character = dialogue_bro
            if current_index == 22:
                dialogue_character = dialogue_ch
            if current_index == 23:
                bro = bro_normal
                dialogue_character = dialogue_bro
            if current_index == 25:
                dialogue_character = dialogue_ch
            if current_index == len(current_dialogue) - 1:
                current_index = 0
                dialogue_box_visible = True
                if pet_taken:
                    current_dialogue = best_ending_pet
                else:
                    current_dialogue = best_ending_no_pet

        if current_dialogue == best_ending_pet:
            best_ending_pet[1] = f"{pet_condition_3}."
            if current_index == 0:
                pet_visible = True
                bro_visible = False
                best_ending_pet[0] = f"You glance down at your side, you see {pet_name}"
            if current_index == 3:
                pet_visible = False
                current_bg = bg_in_jeep
            if current_index == 5:
                current_bg = bg_flying
            if current_index == len(current_dialogue) - 1:
                game_state = "game_over"
                best_pet_visible = True

        if current_dialogue == best_ending_no_pet:
            if current_index == 0:
                current_bg = bg_in_jeep
            if current_index == 2:
                current_bg = bg_flying
            if current_index == len(current_dialogue) - 1:
                game_state = "game_over"
                best_visible = True

        if current_dialogue == mid_ending:
            if current_index == 0:
                current_bg = bg_sunset
            if current_index == 2:
                jeep_man_visible = True
                jeep_man = jeep_man_normal
                dialogue_character = dialogue_man
            if current_index == 6:
                dialogue_character = dialogue_ch
            if current_index == len(current_dialogue) - 1:
                current_index = 0
                dialogue_box_visible = True
                current_dialogue = transition
            
        if current_dialogue == transition:
            jeep_man_visible = False
            current_bg = bg_flying
            if current_index == len(current_dialogue) - 1:
                current_index = 0
                dialogue_box_visible = True
                if pet_taken:
                    current_dialogue = mid_ending_pet
                else:
                    current_dialogue = mid_ending_no_pet

        if current_dialogue == mid_ending_pet:
            mid_ending_pet[1] = f"{pet_condition_3}."
            current_bg = bg_mid_pet
            mid_ending_pet[0] = f"You and {pet_name} now work in the cozy little shop."
            if current_index == len(current_dialogue) - 1:
                game_state = "game_over"
                mid_pet_visible = True

        if current_dialogue == mid_ending_no_pet:
            current_bg = bg_mid_no_pet
            if current_index == len(current_dialogue) - 1:
                game_state = "game_over"
                mid_visible = True

        if current_dialogue == bad_ending:
            if current_index == 1:
                current_bg = bg_sunset
            if current_index == 3:
                dialogue_character = dialogue_cactus
            if current_index == 4:
                dialogue_character = dialogue_ch
                cactus_visible = True
            if current_index == 9:
                dialogue_character = dialogue_cactus
                cactus = cactus_angry
            if current_index == 10:
                dialogue_character = dialogue_ch
            if current_index == len(current_dialogue) - 1:
                current_index = 0
                dialogue_box_visible = True
                if pet_taken:
                    current_dialogue = bad_ending_pet
                else:
                    current_dialogue = bad_ending_no_pet
            
        if current_dialogue == bad_ending_pet:
            bad_ending_pet[2] = f"But you do have {pet_name}! Cute little thing!"
            bad_ending_pet[11] = f"—I get to keep {pet_name}."
            if current_index == 0:
                cactus = cactus_normal
                dialogue_character = dialogue_cactus
            if current_index == 1:
                cactus = cactus_shocked
            if current_index == 2:
                cactus = cactus_normal
            if current_index == 3:
                dialogue_character = dialogue_ch
            if current_index == 6:
                dialogue_character = dialogue_cactus
            if current_index == 11:
                cactus = cactus_evil
            if current_index == len(current_dialogue) - 1:
                game_state = "evil_cactus_choices"
                cactus = cactus_normal
        
        if current_dialogue == bad_ending_pet_no:
            bad_ending_pet_no[4] = f"Alone. No {pet_name} in sight."
            if current_index == 0:
                cactus = cactus_evil
                dialogue_character = dialogue_cactus
            if current_index == 1:
                cactus_visible = False
                current_bg = bg_white
                dialogue_character = dialogue_ch
            if current_index == 3:
                current_bg = bg_bad_ending
                bad_ending_pet_no[4] = f"Alone. No {pet_name} in sight."
            if current_index == 6:
                current_bg = bg_bad_ending
            if current_index == len(current_dialogue) - 1:
                game_state = "game_over"
                bad_pet_visible = True

        if current_dialogue == bad_ending_pet_yes:
            bad_ending_pet_yes[4] = f"Alone. No {pet_name} in sight."
            if current_index == 0:
                cactus = cactus_evil
                dialogue_character = dialogue_cactus
            if current_index == 1:
                cactus_visible = False
                current_bg = bg_white
                dialogue_character = dialogue_ch
            if current_index == 3:
                current_bg = bg_bad_ending
            if current_index == 6:
                current_bg = bg_bad_ending
            if current_index == len(current_dialogue) - 1:
                game_state = "game_over"
                bad_pet_visible = True
                
        if current_dialogue == bad_ending_no_pet:
            bad_ending_no_pet[12] = f"{total_score} points, right?"
            if current_index == 0:
                cactus = cactus_normal
                dialogue_character = dialogue_cactus
            if current_index == 1:
                cactus = cactus_dissappointed
                dialogue_character = dialogue_ch
            if current_index == 2:
                cactus = cactus_normal
                dialogue_character = dialogue_cactus
            if current_index == 3:
                dialogue_character = dialogue_ch
            if current_index == 6:
                dialogue_character = dialogue_cactus
            if current_index == 8:
                catus = cactus_happy
            if current_index == 9:
                cactus = cactus_normal
            if current_index == 11:
                cactus = cactus_evil
            if current_index == len(current_dialogue) - 1:
                game_state = "evil_cactus_choices_no_pet"
                cactus = cactus_normal
                
            
        if current_dialogue == bad_ending_no_pet_no:
            if current_index == 0:
                cactus = cactus_evil
                dialogue_character = dialogue_cactus
            if current_index == 1:
                cactus_visible = False
                current_bg = bg_white
                dialogue_character = dialogue_ch
            if current_index == 3:
                current_bg = bg_bad_ending
            if current_index == 7:
                current_bg = bg_bad_ending
            if current_index == len(current_dialogue) - 1:
                game_state = "game_over"
                bad_visible = True

        if current_dialogue == bad_ending_no_pet_yes:
            if current_index == 0:
                cactus = cactus_evil
                dialogue_character = dialogue_cactus
            if current_index == 1:
                cactus_visible = False
                current_bg = bg_white
                dialogue_character = dialogue_ch
            if current_index == 3:
                current_bg = bg_bad_ending
            if current_index == 7:
                current_bg = bg_bad_ending
            if current_index == len(current_dialogue) - 1:
                game_state = "game_over"
                bad_visible = True
                    
        if current_bg == bg2:
            if not bucket_taken:
                screen.blit(bucket_img, (510,352))
            

        

        if bucket_scene_started and not dialogue_box_visible:
            if current_time - bucket_timer > 2000 and not bucket_choice_started:
                current_dialogue = bucket_dialogue
                current_index = 0
                dialogue_box_visible = True

        if man_back and not dialogue_box_visible:
            if current_time - man_back_timer > 2000:
                man_back_dialogue[4] = f"Your total score now is {total_score} points!"  
                current_dialogue = man_back_dialogue
                current_index = 0
                dialogue_box_visible = True

        if trivia_3_done and not dialogue_box_visible: 
            if current_time - trivia_3_timer > 2000:
                current_dialogue = "weird"
                current_index = 0
                dialogue_box_visible = True

        if the_pet == "a cat":
            the_pet_img = pet_cat
        elif the_pet == "a turtle":
            the_pet_img = pet_turtle
        elif the_pet == "a..goat?":
            the_pet_img = pet_goat
        elif the_pet == "a rabbit":
            the_pet_img = pet_rabbit
        elif the_pet == "a bird":
            the_pet_img = pet_bird
        elif the_pet == "a monkey":
            the_pet_img = pet_monkey
        elif the_pet == "a cactus, it may be your imagination or dehydration but..":
            the_pet_img = pet_cactus

        if the_food == "camel meat and bread":
            the_food_img = c_m_b_icon
        elif the_food == "lamb and bread":
            the_food_img = s_m_b_icon
        elif the_food == "plain bread, you are hungry you can't complain":
            the_food_img = bread_icon
        elif the_food == "fruit salad":
            the_food_img = fruit_salad_icon
        elif the_food == "plate of rice":
            the_food_img = rice_icon
        elif the_food == "salad":
            the_food_img = salad_icon
        elif the_food == "chicken and bread":
            the_food_img = chicken_and_bread_icon
        elif the_food == "a strange sandwich, it smells like goat cheese, let's hope it tastes good.":
            the_food_img = sandwich_icon
        elif the_food == "goat cheese":
            the_food_img = goat_cheese_icon

        if the_drink == "warm water":
            the_drink_img = warm_water_icon
        elif the_drink == "water":
            the_drink_img = water_icon
        elif the_drink == "cold water":
            the_drink_img = cold_water_icon
        elif the_drink == "a..smoothie? How did it come here?":
            the_drink_img = smoothie_icon
        elif the_drink == "orange juice":
            the_drink_img = orange_juice_icon
        elif the_drink == "coconut water":
            the_drink_img = coconut_water_icon   
        elif the_drink == "tea? that may do":
            the_drink_img = tea_icon
        elif the_drink == "green juice.. you are thiristy, you can't complain":
            the_drink_img = green_juice_icon

        if jeep_man_visible: 
                screen.blit(jeep_man, (480, 280))  

        if bro_visible: 
                screen.blit(bro, (480, 280))      

        if pet_visible:
            screen.blit(the_pet_img, (480, 280))  

        
        if game_state == "dialogue":
            dialogue_check()
        elif game_state == "choice_cactus_1":
            cactus_questions("That was weird", "That was soooo much fun!") 
        elif game_state == "game_over":
            dialogue_check() 

        elif game_state == "bucket_choice":
            choices("Take the bucket", "Leave the bucket")

        elif game_state == "jeep_vs_pond_choice":
            choices("Walk to the pond", "Walk to the jeep")

        elif game_state == "pond_choices":
            choices("Keep walking", "Go back")

        elif game_state == "cactus_rare_choices":
            choices("Accept the offer", "Refuse")

        elif game_state == "jeep_choices":
            choices("Talk to the man", "Go back")
    #HERE
        elif game_state == "jeep_bucket_choices":
            choices("Give him the bucket", "Throw the bucket at his head.")

        elif game_state == "jeep_no_bucket_choices":
            choices("Try to help in another way", "Stare at him.")

        elif game_state == "trivia_game_2":
            current_bg = bg_jeep
            choices("Let's play", "No. GO. AWAY.")
        
        elif game_state == "pet_choices":
            choices("Keep it", "Don't")

        elif game_state == "coin_choices":
            choices("thank him and walk away", "Ask to go with him")

        elif game_state == "buy":
            current_bg = bg_shop
            choices("Ask for both food and a drink", "Ask for one of them only")
        
        elif game_state == "buy_score":
            choices("Agree", "Walk")

        elif game_state == "cactus_eating_choices":
            current_bg = bg_sunset_sitting
            choices("Fine.", "Throw the empty cup at it.")

        elif game_state == "evil_cactus_choices":
            choices("Agree", "Refuse")

        elif game_state == "evil_cactus_choices_no_pet":
            choices("Agree", "Refuse")

        if trivia_active:
            draw_trivia()

        if game_state == "pet_naming":
            draw_naming()

        if showing_trivia_result:
            if current_time - result_timer > 1000:
                cactus = cactus_normal
                showing_trivia_result = False
                game_state = "dialogue"
                dialogue_box_visible = True
                trivia_dialogue = [score_line, cactus_last_line, narrator_last_line]
                current_dialogue = trivia_dialogue
                current_index = 0
                round_score = 0

        if inventory_visible:
            draw_inventory()    

        

        draw_message(f"Score: {total_score}", 20, 630)

        if endings and not naming_active:
            endings_shown = True
            screen.blit(endings_screen, (0,0))
        else:
            endings_shown = False
        #ENDINGS
        if points_poor_visible and endings:
            screen.blit(points_poor_text, (0, 0))
        if refuse_cactus_visible and endings:
            screen.blit(refuse_cactus, (0, 0))
        if collapsed_sand_visible and endings:
            screen.blit(collapsed_sand, (0, 0))
        if collapse_exhaustion_visible and endings:
            screen.blit(collapse_exhaustion, (0, 0))
        if refuse_woman_visible and endings:
            screen.blit(refuse_woman, (0, 0))
        if best_pet_visible and endings: 
            screen.blit(best_pet, (0, 0))
        if best_visible and endings:
            screen.blit(best, (0, 0))
        if mid_pet_visible and endings:
            screen.blit(mid_pet, (0, 0))
        if mid_visible and endings:
            screen.blit(mid, (0, 0))
        if bad_pet_visible and endings:
            screen.blit(bad_pet, (0, 0))
        if bad_visible and endings:
            screen.blit(bad, (0, 0))

        if bad_visible:
            cactus_normal = pygame.image.load("Images/cactus_normal_cap.png").convert_alpha()
            cactus_shocked = pygame.image.load("Images/cactus_shocked_cap.png").convert_alpha()
            cactus_evil = pygame.image.load("Images/cactus_evil_cap.png").convert_alpha()
            cactus_dissappointed = pygame.image.load("Images/cactus_dissappointed_cap.png").convert_alpha()
            cactus_points_won = pygame.image.load("Images/cactus_points_won_cap.png").convert_alpha()
            cactus_points_loss = pygame.image.load("Images/cactus_points_loss_cap.png").convert_alpha()
            cactus_happy = pygame.image.load("Images/cactus_happy_cap.png").convert_alpha()
            cactus_angry = pygame.image.load("Images/cactus_angry_cap.png").convert_alpha()
            bad_ending_no_pet[11] = "—I get to keep all your points! I can buy that other cool cap now!"

        pygame.display.update()
        await asyncio.sleep(0)
        
asyncio.run(main())