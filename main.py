# This is my first test based adventure game
from IPython.display import clear_output
import time

a = 2
b = 0.2
c = 0.08
city = True
forrest = True
choices_city = ["ally", "right", "left", "knife", "gun", "voice", "room", "paper", "building", "street"]
choices_forrest = ["night","day", "foot print", "follow","lake", "fairy"]

name = input("Please type your name: ").upper()
time.sleep(a)
print("")
time.sleep(a)
print("    ********************************************************")
time.sleep(a)
print("    |                                                      |")
time.sleep(a)
print("    |                     Welcome                          |")
time.sleep(a)
print("    |         To The World Of The Unknown",name,"             |")
time.sleep(a)
print("    |      Type 'quit' at anypoint to leave the journey    |")
time.sleep(a)
print("    |                                                      |")
time.sleep(a)
print("    ********************************************************")
time.sleep(a)
print("")
 
time.sleep(a)

answer = input(" Would you like to play in the a mystical forrest or in a dense city.\n Type city or forrest: ")


if answer == "city":
    clear_output()

    while city:
        print(" Welcome to the city of the lost. Here you will discover a deep dark secret and if you are lucky enough you will survive.")
        time.sleep(a)
        print(" As you start walking down the city street you see a piece of paper on the ground, at the same time you notice a flash coming from a dark ally")
        time.sleep(a)
        print(" Time to decide. Do you want to pick up the paper or head down the ally.")
        time.sleep(a)
        answer = input("Type Ally or Type paper: ").lower()
        clear_output()

        if answer == "ally":
            print(" As you head down the dark ally the light you saw quickly gets further and further away and you then notice 2 doors.")
            time.sleep(a) 
            print(" 1 on your right side and 1 on your left side. Which door do you choose?")
            time.sleep(a)
            answer = input("Type Left or Right: ").lower()
            clear_output()

            if answer == "left":
                clear_output()
                print(" You think just because this path isn't as dark it is safer. But you may be in for a suprise.")
                time.sleep(a)
                print(" The door opens and you are faced with the brightest light you have ever seen.")
                time.sleep(a)
                print(" As your eyes try to adjust. You feel these drips of something hitting the top of your head. You wipe your head and look into your hands")
                time.sleep(a)
                print(" You see your hands covered in blood. As you shield your eyes and look up you see the ceiling is covered in spikes.")
                time.sleep(3)
                print(" The spikes plunge from the ceiling and impale you.")
                time.sleep(3)
                print(" YOU HAVE MADE A BAD CHOICE {}, CHOOSING TO BE LEAD BY THE LIGHT. THE LIGHT HAS COST YOU YOUR LIFE.".format(name))
            
                city = False
                time.sleep(a)
                print("GAME OVER")

            elif answer == "right":
                print(" You are headed down a dark path but the reward may be great!!")
                time.sleep(a)
                print(" As the door opens you see a knife and a bow/arrow on the table, you have a feeling you will need one of them but which do you choose.")
                time.sleep(a)
                answer = input("Type Knife or Bow/Arrow to choose your weapon: ").lower()

                if answer == "knife":
                    print(" You pick up the knife and notice it already has dried blood on it. Who's blood is this you wonder. \n")
                    time.sleep(a)
                    print(" You head further into the dark room and you hear very faintly your name being called. {}........{}..... Please come help me".format(name, name))
                    time.sleep(a)
                    answer = input("Type 'voice' to head towards the voice or Type 'room' to keep exploring the room: ").lower()
   
                    if answer == "voice":
                        print(" As you head up the stairs were you believe the voice is coming from all of a sudden the voice stops and the stairs start to shake beanthe yor feet.")
                        time.sleep(a)
                        print(" You start to turn to run back down the stair and all of a sudden the stairs open up and you begin to fall into a even darker hole.")
                        time.sleep(a)
                        print(" You finally land with a hard thud on a dirt floor.")
                        time.sleep(a)
                        print(" You slowly lift your head and with the small sliver of light coming in the room you see a shadow standing above you.")
                        time.sleep(a)
                        print(" The shadow longes towards you and you remember you have the knife you pull it out.")
                        time.sleep(a)
                        print(" As the shadow longes towards you to shove the knife out in front of you.")
                        time.sleep(a)
                        print(" The knife plunges deep into the shadowy figure and at that moment you realize.") 
                        time.sleep(3)
                        print(" You too have been stabbed.")
                        time.sleep(a)
                        print(" You were killed by the shadowy figure. In the end you chose the wrong weapon for this battle.")
                        time.sleep(4)
                        print(" YOU HAVE LOST THE GAME")
                        time.sleep(a)
                        city = False
                    elif answer == "room":
                        print(" You continue to explore the room and you find a key. Hold on to this key. it may prove useful.")
                        time.sleep(a)
                        print(" You see a door with light coming from the bottom. The door is locked and you remember you have a key.")
                        time.sleep(a)
                        print(" You try the key and it opens the door.")
                        time.sleep(a)
                        print(" Once the door opens you find a pot of gold and a note. The note reads: ")
                        time.sleep(3)
                        print(" You have avoid all dangers within my city. This gold is yours. YOU HAVE WON!!!")
                        city = False
                        time.sleep(a)
                        print(" YOU HAVE WON THE GAME {}. ".format(name))

                    else:
                        print("You picked an invalid option. You have lost the game.")
                        city = False

                elif answer == "bow/arrow":
                    print(" Once you pick up the bow and arrow you see a note under the equipment on the table.")
                    time.sleep(a)
                    print(" The note reads: ")
                    time.sleep(a)
                    print(" The weapon you have chosen leads us to believe you may be the hero we have been searching for.")
                    time.sleep(a)
                    print(" You only have 1 arrow. use it wisely. It just might save your life.")
                    print()
                    time.sleep(a)
                    print(" While scanning the room you hear a voice calling your name.")
                    time.sleep(a)
                    print("{}...........{}............{}....".format(name, name, name))
                    time.sleep(a)
                    print(" You head towards the sound and you see a stairwell.")
                    time.sleep(a)
                    print(" Time to decide. Do you want to head up the stairs or stay and explore.")
                    time.sleep(a)
                    answer = input(" Type 'stairs' or Type 'explore' ").lower()

                    if answer == "stairs":
                        time.sleep(a)
                        print(" As you head up the stairs were you believe the voice is coming from all of a sudden the voice stops and the stairs start to shake beanthe yor feet.")
                        time.sleep(a)
                        print(" You start to turn to run back down the stair and all of a sudden the stairs open up and you begin to fall into a even darker hole.")
                        time.sleep(a)
                        print(" You finally land with a hard thud on a dirt floor.")
                        time.sleep(a)
                        print(" You slowly lift your head and with the small sliver of light coming in the room you see a shadow standing above you.")
                        time.sleep(a)
                        print(" The shadow longes towards you.")
                        time.sleep(a)
                        print(" You fire your only arrow hitting the shadowy figure in the heart.")
                        print()
                        time.sleep(a)
                        print(" As the figure slumps to the floor you see a door behind it. You head to the door and open it.")
                        time.sleep(a)
                        print(" There you see a pot of gold and a note that reads: ")
                        time.sleep(a)
                        print(" You have killed the Gaurdian of the gold. This gold is yours.")
                        time.sleep(a)
                        print(" YOU HAVE WON THE GAME {}. ".format(name))
                        city = False
                        break

                    elif answer == "explore":
                        print(" As you continue to explore the room, you start to fell really hot.")
                        time.sleep(a)
                        print(" You start to feel as if you skin is burning.")
                        time.sleep(a)
                        print(" The room a become so hot that you pass out.")
                        time.sleep(a)
                        print(" You have succumb to the heat in the room. ")
                        time.sleep(a)
                        print()
                        print(" You have die.")
                        print(" YOU LOST THE GAME!!")
                        city = False
                        break


        elif answer == "paper":
            print(" You pick up the piece of paper and see that the note is written in blood.")
            time.sleep(a)
            print(" The note reads ' I KNOW WHO YOU ARE {}. DO YOU KNOW WHY YOU ARE IN MY CITY. YOU WILL SOON FIND OUT.".format(name))
            time.sleep(a)
            print(" The note then gives you 2 direction to chose from cross the street and head into the 10 story building or continue down the street.")
            time.sleep(a)
            answer = input(" Type 'building' to head into the building or type 'street' to continue down the street: ")

            if answer == "building":
                print(" Once you enter the building the door slams shut behind.")
                time.sleep(a)
                print(" The room turns red and you hear a robotic voice say: ")
                time.sleep(3)
                print(" YOU HAVE MADE A BAD DECISION. THIS BUILDING WILL BECOME YOUR TOMB")
                time.sleep(a)
                print(" The walls close in on you and you are crushed. ")
                time.sleep(a)
                print(" You have died.")
                time.sleep(a)
                print(" YOU HAVE LOST THE GAME!!!")
                time.sleep(a)
                print()
                time.sleep(a)
                print("GAME OVER....")

                city = False                
                break
                

            elif answer == "street":
                print(" You continue walking down the street and you see a phone booth.")
                time.sleep(a)
                print(" The phone inside the booth is ring.")
                time.sleep(a)
                print(" You answer the phone and your hear on the other end: ")
                time.sleep(3)
                print(" {}.......{}.... You have chosen the correct path.".format(name, name))
                time.sleep(a)
                print("......... Once you hang up this night mare will be over. ")
                time.sleep(a)
                print("...... Hang up the phone!!! ")
                time.sleep(a)
                print(" You hang up and you awake in your home. ")
                time.sleep(a)
                print(" At your feet you see a pot of gold. ")
                time.sleep(3)
                print(" YOU HAVE SURVIVED THE GAME AND RECEIVED YOUR POT OF GOLD. ")
                time.sleep(a)
                print(" YOU HAVE WON THE GAME {}".format(name))
                city  = False                
                break
            

        elif answer == "quit":
            print(" Thank you starting the journey {}, we do hope you come back and try again.".format(name))
            city = False
            break


        elif answer not in choices_city:
            print(" That is not a choice please try again. ")
            continue
            
        

elif answer == "forrest":

    while forrest:
        print(" Welcome {}, to the magical mystical forrest were nothing is as it seems".format(name))
        time.sleep(a)
        print(" How you got to the forrest is unknown and how to leave the forrest is even more of a mystery.\n")
        time.sleep(a)
        print(" Time for your first choice of the game weather it is day or night. Be aware the time of day may or maynot affect the creatures you run into")
        time.sleep(a)
        answer = input(" Type 'Day' or Type 'Night' to choose when you entered the forrest:\n ").lower()
        clear_output()


        if answer == "day":
            print(" As you walk through the thick lush forrest you noticed all the pretty flowers, the lovely smell of a fresh rain.")
            time.sleep(a)
            print(" You also notice what looks to be a weird shaped foot print in the wet dirt.")
            time.sleep(a)
            print(" At the same time you see what you could swear was a fairy fly past you saying you name. {}.... {} follow me!!!!!!".format(name, name))
            time.sleep(a)
            answer = input(" Follow the fairy or examine the foot print. Type fairy or foot print: ")
            clear_output()

            if answer == "fairy":
                print(" You start to follow the fairy and as she flies past the leaves and \n the grass the glitter that follows her starts to turn everything into a brighter color of what it original was.")
                time.sleep(a)
                print(" The colors catch your attention and you notice that her glitter is also revealing a path. You decide to reach out and touch the glitter.")
                time.sleep(a)
                print(" Instantly your fingers begins to burn. You notice a lake to your right and the fairy starts to fly to the left.")
                time.sleep(a)
                print(" Time to decide. Do you head towards the lake to sooth your burning hand and risk losing sight of the fairy or do you continue to follow the fairy and risky what ever may happen to your hand.")
                answer = input(" Type 'Follow' to follow the fairy or Type 'Lake' to head towards the lake: ").lower()

                if answer == "lake":
                 print(" You head towards the lake as fast as you can.")
                 time.sleep(a)
                 print(" You plunge your arm into the glowing water.")
                 time.sleep(a)
                 print(" Instantly your arm stops burning and you see a rope at the bottom of the water")
                 time.sleep(a)
                 print(" You pull at the rope and a hatch opens beneath the dirt behind you. ")
                 time.sleep(a)
                 print(" you walk up to the hatch and see a pot of gold with a note.")
                 time.sleep(a)
                 print(" The note read: ")
                 time.sleep(a)
                 print(" Because you did not let the fairy lead you aware deeper into my forrest you can keep this pot of gold.")
                 time.sleep(a)
                 print(" YOU HAVE WON THE GAME.")
                 forrest = False
                 break

                elif answer == "follow":
                    print(" Your curiosity has cost you dearly.")
                    time.sleep(a)
                    print(" even though your hand/arm is burning you have chosen to follow the fairy.")
                    time.sleep(a)
                    print(" While following her you didn't realize what was following you until it was to late.")
                    time.sleep(a)
                    print(" As you turn around you see the biggest dragon you could ever imagine.")
                    time.sleep(a)
                    print(" The dragon says to you: ")
                    time.sleep(3)
                    print(".... How dare you follow my fairy into my forrest. You have come to far stranger.")
                    time.sleep(a)
                    print(" The dragon then leans in and swallows you in one bite.")
                    time.sleep(a)
                    print(" Due to your curiosity and disregard for your own injury.")
                    time.sleep(3)
                    print(" You Have Died!!! ")
                    print(" YOU HAVE LOST THE GAME!!")
                    print(" GAME OVER")

                    forrest = False
                    break
        
            if answer == "foot print":
                print(" While looking at the footprint you fail to notice Goblin that snuck up behind you. ")
                time.sleep(a)
                print(" As you turn around he impales you with the horn protruding from his chest.")
                time.sleep(a)
                print(" You have Died.")
                time.sleep(a)
                print(" YOU HAVE LOST THE GAME.")
                time.sleep(a)
                print(" GAME OVER!!!")

                forrest = False
                break

        if answer == "night":
            print(" Why would anyone want to be in a spooky forrest at night. ")
            time.sleep(a)
            print(" The first creature you see is a huge dragon.")
            time.sleep(a)
            print(" The dragon blow fire on you.")
            time.sleep(a)
            print(" YOU HAVE DIED.")
            time.sleep(a)
            print(" YOU HAVE LOST THE GAME!!!")
            print(" GAME OVER!!!")
            
            forrest = False
            break

        
        if answer == "quit":
            print(" Thank you starting the journey {}, we do hope you come back and try again.".format(name))
            forrest = False
            break


        elif answer not in choices_forrest:
            print(" That is not a choice. You Lose The Game ")
            forrest = False
            continue

elif answer == "quit":
    print(" Thank you starting the journey {}, we do hope you come back and try again.".format(name))
    city = False
    forrest = False
    
    




        

