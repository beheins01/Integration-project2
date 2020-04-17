'#Integration Project'
'#Create Your Own Adventure'
'#Ben Heins'
'#Computer Science'
'#This is a story telling program where your choices have consiquences!'
'#The story changes depending on the choices you make.'
'#so be careful becuase one wrong choice may be your last...'

print("Welcome to the story!")
print("Today you will be participating in my Integration Project!")
print("You win if you become the hero of a town/village!")
print("This project is a create your own adventure.I Hope You Enjoy!")
print("AND REMEMBER YOUR CHOICES HAVE CONSIQUENCES!")

answer = input("Would you like to play? (yes/no) ")

if answer.lower().strip() == "yes":
    '#"answer" - checks the answer'
    '#"lower" - makes sure the answer is in all lower case'
    '#"strip" - gets rid of any white space or spaces (From W3Schools)'

    import time
    time.sleep(1.5)
    '#The last two lines of code'
    '#delay the next line for 3 seconds  (From W3Schools)'

    print("Calibration is underway.")
    print("Please help by putting in your real life age.")
    print("This is completely confidential")

    age = input()
    print("Your age is " + age)

    print("Now I just need to make sure I can do some easy math.")
    print("(Give me some numbers so I can do a math problem that involes,")
    print("(+,-,*,//))")
    print("For example ( (((12+2)*4)//6)-4) ) NO MORE THAN 5 NUMBERS!")

    a1 = input("Value a: ")
    b1 = input("Value b: ")
    c1 = input("Value c: ")
    d1 = input("Value d: ")
    e1 = input("Value e: ")

    a = int(a1)
    b = int(b1)
    c = int(c1)
    d = int(d1)
    e = int(e1)

    outcome = a+b*c//d-e
    print("Outcome = ", outcome)

    name = input("Please enter your name: ")
    x = 0
    while (x < 20):
        print(name)
        x = x + 2

    print("Now I am gonna need 3 numbers from you.")

    def smallnumber(num1, num2):
        if num1 < num2:
            smallest = num1
        else:
            smallest = num2
        return smallest

    def main():
        choice1 = int(input("Please enter a number: "))
        choice2 = int(input("Please enter another number: "))

        smallerNumber = int(input("Enter a number: "))
        print("One of the numbers is", smallerNumber)

    main()

    my_list = [1, 2, 3, 4]

    def append_list(my_list):
        my_list.append(12)

    append_list(my_list)
    print(my_list)

print("Great! Now its time to start your adventure!")
print("Welcome Hunter! Now I need to know a bit about you.")

answer = input("Are you a Boy or a Girl? (boy/girl)")

if answer.lower().strip() == "boy":
    answer = input("What is your age? (has to be above 18!!)")

    if int(answer) < 18:
        print("Sorry, go back to your parents you are not ready.")
        print("Try again when you are older.")

    elif int(answer) >= 18 and int(answer) <= 23:
        print("You are a new hunter!")

        answer = input("Do you want to continue? (yes/no)")

        if answer.lower().strip() == "no":
            print("GAME OVER!")

        elif answer.lower().strip() == "yes":

            print("Great! Welcome to Camp Prust!")
            print("I hope you can make yourself comfortable here.")

            import time
            time.sleep(1.5)

            print("We need food and supplies can you do one?")

            answer = input("Where would you rather go? (woods/settlement)")

            if answer.lower().strip() == "woods":
                print("Great! You are going to help us get some food!")
                print("The people from Camp Prust love meats and berries,")
                print("beware though Ogres wander in the woods at night.")
                print("While hunting,")
                print("one of your fellow hunters get severely hurt,")
                print("you only have 1 hour before it becomes dark.")
                print("There is just enough time,")
                print("to get out of the woods.")
                print("Sadly if you want to save the hunter,")
                print("you must stay during the night")

                answer = input("What do you do? (leave him/help him)")

                if answer.lower().strip() == "leave him":
                    print("You decided to leave the fellow hunter.")
                    print("As you leave you hear the hunters scream,")
                    print("it pierces your ears and the guilt sets in.")
                    print("You bring the food back to Prust.")
                    print("Some of the people realize the missing person.")
                    print("You see the family of the hunter in the distance.")
                    print("They comfront you and ask what happened.")
                    print("How do you tell them he died?")

                    answer = input("(left him/with honor)")

                    if answer.lower().strip() == "left him":
                        print("HOW COULD YOU!")
                        print("He trusted you with his life,")
                        print("and you betrayed him.")
                        print("The people of Prust seem to be angry.")
                        print("Leave Prust,")
                        print("and never return you traitor,")
                        print("you hear in the crowd.")
                        print("We will kill you if you stay here,")
                        print("you hear,")
                        print("from another member of the crowd")
                        print("Adventurer,")
                        print("I fear you are in danger here,")
                        print("and you have to leave.")
                        print("As you leave Prust,")
                        print("you keep the food you gathered.")
                        print("10 days later")
                        print("You find yourself in the desert,")
                        print("you realize you need food and water.")
                        print("There is no oasis near by,")
                        print("and you start to realize,")
                        print("this could be your last couple days,")
                        print("but you must move forward.")
                        print("4 days later")
                        print("You are officially out of food and water,")
                        print("You start to hallucinate and see things.")
                        print("In the distance you see a cactus,")
                        print("and a lizard.")
                        print("The cactus has water in it which can help,")
                        print("the lizard would be good food.")

                        answer = input("Which do you choose? (lizard/cactus)")

                        if answer.lower().strip() == "lizard":
                            print("You walk over to the lizard,")
                            print("and kill it.")
                            print("You make a fire and start to cook it.")
                            print("As you cook it,")
                            print("you go over to the cactus,")
                            print("when you get to the cactus,")
                            print("you cut it open,")
                            print("and drink the water.")
                            print("You then set up camp,")
                            print("and sleep so that you can continue on.")
                            print("The next day you see a town in the desert.")
                            print("You have no clue who is in the town.")
                            print("Should you enter the town?")

                            answer = input("(yes/no)")

                            if answer.lower().strip() == "yes":
                                print("You enter the town,")
                                print("and the people")
                                print("of the town are welcoming.")
                                print("They offer you food,")
                                print("water, and shelter.")
                                print("They only ask you help,")
                                print("take out a druid.")
                                print("that has been terrorizing their town.")
                                print("The druid is a millenia old,")
                                print("and very wise.")
                                print("Will you help the town?")

                                answer = input("(yes/no)")

                                if answer.lower().strip() == "yes":
                                    print("Thank you hunter!")
                                    print("The druids only known location is,")
                                    print("up on mount mordoth.")
                                    print("You will need to be careful.")
                                    print("The wilderness is dangerous.")
                                    print("We can give you some supplies,")
                                    print("Your treck starts today,")
                                    print("The village offers you two things.")
                                    print("You can only take one.")
                                    print("They offer you a horse for travel,")
                                    print("or the sword of desolation")
                                    print("that glows when danger lurks.")
                                    print("Which will you take?")

                                    answer = input("(horse/sword)")

                                    if answer.lower().strip() == "horse":
                                        print("You took the horse,")
                                        print("to the top of mount mordoth,")
                                        print("and went into the tower.")
                                        print("You entered his keep,")
                                        print("to find nothing.")
                                        print("As you search for him,")
                                        print("you hear something")
                                        print("coming from the next room.")
                                        print("You enter the room,")
                                        print("and find an open spell book,")
                                        print("and you go to investigate it.")
                                        print("There is a blast of light,")
                                        print("the was druid was behind you.")
                                        print("You find yourself in a cage.")
                                        print("You have no way to escape")
                                        print("the cage,")
                                        print("because it is locked by magic.")
                                        print("You were stuck there,")
                                        print("for the rest of your days.")
                                        print("GAME OVER! You lose!")

                                        '###########END OF PATH###########'

                                    elif answer.lower().strip() == "sword":
                                        print("Great choice!")
                                        print("You start your adventure.")
                                        print("After about one week,")
                                        print("of trecking up the mountain,")
                                        print("you finally arrive.")
                                        print("You enter the druids tower,")
                                        print("to stop his reign.")
                                        print("You search,")
                                        print("and find a spell book.")
                                        print("Then,")
                                        print("You see your sword glow.")
                                        print("Will you search,")
                                        print("or go to the spell book?")

                                        answer = input("(book/search)")

                                        if answer.lower().strip() == "book":
                                            print("You walk toward the book,")
                                            print("and ignore your sword.")
                                            print("Then,")
                                            print("there is a blast of light,")
                                            print("because he was behind you.")
                                            print("You then,")
                                            print("find yourself in a cage.")
                                            print("You have no way to escape,")
                                            print("because magic locked it.")
                                            print("You were stuck there,")
                                            print("for the rest of your days.")
                                            print("GAME OVER! You lose!")

                                            '###########END OF PATH###########'

                                        elif answer.lower().strip() == "search":
                                            print("You search the room,")
                                            print("and realize,")
                                            print("something is behind you.")
                                            print("You turn around,")
                                            print("and see the druid")
                                            print("casting a spell.")
                                            print("You tackle him,")
                                            print("which starts a fight")
                                            print("You two are sharing blows,")
                                            print("back and forth,")
                                            print("until you have him,")
                                            print("beat on the ground.")
                                            print("You have your sword")
                                            print("pointing to him,")
                                            print("and he asks for mercy.")
                                            print("Will you take him hostage,")
                                            print("or strike him down?")

                                            answer = input("(kill/hostage)")

                                            if answer.lower().strip() == "hostage":
                                                print("You bring him back")
                                                print("to the town,")
                                                print("and there is cheering,")
                                                print("you have defeated him.")
                                                print("You take him")
                                                print("to his cell.")
                                                print("You are gifted gold,")
                                                print("for your trouble.")
                                                print("Your their hero,")
                                                print("and your a legend,")
                                                print("whom will never die.")
                                                print("CONGRATS!")
                                                print("You became a hero!")
                                                print("That is the end!")

                                                '#######END OF STORY!#######'

                                            elif answer.lower.strip() == "kill":
                                                print("You attempt to")
                                                print("strike him down,")
                                                print("but he has ward on.")
                                                print("This protects him,")
                                                print("from death.")
                                                print("It kills the person")
                                                print("trying to kill him.")
                                                print("GAME OVER! You lose!")

                                                '########END OF PATH#######'

                                    elif answer.lower().strip() == "no":
                                        print("You continue on your journey.")
                                        print("A couple days later")
                                        print("you realize,")
                                        print("that you still need food.")
                                        print("You continue,")
                                        print("and find a dead animal,")
                                        print("on the ground.")
                                        print("Due to the lack of food,")
                                        print("you go and take the animal.")
                                        print("As you eat the animal,")
                                        print("there is a coyote")
                                        print("that wants the food.")
                                        print("It sneaks up behind you,")
                                        print("and attacks,")
                                        print("and you were not ready.")
                                        print("The coyote kills you.")
                                        print("GAME OVER! YOU DIED!")

                                        '###### END OF PATH ######'

                                elif answer.lower().strip() == "cactus":
                                    print("You go to the cactus,")
                                    print("and cut it open,")
                                    print("and drink the water.")
                                    print("After you drink the water,")
                                    print("you look for the lizard.")
                                    print("The lizard is gone,")
                                    print("and now you have no food.")
                                    print("A long time later")
                                    print("30 days ago starvation set in,")
                                    print("You have yet to find any food.")
                                    print("4 days later")
                                    print("GAME OVER! YOU DIED! :(")

                                    '###### END OF PATH #####'

                        elif answer.lower().strip() == "help him":
                            print("Thank you adventurer!")
                            print("We have to be quiet in order to escape,")
                            print("if we are not the Ogres,")
                            print("will find us and eat us.")
                            print("The only way out is,")
                            print("the way we came so we must hurry.")
                            print("You take the hunter,")
                            print("and help him through the woods,")
                            print("You start to get close to the exit,")
                            print("you put him on his horse,")
                            print("and he rides off to Prust.")
                            print("Thats when you hear,")
                            print("something behind you,")
                            print("then everything goes black.")
                            print("You awaken at a Ogre village.")
                            print("There is a fire in front of you,")
                            print("and you are tied to a log.")
                            print("You have none of your weapons,")
                            print("and you start to look around,")
                            print("for something to get yourself free.")
                            print("You see a knife near your feet,")
                            print("and the fire is behind you.")
                            print("How will you escape?")

                            answer = input("(cut out/ burn the rope)")

                            if answer.lower().strip() == "cut out":
                                print("You reach for the knife and grab it.")
                                print("You had no clue but it was a trap,")
                                print("The Ogres wanted you")
                                print("to grab the knife.")
                                print("They now decide t")
                                print("o put you over the fire.")
                                print("You now have no way out,")
                                print("and end up burning alive.")
                                print("GAME OVER! YOU DIED! :(")

                                '###### END OF PATH #####'

                            elif answer.lower().strip() == "burn the rope":
                                print("You start to wiggle towards the fire.")
                                print("The Ogres have no idea,")
                                print("what you doing.")
                                print("You get close to the fire,")
                                print("and the rope starts to burn.")
                                print("In order to burn the rope,")
                                print("you must burn your hands.")
                                print("You take the sacrafice,")
                                print("and burn your hands.")
                                print("After a bit you are free,")
                                print("and sneak away.")
                                print("You make your way out of the woods,")
                                print("then you have to start wrapping")
                                print("your hands in cloth")
                                print("in order to protect them")
                                print("from futher harm.")
                                print("You escaped,")
                                print("but lost your share of food,")
                                print("because of the Ogres.")
                                print("Your hourse is gone,")
                                print("and you must walk back to Prust.")
                                print("6 days later")
                                print("You arrived in Prust,")
                                print("and you are greeted with open arms.")
                                print("You see the hunter you saved,")
                                print("and he asks")
                                print("what happened to your hands.")
                                print("You explain it to crowd,")
                                print("and that you lost the food.")
                                print("They said that they are not worried")
                                print("about the food,")
                                print("They are more worried")
                                print("about your hands and healing them.")
                                print("They say that there is a healer,")
                                print("who can help,")
                                print("or you can heal your hand.")
                                print("What do you want to do?")

                                answer = input("(healer/by yourself)")

                                if answer.lower().strip() == "healer":
                                    print("Welcome adventurer...")

                                    import time
                                    time.sleep(1.5)

                                    print("You see a hooded figure.")
                                    print("I see your hand is severly burned.")
                                    print("I have two choices for you...")
                                    print("The first one is")
                                    print("the double-edged potion.")
                                    print("The second is an herb,")
                                    print("that takes a while to work.")
                                    print("Which one do you want?")

                                    answer = input("(herb/potion)")

                                    if answer.lower().strip() == "herb":
                                        print("You take take the herb,")
                                        print("and you heal,")
                                        print("but it takes weeks to heal.")
                                        print("The town has one last request.")
                                        print("There is a monster")
                                        print("that is outside our walls.")
                                        print("This monster")
                                        print("keeps us from leaving,")
                                        print("and holds us hostage.")
                                        print("Can you help us?")

                                        answer = input("(yes/no)")

                                        if answer.lower().strip() == "yes":
                                            print("The monster")
                                            print("is known as the Fargwa,")
                                            print("says the towns people.")
                                            print("This monster")
                                            print("may not be that big,")
                                            print("but it is dangerous.")
                                            print("You leave in order to")
                                            print("find the Fargwa,")
                                            print("and find dead soldiers.")
                                            print("You investigate them.")
                                            print("Then you hear the roar")
                                            print("of the Fargwa")
                                            print("You must kill it.")
                                            print("You attack and attack,")
                                            print("but it does nothing.")
                                            print("Then,")
                                            print("you decide to lead it,")
                                            print("towards the rapids.")
                                            print("You jump on a rock")
                                            print("in the rapids,")
                                            print("and the Fargwa follows.")
                                            print("It hits a rock that moved,")
                                            print("and it slipped")
                                            print("into the rapids,")
                                            print("and it was gone forever.")
                                            print("You make your way back")
                                            print("to the village.")
                                            print("When you get back,")
                                            print("you are greated")
                                            print("like a hero.")
                                            print("CONGRATS!")
                                            print("You completed the story,")
                                            print("and became a hero!")
                                            print("This is the end!")

                                        elif answer.lower().strip() == "no":
                                            print("Well I guess we aren't")
                                            print("that important to you.")
                                            print("Go about your life.")
                                            print("We will have to live")
                                            print("in fear now.")
                                            print("GAME OVER!")

                                            '####End of Path####'

                                    elif answer.lower().strip() == "potion":
                                        print("This potion healed you,")
                                        print("but made you lose your memory,")
                                        print("of why you were there.")
                                        print("You go on with your life,")
                                        print("without any recolection")
                                        print("of who you are.")
                                        print("GAME OVER!")

                                        '#####End of Path#####'

                                elif answer.lower().strip() == "by yourself":

                                    print("You know some healing.")
                                    print("The most basic potion")
                                    print("I know is the green potion.")
                                    print("This potion heals you,")
                                    print("but takes a day to work.")
                                    print("Or,")
                                    print("I could let myself heal over time.")
                                    print("How should I heal myself?")

                                    answer = input("(over time/green potion)")

                                    if answer.lower().strip() == "over time":
                                        print("The burn heals over time.")
                                        print("THe issue is that you lost")
                                        print("the function of that hand.")
                                        print("This forces you stop")
                                        print("your adventuring,")
                                        print("and quit being a hunter.")
                                        print("GAME OVER!")

                                        '#####End of Path#####'

                                    elif answer.lower().strip() == "green potion":
                                        print("You heal after a couple days.")
                                        print("The people")
                                        print("of the village thank you,")
                                        print("for your help with the food.")
                                        print("You are given gold,")
                                        print("and a large house")
                                        print("in the village.")
                                        print("The people hold a celebration,")
                                        print("and you are granted")
                                        print("the rank HERO!")
                                        print("CONGRATS! YOU WON!")
                                        print("That is the end!")

                                        '#####End of Story#####'

                    elif answer.lower().strip() == "settlement":
                        print("Cool!")
                        print("You are going to get our supplies!")
                        print("You need to make your way to Numenthorn.")
                        print("There you will find supplies")
                        print("that were stolen from us.")
                        print("The commoners there can be hostile,")
                        print("so bring your weapons.")
                        print("You reach your Numenthorn,")
                        print("and it is quiet.")
                        print("It looks like everyone left,")
                        print("and in hurry.")
                        print("You hear a roar,")
                        print("and look behind you,")
                        print("and realize what scared them.")

                        import time
                        time.sleep(1)

                        print("A giant Basilisk is staring right at you.")
                        print("HURRY YOU MUST CHOOSE WHAT TO DO!")

                        answer = input("What do you do? (attack/hide)")

                        if answer.lower().strip() == "attack":
                            print("You fight the Basilisk,")
                            print("and end up getting scraped")
                            print("by one of its fangs.")
                            print("This poisons you,")
                            print("but you must finish what you started.")
                            print("You continue to fight,")
                            print("and end up being in a fight")
                            print("that takes hours and hours.")
                            print("You eventually end up")
                            print("on top of a building,")
                            print("and you jump off,")
                            print("and stab the basalisk.")
                            print("The snake falls motionless")
                            print("to the ground.")
                            print("You collect the supplies,")
                            print("and return to the village.")
                            print("You live rest of you years,")
                            print("and grow old,")
                            print("and you remembered as a hero.")
                            print("CONGRATS! YOU WON!")
                            print("This is the end!")

                        elif answer.lower().strip() == "hide":
                            print("You hide from the snake.")
                            print("But Basalisks have a great")
                            print("sense of smell,")
                            print("and it finds you.")
                            print("It bites you")
                            print("which ends up killing you.")
                            print("GAME OVER!")

                            '#####End of Path#####'

        elif int(answer) > 23 and int(answer) <= 50:
            print("Welcome experienced Hunter!")

            answer = input("Do you want to continue? (yes/no)")

            if answer.lower().strip() == "no":
                print("GAME OVER!")

            elif answer.lower().strip() == "yes":

                print("Great! Welcome to Camp Prust!")
                print("I hope you can make yourself comfortable here.")

                import time
                time.sleep(1.5)

                print("We need food and supplies can you do one?")

                answer = input("Where would you rather go? (woods/settlement)")

                if answer.lower().strip() == "woods":
                    print("Great! You are going to help us get some food!")
                    print("The people from Camp Prust love meats and berries,")
                    print("beware though Ogres wander in the woods at night.")
                    print("While hunting,")
                    print("one of your fellow hunters get severely hurt,")
                    print("you only have 1 hour before it becomes dark.")
                    print("There is just enough time,")
                    print("to get out of the woods.")
                    print("Sadly if you want to save the hunter,")
                    print("you must stay during the night")

                    answer = input("What do you do? (leave him/help him)")

                    if answer.lower().strip() == "leave him":
                        print("You decided to leave the fellow hunter.")
                        print("As you leave you hear the hunters scream,")
                        print("it pierces your ears and the guilt sets in.")
                        print("You bring the food back to Prust.")
                        print("Some of the people realize the missing person.")
                        print("You see the family,")
                        print("of the hunter in the distance.")
                        print("They comfront you,")
                        print("and ask what happened.")
                        print("How do you tell them he died?")

                        answer = input("(left him/with honor)")

                        if answer.lower().strip() == "left him":
                            print("HOW COULD YOU!")
                            print("He trusted you with his life,")
                            print("and you betrayed him.")
                            print("The people of Prust seem to be angry.")
                            print("Leave Prust,")
                            print("and never return you traitor,")
                            print("you hear in the crowd.")
                            print("We will kill you if you stay here,")
                            print("you hear,")
                            print("from another member of the crowd")
                            print("Adventurer,")
                            print("I fear you are in danger here,")
                            print("and you have to leave.")
                            print("As you leave Prust,")
                            print("you keep the food you gathered.")
                            print("10 days later")
                            print("You find yourself in the desert,")
                            print("you realize you need food and water.")
                            print("There is no oasis near by,")
                            print("and you start to realize,")
                            print("this could be your last couple days,")
                            print("but you must move forward.")
                            print("4 days later")
                            print("You are officially out of food and water,")
                            print("You start to hallucinate and see things.")
                            print("In the distance you see a cactus,")
                            print("and a lizard.")
                            print("The cactus has water in it which can help,")
                            print("the lizard would be good food.")
                            print("Which do you choose?")

                            answer = input("(lizard/cactus)")

                            if answer.lower().strip() == "lizard":
                                print("You walk over to the lizard,")
                                print("and kill it.")
                                print("You make a fire and start to cook it.")
                                print("As you cook it,")
                                print("you go over to the cactus,")
                                print("when you get to the cactus,")
                                print("you cut it open,")
                                print("and drink the water.")
                                print("You then set up camp,")
                                print("and sleep so that you can continue on.")
                                print("The next day,")
                                print("you see a town in the desert.")
                                print("You have no clue who is in the town.")
                                print("Should you enter the town?")

                                answer = input("(yes/no)")

                                if answer.lower().strip() == "yes":
                                    print("You enter the town,")
                                    print("and the people")
                                    print("of the town are welcoming.")
                                    print("They offer you food,")
                                    print("water, and shelter.")
                                    print("They only ask you help,")
                                    print("take out a druid.")
                                    print("that has been terrorizing town.")
                                    print("The druid is a millenia old,")
                                    print("and very wise.")
                                    print("Will you help the town?")

                                    answer = input("(yes/no)")

                                    if answer.lower().strip() == "yes":
                                        print("Thank you hunter!")
                                        print("The druids only")
                                        print("known location is,")
                                        print("up on mount mordoth.")
                                        print("You will need to be careful.")
                                        print("The wilderness is dangerous.")
                                        print("We can give you some supplies,")
                                        print("Your treck starts today,")
                                        print("The village offers")
                                        print("you two things.")
                                        print("You can only take one.")
                                        print("They offer you a horse,")
                                        print("or the sword of desolation")
                                        print("that glows when danger lurks.")
                                        print("Which will you take?")

                                        answer = input("(horse/sword)")

                                        if answer.lower().strip() == "horse":
                                            print("You took the horse,")
                                            print("to mount mordoth,")
                                            print("and went into the tower.")
                                            print("You entered his keep,")
                                            print("to find nothing.")
                                            print("As you search for him,")
                                            print("you hear something")
                                            print("coming from the next room.")
                                            print("You enter the room,")
                                            print("and find a spell book,")
                                            print("and you investigate it.")
                                            print("There is a blast of light,")
                                            print("he was behind you.")
                                            print("You find yourself")
                                            print("in a cage.")
                                            print("You have no way to escape")
                                            print("the cage,")
                                            print("because it is locked,")
                                            print("by magic.")
                                            print("You were stuck there,")
                                            print("for the rest of your days.")
                                            print("GAME OVER! You lose!")

                                            '###########END OF PATH###########'

                                        elif answer.lower().strip() == "sword":
                                            print("Great choice!")
                                            print("You start your adventure.")
                                            print("After about one week,")
                                            print("of climbing,")
                                            print("you finally arrive.")
                                            print("You enter the tower,")
                                            print("to stop his reign.")
                                            print("You search,")
                                            print("and find a spell book.")
                                            print("Then,")
                                            print("You see your sword glow.")
                                            print("Will you search,")
                                            print("or go to the spell book?")

                                            answer = input("(book/search)")

                                            if answer.lower().strip() == "book":
                                                print("You walk to the book,")
                                                print("and ignore your sword.")
                                                print("Then,")
                                                print("there is a blast")
                                                print("of light,")
                                                print("You are then,")
                                                print("in a cage.")
                                                print("You have no escape,")
                                                print("because he locked it.")
                                                print("You were stuck there,")
                                                print("FOREVER.")
                                                print("GAME OVER! You lose!")

                                                '#####END OF PATH#####'

                                            elif answer.lower().strip() == "search":
                                                print("You search the room,")
                                                print("and realize,")
                                                print("he is behind you.")
                                                print("You turn around,")
                                                print("and see the druid")
                                                print("casting a spell.")
                                                print("You tackle him,")
                                                print("which starts a fight")
                                                print("You two are fighting,")
                                                print("back and forth,")
                                                print("until you have him,")
                                                print("beat on the ground.")
                                                print("You have your sword")
                                                print("pointing to him,")
                                                print("and he asks for mercy.")
                                                print("Will you take him,")
                                                print("or strike him down?")

                                                answer = input("(kill/hostage)")

                                                if answer.lower().strip() == "hostage":
                                                    print("You bring him back")
                                                    print("to the town,")
                                                    print("you hear cheering,")
                                                    print("you defeated him.")
                                                    print("You take him")
                                                    print("to his cell.")
                                                    print("You are gifted")
                                                    print("for your trouble.")
                                                    print("Your their hero,")
                                                    print("and your a legend.")
                                                    print("CONGRATS!")
                                                    print("You became a hero!")
                                                    print("That is the end!")

                                                    '###END OF STORY!###'

                                                elif answer.lower.strip() == "kill":
                                                    print("You attempt to")
                                                    print("strike him down,")
                                                    print("but he has ward.")
                                                    print("This protects him,")
                                                    print("from death.")
                                                    print("It kills who is")
                                                    print("trying to kill.")
                                                    print("GAME OVER!")
                                                    print("You lose!")

                                                    '####END OF PATH####'

                                        elif answer.lower().strip() == "no":
                                            print("You continue")
                                            print("on your journey.")
                                            print("A couple days later")
                                            print("you realize,")
                                            print("that you still need food.")
                                            print("You continue,")
                                            print("and find a dead animal,")
                                            print("on the ground.")
                                            print("Due to the lack of food,")
                                            print("you go,")
                                            print("and take the animal.")
                                            print("As you eat the animal,")
                                            print("there is a coyote")
                                            print("that wants the food.")
                                            print("It sneaks up behind you,")
                                            print("and attacks,")
                                            print("and you were not ready.")
                                            print("The coyote kills you.")
                                            print("GAME OVER! YOU DIED!")

                                            '###### END OF PATH ######'

                                    elif answer.lower().strip() == "cactus":
                                        print("You go to the cactus,")
                                        print("and cut it open,")
                                        print("and drink the water.")
                                        print("After you drink the water,")
                                        print("you look for the lizard.")
                                        print("The lizard is gone,")
                                        print("and now you have no food.")
                                        print("A long time later")
                                        print("30 days ago starvation set in,")
                                        print("You have yet to find any food.")
                                        print("4 days later")
                                        print("GAME OVER! YOU DIED! :(")

                                        '###### END OF PATH #####'

                            elif answer.lower().strip() == "help him":
                                print("Thank you adventurer!")
                                print("We have to be quiet,")
                                print("in order to escape,")
                                print("if we are not the Ogres,")
                                print("will find us and eat us.")
                                print("The only way out is,")
                                print("the way we came so we must hurry.")
                                print("You take the hunter,")
                                print("and help him through the woods,")
                                print("You start to get close to the exit,")
                                print("you put him on his horse,")
                                print("and he rides off to Prust.")
                                print("Thats when you hear,")
                                print("something behind you,")
                                print("then everything goes black.")
                                print("You awaken at a Ogre village.")
                                print("There is a fire in front of you,")
                                print("and you are tied to a log.")
                                print("You have none of your weapons,")
                                print("and you start to look around,")
                                print("for something to get yourself free.")
                                print("You see a knife near your feet,")
                                print("and the fire is behind you.")
                                print("How will you escape?")

                                answer = input("(cut out/ burn the rope)")

                                if answer.lower().strip() == "cut out":
                                    print("You reach for the knife<")
                                    print("and grab it.")
                                    print("You had no clue but it was a trap,")
                                    print("The Ogres wanted you")
                                    print("to grab the knife.")
                                    print("They now decide t")
                                    print("o put you over the fire.")
                                    print("You now have no way out,")
                                    print("and end up burning alive.")
                                    print("GAME OVER! YOU DIED! :(")

                                    '###### END OF PATH #####'

                                elif answer.lower().strip() == "burn the rope":
                                    print("You start to")
                                    print("wiggle towards the fire.")
                                    print("The Ogres have no idea,")
                                    print("what you doing.")
                                    print("You get close to the fire,")
                                    print("and the rope starts to burn.")
                                    print("In order to burn the rope,")
                                    print("you must burn your hands.")
                                    print("You take the sacrafice,")
                                    print("and burn your hands.")
                                    print("After a bit you are free,")
                                    print("and sneak away.")
                                    print("You out of the woods,")
                                    print("then you have to start wrapping")
                                    print("your hands in cloth")
                                    print("in order to protect them")
                                    print("from futher harm.")
                                    print("You escaped,")
                                    print("but lost your share of food,")
                                    print("because of the Ogres.")
                                    print("Your hourse is gone,")
                                    print("and you must walk back to Prust.")
                                    print("6 days later")
                                    print("You arrived in Prust,")
                                    print("and you are greeted.")
                                    print("You see the hunter you saved,")
                                    print("and he asks")
                                    print("what happened to your hands.")
                                    print("You explain it to crowd,")
                                    print("and that you lost the food.")
                                    print("They said,")
                                    print("that they are not worried")
                                    print("about the food,")
                                    print("They are more worried")
                                    print("about your hands and healing them.")
                                    print("They say that there is a healer,")
                                    print("who can help,")
                                    print("or you can heal your hand.")
                                    print("What do you want to do?")

                                    answer = input("(healer/by yourself)")

                                    if answer.lower().strip() == "healer":
                                        print("Welcome adventurer...")

                                        import time
                                        time.sleep(1.5)

                                        print("You see a hooded figure.")
                                        print("I see your hand is burned.")
                                        print("I have two choices for you...")
                                        print("The first one is")
                                        print("the double-edged potion.")
                                        print("The second is an herb,")
                                        print("that takes a while to work.")
                                        print("Which one do you want?")

                                        answer = input("(herb/potion)")

                                        if answer.lower().strip() == "herb":
                                            print("You take take the herb,")
                                            print("and you heal,")
                                            print("but it takes weeks.")
                                            print("The town has one request.")
                                            print("There is a monster")
                                            print("that is outside our walls.")
                                            print("This monster")
                                            print("keeps us from leaving,")
                                            print("and holds us hostage.")
                                            print("Can you help us?")

                                            answer = input("(yes/no)")

                                            if answer.lower().strip() == "yes":
                                                print("The monster")
                                                print("is the Fargwa,")
                                                print("says the towns people.")
                                                print("This monster")
                                                print("may not be that big,")
                                                print("but it is dangerous.")
                                                print("You leave in order to")
                                                print("find the Fargwa,")
                                                print("and find skeletons.")
                                                print("You investigate them.")
                                                print("Then you hear the roar")
                                                print("of the Fargwa")
                                                print("You must kill it.")
                                                print("You attack and attack,")
                                                print("but it does nothing.")
                                                print("Then,")
                                                print("you decide to lead it,")
                                                print("towards the rapids.")
                                                print("You jump on a rock")
                                                print("in the rapids,")
                                                print("and it follows.")
                                                print("It hits a rock,")
                                                print("and it slipped")
                                                print("into the rapids,")
                                                print("and it was gone.")
                                                print("You make your way back")
                                                print("to the village.")
                                                print("When you get back,")
                                                print("you are greated")
                                                print("like a hero.")
                                                print("CONGRATS!")
                                                print("and became a hero!")
                                                print("This is the end!")

                                            elif answer.lower().strip() == "no":
                                                print("Well I guess we aren't")
                                                print("that important to you.")
                                                print("Go about your life.")
                                                print("We will have to live")
                                                print("in fear now.")
                                                print("GAME OVER!")

                                                '####End of Path####'

                                    elif answer.lower().strip() == "potion":
                                        print("This potion healed you,")
                                        print("but made you lose your memory,")
                                        print("of why you were there.")
                                        print("You go on with your life,")
                                        print("without any recolection")
                                        print("of who you are.")
                                        print("GAME OVER!")

                                        '#####End of Path#####'

                                    elif answer.lower().strip() == "by yourself":

                                        print("You know some healing.")
                                        print("The most basic potion")
                                        print("I know is the green potion.")
                                        print("This potion heals you,")
                                        print("but takes a day to work.")
                                        print("Or,")
                                        print("I could heal over time.")
                                        print("How should I heal myself?")

                                        answer = input("(over time/green potion)")

                                        if answer.lower().strip() == "over time":
                                            print("The burn heals over time.")
                                            print("THe issue is that you lost")
                                            print("the function of that hand.")
                                            print("This forces you stop")
                                            print("your adventuring,")
                                            print("and quit being a hunter.")
                                            print("GAME OVER!")

                                            '#####End of Path#####'

                                        elif answer.lower().strip() == "green potion":
                                            print("You heal after a couple days.")
                                            print("The people")
                                            print("of the village thank you,")
                                            print("for your help with the food.")
                                            print("You are given gold,")
                                            print("and a large house")
                                            print("in the village.")
                                            print("The people hold a celebration,")
                                            print("and you are granted")
                                            print("the rank HERO!")
                                            print("CONGRATS! YOU WON!")
                                            print("That is the end!")

                                            '#####End of Story#####'

                        elif answer.lower().strip() == "settlement":
                            print("Cool!")
                            print("You are going to get our supplies!")
                            print("You need to make your way to Numenthorn.")
                            print("There you will find supplies")
                            print("that were stolen from us.")
                            print("The commoners there can be hostile,")
                            print("so bring your weapons.")
                            print("You reach your Numenthorn,")
                            print("and it is quiet.")
                            print("It looks like everyone left,")
                            print("and in hurry.")
                            print("You hear a roar,")
                            print("and look behind you,")
                            print("and realize what scared them.")

                            import time
                            time.sleep(1)

                            print("A giant Basilisk is staring right at you.")
                            print("HURRY YOU MUST CHOOSE WHAT TO DO!")

                            answer = input("What do you do? (attack/hide)")

                            if answer.lower().strip() == "attack":
                                print("You fight the Basilisk,")
                                print("and end up getting scraped")
                                print("by one of its fangs.")
                                print("This poisons you,")
                                print("but you must finish what you started.")
                                print("You continue to fight,")
                                print("and end up being in a fight")
                                print("that takes hours and hours.")
                                print("You eventually end up")
                                print("on top of a building,")
                                print("and you jump off,")
                                print("and stab the basalisk.")
                                print("The snake falls motionless")
                                print("to the ground.")
                                print("You collect the supplies,")
                                print("and return to the village.")
                                print("You live rest of you years,")
                                print("and grow old,")
                                print("and you remembered as a hero.")
                                print("CONGRATS! YOU WON!")
                                print("This is the end!")

                            elif answer.lower().strip() == "hide":
                                print("You hide from the snake.")
                                print("But Basalisks have a great")
                                print("sense of smell,")
                                print("and it finds you.")
                                print("It bites you")
                                print("which ends up killing you.")
                                print("GAME OVER!")

                                '#####End of Path#####'

            elif int(answer) > 50 and answer <= 80:
                print("You are getting old Hunter. Your age may hurt you.")

                answer = input("Do you want to continue? (yes/no)")

                if answer.lower().strip() == "yes":

                    print("Great! Welcome to Camp Prust!")
                    print("I hope you can make yourself comfortable here.")

                    import time
                    time.sleep(1.5)

                    print("We need food and supplies can you do one?")

                    answer = input("Where would you rather go? (woods/settlement)")

                    if answer.lower().strip() == "woods":
                        print("Great!")
                        print("You are going to help us,")
                        print("get some food!")
                        print("The people love meats and berries,")
                        print("beware of Ogres at night.")
                        print("While hunting,")
                        print("one of your hunters get hurt,")
                        print("you only have 1 hour nightfall.")
                        print("There is just enough time,")
                        print("to get out of the woods.")
                        print("Sadly if you want to save the hunter,")
                        print("you must stay during the night")

                answer = input("What do you do? (leave him/help him)")

                if answer.lower().strip() == "leave him":
                    print("You decided to leave the fellow hunter.")
                    print("As you leave you hear the hunters scream,")
                    print("it pierces your ears and the guilt sets in.")
                    print("You bring the food back to Prust.")
                    print("Some of the people realize the missing person.")
                    print("You see the family of the hunter in the distance.")
                    print("They comfront you and ask what happened.")
                    print("How do you tell them he died?")

                    answer = input("(left him/with honor)")

                    if answer.lower().strip() == "left him":
                        print("HOW COULD YOU!")
                        print("He trusted you with his life,")
                        print("and you betrayed him.")
                        print("The people of Prust seem to be angry.")
                        print("Leave Prust,")
                        print("and never return you traitor,")
                        print("you hear in the crowd.")
                        print("We will kill you if you stay here,")
                        print("you hear,")
                        print("from another member of the crowd")
                        print("Adventurer,")
                        print("I fear you are in danger here,")
                        print("and you have to leave.")
                        print("As you leave Prust,")
                        print("you keep the food you gathered.")
                        print("10 days later")
                        print("You find yourself in the desert,")
                        print("you realize you need food and water.")
                        print("There is no oasis near by,")
                        print("and you start to realize,")
                        print("this could be your last couple days,")
                        print("but you must move forward.")
                        print("4 days later")
                        print("You are officially out of food and water,")
                        print("You start to hallucinate and see things.")
                        print("In the distance you see a cactus,")
                        print("and a lizard.")
                        print("The cactus has water in it which can help,")
                        print("the lizard would be good food.")

                        answer = input("Which do you choose? (lizard/cactus)")

                        if answer.lower().strip() == "lizard":
                            print("You walk over to the lizard,")
                            print("and kill it.")
                            print("You make a fire and start to cook it.")
                            print("As you cook it,")
                            print("you go over to the cactus,")
                            print("when you get to the cactus,")
                            print("you cut it open,")
                            print("and drink the water.")
                            print("You then set up camp,")
                            print("and sleep so that you can continue on.")
                            print("The next day you see a town in the desert.")
                            print("You have no clue who is in the town.")
                            print("Should you enter the town?")

                            answer = input("(yes/no)")

                            if answer.lower().strip() == "yes":
                                print("You enter the town,")
                                print("and the people")
                                print("of the town are welcoming.")
                                print("They offer you food,")
                                print("water, and shelter.")
                                print("They only ask you help,")
                                print("take out a druid.")
                                print("that has been terrorizing their town.")
                                print("The druid is a millenia old,")
                                print("and very wise.")
                                print("Will you help the town?")

                                answer = input("(yes/no)")

                                if answer.lower().strip() == "yes":
                                    print("Thank you hunter!")
                                    print("The druids only known location is,")
                                    print("up on mount mordoth.")
                                    print("You will need to be careful.")
                                    print("The wilderness is dangerous.")
                                    print("We can give you some supplies,")
                                    print("Your treck starts today,")
                                    print("The village offers you two things.")
                                    print("You can only take one.")
                                    print("They offer you a horse for travel,")
                                    print("or the sword of desolation")
                                    print("that glows when danger lurks.")
                                    print("Which will you take?")

                                    answer = input("(horse/sword)")

                                    if answer.lower().strip() == "horse":
                                        print("You took the horse,")
                                        print("to the top of mount mordoth,")
                                        print("and went into the tower.")
                                        print("You entered his keep,")
                                        print("to find nothing.")
                                        print("As you search for him,")
                                        print("you hear something")
                                        print("coming from the next room.")
                                        print("You enter the room,")
                                        print("and find an open spell book,")
                                        print("and you go to investigate it.")
                                        print("There is a blast of light,")
                                        print("the was druid was behind you.")
                                        print("You find yourself in a cage.")
                                        print("You have no way to escape")
                                        print("the cage,")
                                        print("because it is locked by magic.")
                                        print("You were stuck there,")
                                        print("for the rest of your days.")
                                        print("GAME OVER! You lose!")

                                        '###########END OF PATH###########'

                                    elif answer.lower().strip() == "sword":
                                        print("Great choice!")
                                        print("You start your adventure.")
                                        print("After about one week,")
                                        print("of trecking up the mountain,")
                                        print("you finally arrive.")
                                        print("You enter the druids tower,")
                                        print("to stop his reign.")
                                        print("You search,")
                                        print("and find a spell book.")
                                        print("Then,")
                                        print("You see your sword glow.")
                                        print("Will you search,")
                                        print("or go to the spell book?")

                                        answer = input("(book/search)")

                                        if answer.lower().strip() == "book":
                                            print("You walk toward the book,")
                                            print("and ignore your sword.")
                                            print("Then,")
                                            print("there is a blast of light,")
                                            print("because he was behind you.")
                                            print("You then,")
                                            print("find yourself in a cage.")
                                            print("You have no way to escape,")
                                            print("because magic locked it.")
                                            print("You were stuck there,")
                                            print("for the rest of your days.")
                                            print("GAME OVER! You lose!")

                                            '###########END OF PATH###########'

                                        elif answer.lower().strip() == "search":
                                            print("You search the room,")
                                            print("and realize,")
                                            print("something is behind you.")
                                            print("You turn around,")
                                            print("and see the druid")
                                            print("casting a spell.")
                                            print("You tackle him,")
                                            print("which starts a fight")
                                            print("You two are sharing blows,")
                                            print("back and forth,")
                                            print("until you have him,")
                                            print("beat on the ground.")
                                            print("You have your sword")
                                            print("pointing to him,")
                                            print("and he asks for mercy.")
                                            print("Will you take him hostage,")
                                            print("or strike him down?")

                                            answer = input("(kill/hostage)")

                                            if answer.lower().strip() == "hostage":
                                                print("You bring him back")
                                                print("to the town,")
                                                print("and there is cheering,")
                                                print("you have defeated him.")
                                                print("You take him")
                                                print("to his cell.")
                                                print("You are gifted gold,")
                                                print("for your trouble.")
                                                print("Your their hero,")
                                                print("and your a legend,")
                                                print("whom will never die.")
                                                print("CONGRATS!")
                                                print("You became a hero!")
                                                print("That is the end!")

                                                '#######END OF STORY!#######'

                                            elif answer.lower.strip() == "kill":
                                                print("You attempt to")
                                                print("strike him down,")
                                                print("but he has ward on.")
                                                print("This protects him,")
                                                print("from death.")
                                                print("It kills the person")
                                                print("trying to kill him.")
                                                print("GAME OVER! You lose!")

                                                '########END OF PATH#######'

                                    elif answer.lower().strip() == "no":
                                        print("You continue on your journey.")
                                        print("A couple days later")
                                        print("you realize,")
                                        print("that you still need food.")
                                        print("You continue,")
                                        print("and find a dead animal,")
                                        print("on the ground.")
                                        print("Due to the lack of food,")
                                        print("you go and take the animal.")
                                        print("As you eat the animal,")
                                        print("there is a coyote")
                                        print("that wants the food.")
                                        print("It sneaks up behind you,")
                                        print("and attacks,")
                                        print("and you were not ready.")
                                        print("The coyote kills you.")
                                        print("GAME OVER! YOU DIED!")

                                        '###### END OF PATH ######'

                                elif answer.lower().strip() == "cactus":
                                    print("You go to the cactus,")
                                    print("and cut it open,")
                                    print("and drink the water.")
                                    print("After you drink the water,")
                                    print("you look for the lizard.")
                                    print("The lizard is gone,")
                                    print("and now you have no food.")
                                    print("A long time later")
                                    print("30 days ago starvation set in,")
                                    print("You have yet to find any food.")
                                    print("4 days later")
                                    print("GAME OVER! YOU DIED! :(")

                                    '###### END OF PATH #####'

                        elif answer.lower().strip() == "help him":
                            print("Thank you adventurer!")
                            print("We have to be quiet in order to escape,")
                            print("if we are not the Ogres,")
                            print("will find us and eat us.")
                            print("The only way out is,")
                            print("the way we came so we must hurry.")
                            print("You take the hunter,")
                            print("and help him through the woods,")
                            print("You start to get close to the exit,")
                            print("you put him on his horse,")
                            print("and he rides off to Prust.")
                            print("Thats when you hear,")
                            print("something behind you,")
                            print("then everything goes black.")
                            print("You awaken at a Ogre village.")
                            print("There is a fire in front of you,")
                            print("and you are tied to a log.")
                            print("You have none of your weapons,")
                            print("and you start to look around,")
                            print("for something to get yourself free.")
                            print("You see a knife near your feet,")
                            print("and the fire is behind you.")
                            print("How will you escape?")

                            answer = input("(cut out/ burn the rope)")

                            if answer.lower().strip() == "cut out":
                                print("You reach for the knife and grab it.")
                                print("You had no clue but it was a trap,")
                                print("The Ogres wanted you")
                                print("to grab the knife.")
                                print("They now decide t")
                                print("o put you over the fire.")
                                print("You now have no way out,")
                                print("and end up burning alive.")
                                print("GAME OVER! YOU DIED! :(")

                                '###### END OF PATH #####'

                            elif answer.lower().strip() == "burn the rope":
                                print("You start to wiggle towards the fire.")
                                print("The Ogres have no idea,")
                                print("what you doing.")
                                print("You get close to the fire,")
                                print("and the rope starts to burn.")
                                print("In order to burn the rope,")
                                print("you must burn your hands.")
                                print("You take the sacrafice,")
                                print("and burn your hands.")
                                print("After a bit you are free,")
                                print("and sneak away.")
                                print("You make your way out of the woods,")
                                print("then you have to start wrapping")
                                print("your hands in cloth")
                                print("in order to protect them")
                                print("from futher harm.")
                                print("You escaped,")
                                print("but lost your share of food,")
                                print("because of the Ogres.")
                                print("Your hourse is gone,")
                                print("and you must walk back to Prust.")
                                print("6 days later")
                                print("You arrived in Prust,")
                                print("and you are greeted with open arms.")
                                print("You see the hunter you saved,")
                                print("and he asks")
                                print("what happened to your hands.")
                                print("You explain it to crowd,")
                                print("and that you lost the food.")
                                print("They said that they are not worried")
                                print("about the food,")
                                print("They are more worried")
                                print("about your hands and healing them.")
                                print("They say that there is a healer,")
                                print("who can help,")
                                print("or you can heal your hand.")
                                print("What do you want to do?")

                                answer = input("(healer/by yourself)")

                                if answer.lower().strip() == "healer":
                                    print("Welcome adventurer...")

                                    import time
                                    time.sleep(1.5)

                                    print("You see a hooded figure.")
                                    print("I see your hand is severly burned.")
                                    print("I have two choices for you...")
                                    print("The first one is")
                                    print("the double-edged potion.")
                                    print("The second is an herb,")
                                    print("that takes a while to work.")
                                    print("Which one do you want?")

                                    answer = input("(herb/potion)")

                                    if answer.lower().strip() == "herb":
                                        print("You take take the herb,")
                                        print("and you heal,")
                                        print("but it takes weeks to heal.")
                                        print("The town has one last request.")
                                        print("There is a monster")
                                        print("that is outside our walls.")
                                        print("This monster")
                                        print("keeps us from leaving,")
                                        print("and holds us hostage.")
                                        print("Can you help us?")

                                        answer = input("(yes/no)")

                                        if answer.lower().strip() == "yes":
                                            print("The monster")
                                            print("is known as the Fargwa,")
                                            print("says the towns people.")
                                            print("This monster")
                                            print("may not be that big,")
                                            print("but it is dangerous.")
                                            print("You leave in order to")
                                            print("find the Fargwa,")
                                            print("and find dead soldiers.")
                                            print("You investigate them.")
                                            print("Then you hear the roar")
                                            print("of the Fargwa")
                                            print("You must kill it.")
                                            print("You attack and attack,")
                                            print("but it does nothing.")
                                            print("Then,")
                                            print("you decide to lead it,")
                                            print("towards the rapids.")
                                            print("You jump on a rock")
                                            print("in the rapids,")
                                            print("and the Fargwa follows.")
                                            print("It hits a rock that moved,")
                                            print("and it slipped")
                                            print("into the rapids,")
                                            print("and it was gone forever.")
                                            print("You make your way back")
                                            print("to the village.")
                                            print("When you get back,")
                                            print("you are greated")
                                            print("like a hero.")
                                            print("CONGRATS!")
                                            print("You completed the story,")
                                            print("and became a hero!")
                                            print("This is the end!")

                                        elif answer.lower().strip() == "no":
                                            print("Well I guess we aren't")
                                            print("that important to you.")
                                            print("Go about your life.")
                                            print("We will have to live")
                                            print("in fear now.")
                                            print("GAME OVER!")

                                            '####End of Path####'

                                    elif answer.lower().strip() == "potion":
                                        print("This potion healed you,")
                                        print("but made you lose your memory,")
                                        print("of why you were there.")
                                        print("You go on with your life,")
                                        print("without any recolection")
                                        print("of who you are.")
                                        print("GAME OVER!")

                                        '#####End of Path#####'

                                elif answer.lower().strip() == "by yourself":

                                    print("You know some healing.")
                                    print("The most basic potion")
                                    print("I know is the green potion.")
                                    print("This potion heals you,")
                                    print("but takes a day to work.")
                                    print("Or,")
                                    print("I could let myself heal over time.")
                                    print("How should I heal myself?")

                                    answer = input("(over time/green potion)")

                                    if answer.lower().strip() == "over time":
                                        print("The burn heals over time.")
                                        print("THe issue is that you lost")
                                        print("the function of that hand.")
                                        print("This forces you stop")
                                        print("your adventuring,")
                                        print("and quit being a hunter.")
                                        print("GAME OVER!")

                                        '#####End of Path#####'

                                    elif answer.lower().strip() == "green potion":
                                        print("You heal after a couple days.")
                                        print("The people")
                                        print("of the village thank you,")
                                        print("for your help with the food.")
                                        print("You are given gold,")
                                        print("and a large house")
                                        print("in the village.")
                                        print("The people hold a celebration,")
                                        print("and you are granted")
                                        print("the rank HERO!")
                                        print("CONGRATS! YOU WON!")
                                        print("That is the end!")

                                        '#####End of Story#####'

                    elif answer.lower().strip() == "settlement":
                        print("Cool!")
                        print("You are going to get our supplies!")
                        print("You need to make your way to Numenthorn.")
                        print("There you will find supplies")
                        print("that were stolen from us.")
                        print("The commoners there can be hostile,")
                        print("so bring your weapons.")
                        print("You reach your Numenthorn,")
                        print("and it is quiet.")
                        print("It looks like everyone left,")
                        print("and in hurry.")
                        print("You hear a roar,")
                        print("and look behind you,")
                        print("and realize what scared them.")

                        import time
                        time.sleep(1)

                        print("A giant Basilisk is staring right at you.")
                        print("HURRY YOU MUST CHOOSE WHAT TO DO!")

                        answer = input("What do you do? (attack/hide)")

                        if answer.lower().strip() == "attack":
                            print("You fight the Basilisk,")
                            print("and end up getting scraped")
                            print("by one of its fangs.")
                            print("This poisons you,")
                            print("but you must finish what you started.")
                            print("You continue to fight,")
                            print("and end up being in a fight")
                            print("that takes hours and hours.")
                            print("You eventually end up")
                            print("on top of a building,")
                            print("and you jump off,")
                            print("and stab the basalisk.")
                            print("The snake falls motionless")
                            print("to the ground.")
                            print("You collect the supplies,")
                            print("and return to the village.")
                            print("You live rest of you years,")
                            print("and grow old,")
                            print("and you remembered as a hero.")
                            print("CONGRATS! YOU WON!")
                            print("This is the end!")

                        elif answer.lower().strip() == "hide":
                            print("You hide from the snake.")
                            print("But Basalisks have a great")
                            print("sense of smell,")
                            print("and it finds you.")
                            print("It bites you")
                            print("which ends up killing you.")
                            print("GAME OVER!")

                            '#####End of Path#####'

            elif int(answer) > 80:
                print("Sorry, but you are too old Hunter.")
                print("Your age will only hold you back.")

        elif answer.lower.strip() == "girl":
            answer = input("What is your age? (has to be above 18!!)")

            if int(answer) < 18:
                print("Sorry, go back to your parents you are not ready.")
                print("Try again when you are older.")

            elif int(answer) >= 18 and int(answer) <= 23:
                print("You are a new hunter!")

                answer = input("Do you want to continue? (yes/no)")

        if answer.lower().strip() == "yes":

            print("Great! Welcome to Camp Prust!")
            print("I hope you can make yourself comfortable here.")

            import time
            time.sleep(1.5)

            print("We need food and supplies can you do one?")

            answer = input("Where would you rather go? (woods/settlement)")

            if answer.lower().strip() == "woods":
                print("Great! You are going to help us get some food!")
                print("The people from Camp Prust love meats and berries,")
                print("beware though Ogres wander in the woods at night.")
                print("While hunting,")
                print("one of your fellow hunters get severely hurt,")
                print("you only have 1 hour before it becomes dark.")
                print("There is just enough time,")
                print("to get out of the woods.")
                print("Sadly if you want to save the hunter,")
                print("you must stay during the night")

                answe = input("What do you do? (leave him/help him)")

                if answer.lower().strip() == "leave him":
                    print("You decided to leave the fellow hunter.")
                    print("As you leave you hear the hunters scream,")
                    print("it pierces your ears and the guilt sets in.")
                    print("You bring the food back to Prust.")
                    print("Some of the people realize the missing person.")
                    print("You see the family of the hunter in the distance.")
                    print("They comfront you and ask what happened.")
                    print("How do you tell them he died?")

                    answer = input("(left him/with honor)")

                    if answer.lower().strip() == "left him":
                        print("HOW COULD YOU!")
                        print("He trusted you with his life,")
                        print("and you betrayed him.")
                        print("The people of Prust seem to be angry.")
                        print("Leave Prust,")
                        print("and never return you traitor,")
                        print("you hear in the crowd.")
                        print("We will kill you if you stay here,")
                        print("you hear,")
                        print("from another member of the crowd")
                        print("Adventurer,")
                        print("I fear you are in danger here,")
                        print("and you have to leave.")
                        print("As you leave Prust,")
                        print("you keep the food you gathered.")
                        print("10 days later")
                        print("You find yourself in the desert,")
                        print("you realize you need food and water.")
                        print("There is no oasis near by,")
                        print("and you start to realize,")
                        print("this could be your last couple days,")
                        print("but you must move forward.")
                        print("4 days later")
                        print("You are officially out of food and water,")
                        print("You start to hallucinate and see things.")
                        print("In the distance you see a cactus,")
                        print("and a lizard.")
                        print("The cactus has water in it which can help,")
                        print("the lizard would be good food.")

                        answer = input("Which do you choose? (lizard/cactus)")

                        if answer.lower().strip() == "lizard":
                            print("You walk over to the lizard,")
                            print("and kill it.")
                            print("You make a fire and start to cook it.")
                            print("As you cook it,")
                            print("you go over to the cactus,")
                            print("when you get to the cactus,")
                            print("you cut it open,")
                            print("and drink the water.")
                            print("You then set up camp,")
                            print("and sleep so that you can continue on.")
                            print("The next day you see a town in the desert.")
                            print("You have no clue who is in the town.")
                            print("Should you enter the town?")

                            answer = input("(yes/no)")

                            if answer.lower().strip() == "yes":
                                print("You enter the town,")
                                print("and the people")
                                print("of the town are welcoming.")
                                print("They offer you food,")
                                print("water, and shelter.")
                                print("They only ask you help,")
                                print("take out a druid.")
                                print("that has been terrorizing their town.")
                                print("The druid is a millenia old,")
                                print("and very wise.")
                                print("Will you help the town?")

                                answer = input("(yes/no)")

                                if answer.lower().strip() == "yes":
                                    print("Thank you hunter!")
                                    print("The druids only known location is,")
                                    print("up on mount mordoth.")
                                    print("You will need to be careful.")
                                    print("The wilderness is dangerous.")
                                    print("We can give you some supplies,")
                                    print("Your treck starts today,")
                                    print("The village offers you two things.")
                                    print("You can only take one.")
                                    print("They offer you a horse for travel,")
                                    print("or the sword of desolation")
                                    print("that glows when danger lurks.")
                                    print("Which will you take?")

                                    answer = input("(horse/sword)")

                                    if answer.lower().strip() == "horse":
                                        print("You took the horse,")
                                        print("to the top of mount mordoth,")
                                        print("and went into the tower.")
                                        print("You entered his keep,")
                                        print("to find nothing.")
                                        print("As you search for him,")
                                        print("you hear something")
                                        print("coming from the next room.")
                                        print("You enter the room,")
                                        print("and find an open spell book,")
                                        print("and you go to investigate it.")
                                        print("There is a blast of light,")
                                        print("the was druid was behind you.")
                                        print("You find yourself in a cage.")
                                        print("You have no way to escape")
                                        print("the cage,")
                                        print("because it is locked by magic.")
                                        print("You were stuck there,")
                                        print("for the rest of your days.")
                                        print("GAME OVER! You lose!")

                                        '###########END OF PATH###########'

                                    elif answer.lower().strip() == "sword":
                                        print("Great choice!")
                                        print("You start your adventure.")
                                        print("After about one week,")
                                        print("of trecking up the mountain,")
                                        print("you finally arrive.")
                                        print("You enter the druids tower,")
                                        print("to stop his reign.")
                                        print("You search,")
                                        print("and find a spell book.")
                                        print("Then,")
                                        print("You see your sword glow.")
                                        print("Will you search,")
                                        print("or go to the spell book?")

                                        answer = input("(book/search)")

                                        if answer.lower().strip() == "book":
                                            print("You walk toward the book,")
                                            print("and ignore your sword.")
                                            print("Then,")
                                            print("there is a blast of light,")
                                            print("because he was behind you.")
                                            print("You then,")
                                            print("find yourself in a cage.")
                                            print("You have no way to escape,")
                                            print("because magic locked it.")
                                            print("You were stuck there,")
                                            print("for the rest of your days.")
                                            print("GAME OVER! You lose!")

                                            '###########END OF PATH###########'

                                        elif answer.lower().strip() == "search":
                                            print("You search the room,")
                                            print("and realize,")
                                            print("something is behind you.")
                                            print("You turn around,")
                                            print("and see the druid")
                                            print("casting a spell.")
                                            print("You tackle him,")
                                            print("which starts a fight")
                                            print("You two are sharing blows,")
                                            print("back and forth,")
                                            print("until you have him,")
                                            print("beat on the ground.")
                                            print("You have your sword")
                                            print("pointing to him,")
                                            print("and he asks for mercy.")
                                            print("Will you take him hostage,")
                                            print("or strike him down?")

                                            answer = input("(kill/hostage)")

                                            if answer.lower().strip() == "hostage":
                                                print("You bring him back")
                                                print("to the town,")
                                                print("and there is cheering,")
                                                print("you have defeated him.")
                                                print("You take him")
                                                print("to his cell.")
                                                print("You are gifted gold,")
                                                print("for your trouble.")
                                                print("Your their hero,")
                                                print("and your a legend,")
                                                print("whom will never die.")
                                                print("CONGRATS!")
                                                print("You became a hero!")
                                                print("That is the end!")

                                                '#######END OF STORY!#######'

                                            elif answer.lower.strip() == "kill":
                                                print("You attempt to")
                                                print("strike him down,")
                                                print("but he has ward on.")
                                                print("This protects him,")
                                                print("from death.")
                                                print("It kills the person")
                                                print("trying to kill him.")
                                                print("GAME OVER! You lose!")

                                                '########END OF PATH#######'

                                    elif answer.lower().strip() == "no":
                                        print("You continue on your journey.")
                                        print("A couple days later")
                                        print("you realize,")
                                        print("that you still need food.")
                                        print("You continue,")
                                        print("and find a dead animal,")
                                        print("on the ground.")
                                        print("Due to the lack of food,")
                                        print("you go and take the animal.")
                                        print("As you eat the animal,")
                                        print("there is a coyote")
                                        print("that wants the food.")
                                        print("It sneaks up behind you,")
                                        print("and attacks,")
                                        print("and you were not ready.")
                                        print("The coyote kills you.")
                                        print("GAME OVER! YOU DIED!")

                                        '###### END OF PATH ######'

                                elif answer.lower().strip() == "cactus":
                                    print("You go to the cactus,")
                                    print("and cut it open,")
                                    print("and drink the water.")
                                    print("After you drink the water,")
                                    print("you look for the lizard.")
                                    print("The lizard is gone,")
                                    print("and now you have no food.")
                                    print("A long time later")
                                    print("30 days ago starvation set in,")
                                    print("You have yet to find any food.")
                                    print("4 days later")
                                    print("GAME OVER! YOU DIED! :(")

                                    '###### END OF PATH #####'

                        elif answer.lower().strip() == "help him":
                            print("Thank you adventurer!")
                            print("We have to be quiet in order to escape,")
                            print("if we are not the Ogres,")
                            print("will find us and eat us.")
                            print("The only way out is,")
                            print("the way we came so we must hurry.")
                            print("You take the hunter,")
                            print("and help him through the woods,")
                            print("You start to get close to the exit,")
                            print("you put him on his horse,")
                            print("and he rides off to Prust.")
                            print("Thats when you hear,")
                            print("something behind you,")
                            print("then everything goes black.")
                            print("You awaken at a Ogre village.")
                            print("There is a fire in front of you,")
                            print("and you are tied to a log.")
                            print("You have none of your weapons,")
                            print("and you start to look around,")
                            print("for something to get yourself free.")
                            print("You see a knife near your feet,")
                            print("and the fire is behind you.")
                            print("How will you escape?")

                            answer = input("(cut out/ burn the rope)")

                            if answer.lower().strip() == "cut out":
                                print("You reach for the knife and grab it.")
                                print("You had no clue but it was a trap,")
                                print("The Ogres wanted you")
                                print("to grab the knife.")
                                print("They now decide t")
                                print("o put you over the fire.")
                                print("You now have no way out,")
                                print("and end up burning alive.")
                                print("GAME OVER! YOU DIED! :(")

                                '###### END OF PATH #####'

                            elif answer.lower().strip() == "burn the rope":
                                print("You start to wiggle towards the fire.")
                                print("The Ogres have no idea,")
                                print("what you doing.")
                                print("You get close to the fire,")
                                print("and the rope starts to burn.")
                                print("In order to burn the rope,")
                                print("you must burn your hands.")
                                print("You take the sacrafice,")
                                print("and burn your hands.")
                                print("After a bit you are free,")
                                print("and sneak away.")
                                print("You make your way out of the woods,")
                                print("then you have to start wrapping")
                                print("your hands in cloth")
                                print("in order to protect them")
                                print("from futher harm.")
                                print("You escaped,")
                                print("but lost your share of food,")
                                print("because of the Ogres.")
                                print("Your hourse is gone,")
                                print("and you must walk back to Prust.")
                                print("6 days later")
                                print("You arrived in Prust,")
                                print("and you are greeted with open arms.")
                                print("You see the hunter you saved,")
                                print("and he asks")
                                print("what happened to your hands.")
                                print("You explain it to crowd,")
                                print("and that you lost the food.")
                                print("They said that they are not worried")
                                print("about the food,")
                                print("They are more worried")
                                print("about your hands and healing them.")
                                print("They say that there is a healer,")
                                print("who can help,")
                                print("or you can heal your hand.")
                                print("What do you want to do?")

                                answer = input("(healer/by yourself)")

                                if answer.lower().strip() == "healer":
                                    print("Welcome adventurer...")

                                    import time
                                    time.sleep(1.5)

                                    print("You see a hooded figure.")
                                    print("I see your hand is severly burned.")
                                    print("I have two choices for you...")
                                    print("The first one is")
                                    print("the double-edged potion.")
                                    print("The second is an herb,")
                                    print("that takes a while to work.")
                                    print("Which one do you want?")

                                    answer = input("(herb/potion)")

                                    if answer.lower().strip() == "herb":
                                        print("You take take the herb,")
                                        print("and you heal,")
                                        print("but it takes weeks to heal.")
                                        print("The town has one last request.")
                                        print("There is a monster")
                                        print("that is outside our walls.")
                                        print("This monster")
                                        print("keeps us from leaving,")
                                        print("and holds us hostage.")
                                        print("Can you help us?")

                                        answer = input("(yes/no)")

                                        if answer.lower().strip() == "yes":
                                            print("The monster")
                                            print("is known as the Fargwa,")
                                            print("says the towns people.")
                                            print("This monster")
                                            print("may not be that big,")
                                            print("but it is dangerous.")
                                            print("You leave in order to")
                                            print("find the Fargwa,")
                                            print("and find dead soldiers.")
                                            print("You investigate them.")
                                            print("Then you hear the roar")
                                            print("of the Fargwa")
                                            print("You must kill it.")
                                            print("You attack and attack,")
                                            print("but it does nothing.")
                                            print("Then,")
                                            print("you decide to lead it,")
                                            print("towards the rapids.")
                                            print("You jump on a rock")
                                            print("in the rapids,")
                                            print("and the Fargwa follows.")
                                            print("It hits a rock that moved,")
                                            print("and it slipped")
                                            print("into the rapids,")
                                            print("and it was gone forever.")
                                            print("You make your way back")
                                            print("to the village.")
                                            print("When you get back,")
                                            print("you are greated")
                                            print("like a hero.")
                                            print("CONGRATS!")
                                            print("You completed the story,")
                                            print("and became a hero!")
                                            print("This is the end!")

                                        elif answer.lower().strip() == "no":
                                            print("Well I guess we aren't")
                                            print("that important to you.")
                                            print("Go about your life.")
                                            print("We will have to live")
                                            print("in fear now.")
                                            print("GAME OVER!")

                                            '####End of Path####'

                                    elif answer.lower().strip() == "potion":
                                        print("This potion healed you,")
                                        print("but made you lose your memory,")
                                        print("of why you were there.")
                                        print("You go on with your life,")
                                        print("without any recolection")
                                        print("of who you are.")
                                        print("GAME OVER!")

                                        '#####End of Path#####'

                                elif answer.lower().strip() == "by yourself":

                                    print("You know some healing.")
                                    print("The most basic potion")
                                    print("I know is the green potion.")
                                    print("This potion heals you,")
                                    print("but takes a day to work.")
                                    print("Or,")
                                    print("I could let myself heal over time.")
                                    print("How should I heal myself?")

                                    answer = input("(over time/green potion)")

                                    if answer.lower().strip() == "over time":
                                        print("The burn heals over time.")
                                        print("THe issue is that you lost")
                                        print("the function of that hand.")
                                        print("This forces you stop")
                                        print("your adventuring,")
                                        print("and quit being a hunter.")
                                        print("GAME OVER!")

                                        '#####End of Path#####'

                                    elif answer.lower().strip() == "green potion":
                                        print("You heal after a couple days.")
                                        print("The people")
                                        print("of the village thank you,")
                                        print("for your help with the food.")
                                        print("You are given gold,")
                                        print("and a large house")
                                        print("in the village.")
                                        print("The people hold a celebration,")
                                        print("and you are granted")
                                        print("the rank HERO!")
                                        print("CONGRATS! YOU WON!")
                                        print("That is the end!")

                                        '#####End of Story#####'

                    elif answer.lower().strip() == "settlement":
                        print("Cool!")
                        print("You are going to get our supplies!")
                        print("You need to make your way to Numenthorn.")
                        print("There you will find supplies")
                        print("that were stolen from us.")
                        print("The commoners there can be hostile,")
                        print("so bring your weapons.")
                        print("You reach your Numenthorn,")
                        print("and it is quiet.")
                        print("It looks like everyone left,")
                        print("and in hurry.")
                        print("You hear a roar,")
                        print("and look behind you,")
                        print("and realize what scared them.")

                        import time
                        time.sleep(1)

                        print("A giant Basilisk is staring right at you.")
                        print("HURRY YOU MUST CHOOSE WHAT TO DO!")

                        answer = input("What do you do? (attack/hide)")

                        if answer.lower().strip() == "attack":
                            print("You fight the Basilisk,")
                            print("and end up getting scraped")
                            print("by one of its fangs.")
                            print("This poisons you,")
                            print("but you must finish what you started.")
                            print("You continue to fight,")
                            print("and end up being in a fight")
                            print("that takes hours and hours.")
                            print("You eventually end up")
                            print("on top of a building,")
                            print("and you jump off,")
                            print("and stab the basalisk.")
                            print("The snake falls motionless")
                            print("to the ground.")
                            print("You collect the supplies,")
                            print("and return to the village.")
                            print("You live rest of you years,")
                            print("and grow old,")
                            print("and you remembered as a hero.")
                            print("CONGRATS! YOU WON!")
                            print("This is the end!")

                        elif answer.lower().strip() == "hide":
                            print("You hide from the snake.")
                            print("But Basalisks have a great")
                            print("sense of smell,")
                            print("and it finds you.")
                            print("It bites you")
                            print("which ends up killing you.")
                            print("GAME OVER!")

                            '#####End of Path#####'

            elif int(answer) > 23 and int(answer) <= 50:
                print("Welcome experienced Hunter!")

                answer = input("Do you want to continue? (yes/no)")

        if answer.lower().strip() == "yes":

            print("Great! Welcome to Camp Prust!")
            print("I hope you can make yourself comfortable here.")

            import time
            time.sleep(1.5)

            print("We need food and supplies can you do one?")

            answer = input("Where would you rather go? (woods/settlement)")

            if answer.lower().strip() == "woods":
                print("Great! You are going to help us get some food!")
                print("The people from Camp Prust love meats and berries,")
                print("beware though Ogres wander in the woods at night.")
                print("While hunting,")
                print("one of your fellow hunters get severely hurt,")
                print("you only have 1 hour before it becomes dark.")
                print("There is just enough time,")
                print("to get out of the woods.")
                print("Sadly if you want to save the hunter,")
                print("you must stay during the night")

                answer = input("What do you do? (leave him/help him)")

                if answer.lower().strip() == "leave him":
                    print("You decided to leave the fellow hunter.")
                    print("As you leave you hear the hunters scream,")
                    print("it pierces your ears and the guilt sets in.")
                    print("You bring the food back to Prust.")
                    print("Some of the people realize the missing person.")
                    print("You see the family of the hunter in the distance.")
                    print("They comfront you and ask what happened.")
                    print("How do you tell them he died?")

                    answer = input("(left him/with honor)")

                    if answer.lower().strip() == "left him":
                        print("HOW COULD YOU!")
                        print("He trusted you with his life,")
                        print("and you betrayed him.")
                        print("The people of Prust seem to be angry.")
                        print("Leave Prust,")
                        print("and never return you traitor,")
                        print("you hear in the crowd.")
                        print("We will kill you if you stay here,")
                        print("you hear,")
                        print("from another member of the crowd")
                        print("Adventurer,")
                        print("I fear you are in danger here,")
                        print("and you have to leave.")
                        print("As you leave Prust,")
                        print("you keep the food you gathered.")
                        print("10 days later")
                        print("You find yourself in the desert,")
                        print("you realize you need food and water.")
                        print("There is no oasis near by,")
                        print("and you start to realize,")
                        print("this could be your last couple days,")
                        print("but you must move forward.")
                        print("4 days later")
                        print("You are officially out of food and water,")
                        print("You start to hallucinate and see things.")
                        print("In the distance you see a cactus,")
                        print("and a lizard.")
                        print("The cactus has water in it which can help,")
                        print("the lizard would be good food.")

                        answer = input("Which do you choose? (lizard/cactus)")

                        if answer.lower().strip() == "lizard":
                            print("You walk over to the lizard,")
                            print("and kill it.")
                            print("You make a fire and start to cook it.")
                            print("As you cook it,")
                            print("you go over to the cactus,")
                            print("when you get to the cactus,")
                            print("you cut it open,")
                            print("and drink the water.")
                            print("You then set up camp,")
                            print("and sleep so that you can continue on.")
                            print("The next day you see a town in the desert.")
                            print("You have no clue who is in the town.")
                            print("Should you enter the town?")

                            answer = input("(yes/no)")

                            if answer.lower().strip() == "yes":
                                print("You enter the town,")
                                print("and the people")
                                print("of the town are welcoming.")
                                print("They offer you food,")
                                print("water, and shelter.")
                                print("They only ask you help,")
                                print("take out a druid.")
                                print("that has been terrorizing their town.")
                                print("The druid is a millenia old,")
                                print("and very wise.")
                                print("Will you help the town?")

                                answer = input("(yes/no)")

                                if answer.lower().strip() == "yes":
                                    print("Thank you hunter!")
                                    print("The druids only known location is,")
                                    print("up on mount mordoth.")
                                    print("You will need to be careful.")
                                    print("The wilderness is dangerous.")
                                    print("We can give you some supplies,")
                                    print("Your treck starts today,")
                                    print("The village offers you two things.")
                                    print("You can only take one.")
                                    print("They offer you a horse for travel,")
                                    print("or the sword of desolation")
                                    print("that glows when danger lurks.")
                                    print("Which will you take?")

                                    answer = input("(horse/sword)")

                                    if answer.lower().strip() == "horse":
                                        print("You took the horse,")
                                        print("to the top of mount mordoth,")
                                        print("and went into the tower.")
                                        print("You entered his keep,")
                                        print("to find nothing.")
                                        print("As you search for him,")
                                        print("you hear something")
                                        print("coming from the next room.")
                                        print("You enter the room,")
                                        print("and find an open spell book,")
                                        print("and you go to investigate it.")
                                        print("There is a blast of light,")
                                        print("the was druid was behind you.")
                                        print("You find yourself in a cage.")
                                        print("You have no way to escape")
                                        print("the cage,")
                                        print("because it is locked by magic.")
                                        print("You were stuck there,")
                                        print("for the rest of your days.")
                                        print("GAME OVER! You lose!")

                                        '###########END OF PATH###########'

                                    elif answer.lower().strip() == "sword":
                                        print("Great choice!")
                                        print("You start your adventure.")
                                        print("After about one week,")
                                        print("of trecking up the mountain,")
                                        print("you finally arrive.")
                                        print("You enter the druids tower,")
                                        print("to stop his reign.")
                                        print("You search,")
                                        print("and find a spell book.")
                                        print("Then,")
                                        print("You see your sword glow.")
                                        print("Will you search,")
                                        print("or go to the spell book?")

                                        answer = input("(book/search)")

                                        if answer.lower().strip() == "book":
                                            print("You walk toward the book,")
                                            print("and ignore your sword.")
                                            print("Then,")
                                            print("there is a blast of light,")
                                            print("because he was behind you.")
                                            print("You then,")
                                            print("find yourself in a cage.")
                                            print("You have no way to escape,")
                                            print("because magic locked it.")
                                            print("You were stuck there,")
                                            print("for the rest of your days.")
                                            print("GAME OVER! You lose!")

                                            '###########END OF PATH###########'

                                        elif answer.lower().strip() == "search":
                                            print("You search the room,")
                                            print("and realize,")
                                            print("something is behind you.")
                                            print("You turn around,")
                                            print("and see the druid")
                                            print("casting a spell.")
                                            print("You tackle him,")
                                            print("which starts a fight")
                                            print("You two are sharing blows,")
                                            print("back and forth,")
                                            print("until you have him,")
                                            print("beat on the ground.")
                                            print("You have your sword")
                                            print("pointing to him,")
                                            print("and he asks for mercy.")
                                            print("Will you take him hostage,")
                                            print("or strike him down?")

                                            answer = input("(kill/hostage)")

                                            if answer.lower().strip() == "hostage":
                                                print("You bring him back")
                                                print("to the town,")
                                                print("and there is cheering,")
                                                print("you have defeated him.")
                                                print("You take him")
                                                print("to his cell.")
                                                print("You are gifted gold,")
                                                print("for your trouble.")
                                                print("Your their hero,")
                                                print("and your a legend,")
                                                print("whom will never die.")
                                                print("CONGRATS!")
                                                print("You became a hero!")
                                                print("That is the end!")

                                                '#######END OF STORY!#######'

                                            elif answer.lower.strip() == "kill":
                                                print("You attempt to")
                                                print("strike him down,")
                                                print("but he has ward on.")
                                                print("This protects him,")
                                                print("from death.")
                                                print("It kills the person")
                                                print("trying to kill him.")
                                                print("GAME OVER! You lose!")

                                                '########END OF PATH#######'

                                    elif answer.lower().strip() == "no":
                                        print("You continue on your journey.")
                                        print("A couple days later")
                                        print("you realize,")
                                        print("that you still need food.")
                                        print("You continue,")
                                        print("and find a dead animal,")
                                        print("on the ground.")
                                        print("Due to the lack of food,")
                                        print("you go and take the animal.")
                                        print("As you eat the animal,")
                                        print("there is a coyote")
                                        print("that wants the food.")
                                        print("It sneaks up behind you,")
                                        print("and attacks,")
                                        print("and you were not ready.")
                                        print("The coyote kills you.")
                                        print("GAME OVER! YOU DIED!")

                                        '###### END OF PATH ######'

                                elif answer.lower().strip() == "cactus":
                                    print("You go to the cactus,")
                                    print("and cut it open,")
                                    print("and drink the water.")
                                    print("After you drink the water,")
                                    print("you look for the lizard.")
                                    print("The lizard is gone,")
                                    print("and now you have no food.")
                                    print("A long time later")
                                    print("30 days ago starvation set in,")
                                    print("You have yet to find any food.")
                                    print("4 days later")
                                    print("GAME OVER! YOU DIED! :(")

                                    '###### END OF PATH #####'

                        elif answer.lower().strip() == "help him":
                            print("Thank you adventurer!")
                            print("We have to be quiet in order to escape,")
                            print("if we are not the Ogres,")
                            print("will find us and eat us.")
                            print("The only way out is,")
                            print("the way we came so we must hurry.")
                            print("You take the hunter,")
                            print("and help him through the woods,")
                            print("You start to get close to the exit,")
                            print("you put him on his horse,")
                            print("and he rides off to Prust.")
                            print("Thats when you hear,")
                            print("something behind you,")
                            print("then everything goes black.")
                            print("You awaken at a Ogre village.")
                            print("There is a fire in front of you,")
                            print("and you are tied to a log.")
                            print("You have none of your weapons,")
                            print("and you start to look around,")
                            print("for something to get yourself free.")
                            print("You see a knife near your feet,")
                            print("and the fire is behind you.")
                            print("How will you escape?")

                            answer = input("(cut out/ burn the rope)")

                            if answer.lower().strip() == "cut out":
                                print("You reach for the knife and grab it.")
                                print("You had no clue but it was a trap,")
                                print("The Ogres wanted you")
                                print("to grab the knife.")
                                print("They now decide t")
                                print("o put you over the fire.")
                                print("You now have no way out,")
                                print("and end up burning alive.")
                                print("GAME OVER! YOU DIED! :(")

                                '###### END OF PATH #####'

                            elif answer.lower().strip() == "burn the rope":
                                print("You start to wiggle towards the fire.")
                                print("The Ogres have no idea,")
                                print("what you doing.")
                                print("You get close to the fire,")
                                print("and the rope starts to burn.")
                                print("In order to burn the rope,")
                                print("you must burn your hands.")
                                print("You take the sacrafice,")
                                print("and burn your hands.")
                                print("After a bit you are free,")
                                print("and sneak away.")
                                print("You make your way out of the woods,")
                                print("then you have to start wrapping")
                                print("your hands in cloth")
                                print("in order to protect them")
                                print("from futher harm.")
                                print("You escaped,")
                                print("but lost your share of food,")
                                print("because of the Ogres.")
                                print("Your hourse is gone,")
                                print("and you must walk back to Prust.")
                                print("6 days later")
                                print("You arrived in Prust,")
                                print("and you are greeted with open arms.")
                                print("You see the hunter you saved,")
                                print("and he asks")
                                print("what happened to your hands.")
                                print("You explain it to crowd,")
                                print("and that you lost the food.")
                                print("They said that they are not worried")
                                print("about the food,")
                                print("They are more worried")
                                print("about your hands and healing them.")
                                print("They say that there is a healer,")
                                print("who can help,")
                                print("or you can heal your hand.")
                                print("What do you want to do?")

                                answer = input("(healer/by yourself)")

                                if answer.lower().strip() == "healer":
                                    print("Welcome adventurer...")

                                    import time
                                    time.sleep(1.5)

                                    print("You see a hooded figure.")
                                    print("I see your hand is severly burned.")
                                    print("I have two choices for you...")
                                    print("The first one is")
                                    print("the double-edged potion.")
                                    print("The second is an herb,")
                                    print("that takes a while to work.")
                                    print("Which one do you want?")

                                    answer = input("(herb/potion)")

                                    if answer.lower().strip() == "herb":
                                        print("You take take the herb,")
                                        print("and you heal,")
                                        print("but it takes weeks to heal.")
                                        print("The town has one last request.")
                                        print("There is a monster")
                                        print("that is outside our walls.")
                                        print("This monster")
                                        print("keeps us from leaving,")
                                        print("and holds us hostage.")
                                        print("Can you help us?")

                                        answer = input("(yes/no)")

                                        if answer.lower().strip() == "yes":
                                            print("The monster")
                                            print("is known as the Fargwa,")
                                            print("says the towns people.")
                                            print("This monster")
                                            print("may not be that big,")
                                            print("but it is dangerous.")
                                            print("You leave in order to")
                                            print("find the Fargwa,")
                                            print("and find dead soldiers.")
                                            print("You investigate them.")
                                            print("Then you hear the roar")
                                            print("of the Fargwa")
                                            print("You must kill it.")
                                            print("You attack and attack,")
                                            print("but it does nothing.")
                                            print("Then,")
                                            print("you decide to lead it,")
                                            print("towards the rapids.")
                                            print("You jump on a rock")
                                            print("in the rapids,")
                                            print("and the Fargwa follows.")
                                            print("It hits a rock that moved,")
                                            print("and it slipped")
                                            print("into the rapids,")
                                            print("and it was gone forever.")
                                            print("You make your way back")
                                            print("to the village.")
                                            print("When you get back,")
                                            print("you are greated")
                                            print("like a hero.")
                                            print("CONGRATS!")
                                            print("You completed the story,")
                                            print("and became a hero!")
                                            print("This is the end!")

                                        elif answer.lower().strip() == "no":
                                            print("Well I guess we aren't")
                                            print("that important to you.")
                                            print("Go about your life.")
                                            print("We will have to live")
                                            print("in fear now.")
                                            print("GAME OVER!")

                                            '####End of Path####'

                                    elif answer.lower().strip() == "potion":
                                        print("This potion healed you,")
                                        print("but made you lose your memory,")
                                        print("of why you were there.")
                                        print("You go on with your life,")
                                        print("without any recolection")
                                        print("of who you are.")
                                        print("GAME OVER!")

                                        '#####End of Path#####'

                                elif answer.lower().strip() == "by yourself":

                                    print("You know some healing.")
                                    print("The most basic potion")
                                    print("I know is the green potion.")
                                    print("This potion heals you,")
                                    print("but takes a day to work.")
                                    print("Or,")
                                    print("I could let myself heal over time.")
                                    print("How should I heal myself?")

                                    answer = input("(over time/green potion)")

                                    if answer.lower().strip() == "over time":
                                        print("The burn heals over time.")
                                        print("THe issue is that you lost")
                                        print("the function of that hand.")
                                        print("This forces you stop")
                                        print("your adventuring,")
                                        print("and quit being a hunter.")
                                        print("GAME OVER!")

                                        '#####End of Path#####'

                                    elif answer.lower().strip() == "green potion":
                                        print("You heal after a couple days.")
                                        print("The people")
                                        print("of the village thank you,")
                                        print("for your help with the food.")
                                        print("You are given gold,")
                                        print("and a large house")
                                        print("in the village.")
                                        print("The people hold a celebration,")
                                        print("and you are granted")
                                        print("the rank HERO!")
                                        print("CONGRATS! YOU WON!")
                                        print("That is the end!")

                                        '#####End of Story#####'

                    elif answer.lower().strip() == "settlement":
                        print("Cool!")
                        print("You are going to get our supplies!")
                        print("You need to make your way to Numenthorn.")
                        print("There you will find supplies")
                        print("that were stolen from us.")
                        print("The commoners there can be hostile,")
                        print("so bring your weapons.")
                        print("You reach your Numenthorn,")
                        print("and it is quiet.")
                        print("It looks like everyone left,")
                        print("and in hurry.")
                        print("You hear a roar,")
                        print("and look behind you,")
                        print("and realize what scared them.")

                        import time
                        time.sleep(1)

                        print("A giant Basilisk is staring right at you.")
                        print("HURRY YOU MUST CHOOSE WHAT TO DO!")

                        answer = input("What do you do? (attack/hide)")

                        if answer.lower().strip() == "attack":
                            print("You fight the Basilisk,")
                            print("and end up getting scraped")
                            print("by one of its fangs.")
                            print("This poisons you,")
                            print("but you must finish what you started.")
                            print("You continue to fight,")
                            print("and end up being in a fight")
                            print("that takes hours and hours.")
                            print("You eventually end up")
                            print("on top of a building,")
                            print("and you jump off,")
                            print("and stab the basalisk.")
                            print("The snake falls motionless")
                            print("to the ground.")
                            print("You collect the supplies,")
                            print("and return to the village.")
                            print("You live rest of you years,")
                            print("and grow old,")
                            print("and you remembered as a hero.")
                            print("CONGRATS! YOU WON!")
                            print("This is the end!")

                        elif answer.lower().strip() == "hide":
                            print("You hide from the snake.")
                            print("But Basalisks have a great")
                            print("sense of smell,")
                            print("and it finds you.")
                            print("It bites you")
                            print("which ends up killing you.")
                            print("GAME OVER!")

                            '#####End of Path#####'

        elif int(answer) > 50 and answer <= 80:
            print("You are getting old Hunter. Your age may hurt you.")

            answer = input("Do you want to continue? (yes/no)")

        if answer.lower().strip() == "yes":

            print("Great! Welcome to Camp Prust!")
            print("I hope you can make yourself comfortable here.")

            import time
            time.sleep(1.5)

            print("We need food and supplies can you do one?")

            answer = input("Where would you rather go? (woods/settlement)")

            if answer.lower().strip() == "woods":
                print("Great! You are going to help us get some food!")
                print("The people from Camp Prust love meats and berries,")
                print("beware though Ogres wander in the woods at night.")
                print("While hunting,")
                print("one of your fellow hunters get severely hurt,")
                print("you only have 1 hour before it becomes dark.")
                print("There is just enough time,")
                print("to get out of the woods.")
                print("Sadly if you want to save the hunter,")
                print("you must stay during the night")

                answer = input("What do you do? (leave him/help him)")

                if answer.lower().strip() == "leave him":
                    print("You decided to leave the fellow hunter.")
                    print("As you leave you hear the hunters scream,")
                    print("it pierces your ears and the guilt sets in.")
                    print("You bring the food back to Prust.")
                    print("Some of the people realize the missing person.")
                    print("You see the family of the hunter in the distance.")
                    print("They comfront you and ask what happened.")
                    print("How do you tell them he died?")

                    answer = input("(left him/with honor)")

                    if answer.lower().strip() == "left him":
                        print("HOW COULD YOU!")
                        print("He trusted you with his life,")
                        print("and you betrayed him.")
                        print("The people of Prust seem to be angry.")
                        print("Leave Prust,")
                        print("and never return you traitor,")
                        print("you hear in the crowd.")
                        print("We will kill you if you stay here,")
                        print("you hear,")
                        print("from another member of the crowd")
                        print("Adventurer,")
                        print("I fear you are in danger here,")
                        print("and you have to leave.")
                        print("As you leave Prust,")
                        print("you keep the food you gathered.")
                        print("10 days later")
                        print("You find yourself in the desert,")
                        print("you realize you need food and water.")
                        print("There is no oasis near by,")
                        print("and you start to realize,")
                        print("this could be your last couple days,")
                        print("but you must move forward.")
                        print("4 days later")
                        print("You are officially out of food and water,")
                        print("You start to hallucinate and see things.")
                        print("In the distance you see a cactus,")
                        print("and a lizard.")
                        print("The cactus has water in it which can help,")
                        print("the lizard would be good food.")

                        answer = input("Which do you choose? (lizard/cactus)")

                        if answer.lower().strip() == "lizard":
                            print("You walk over to the lizard,")
                            print("and kill it.")
                            print("You make a fire and start to cook it.")
                            print("As you cook it,")
                            print("you go over to the cactus,")
                            print("when you get to the cactus,")
                            print("you cut it open,")
                            print("and drink the water.")
                            print("You then set up camp,")
                            print("and sleep so that you can continue on.")
                            print("The next day you see a town in the desert.")
                            print("You have no clue who is in the town.")
                            print("Should you enter the town?")

                            answer = input("(yes/no)")

                            if answer.lower().strip() == "yes":
                                print("You enter the town,")
                                print("and the people")
                                print("of the town are welcoming.")
                                print("They offer you food,")
                                print("water, and shelter.")
                                print("They only ask you help,")
                                print("take out a druid.")
                                print("that has been terrorizing their town.")
                                print("The druid is a millenia old,")
                                print("and very wise.")
                                print("Will you help the town?")

                                answer = input("(yes/no)")

                                if answer.lower().strip() == "yes":
                                    print("Thank you hunter!")
                                    print("The druids only known location is,")
                                    print("up on mount mordoth.")
                                    print("You will need to be careful.")
                                    print("The wilderness is dangerous.")
                                    print("We can give you some supplies,")
                                    print("Your treck starts today,")
                                    print("The village offers you two things.")
                                    print("You can only take one.")
                                    print("They offer you a horse for travel,")
                                    print("or the sword of desolation")
                                    print("that glows when danger lurks.")
                                    print("Which will you take?")

                                    answer = input("(horse/sword)")

                                    if answer.lower().strip() == "horse":
                                        print("You took the horse,")
                                        print("to the top of mount mordoth,")
                                        print("and went into the tower.")
                                        print("You entered his keep,")
                                        print("to find nothing.")
                                        print("As you search for him,")
                                        print("you hear something")
                                        print("coming from the next room.")
                                        print("You enter the room,")
                                        print("and find an open spell book,")
                                        print("and you go to investigate it.")
                                        print("There is a blast of light,")
                                        print("the was druid was behind you.")
                                        print("You find yourself in a cage.")
                                        print("You have no way to escape")
                                        print("the cage,")
                                        print("because it is locked by magic.")
                                        print("You were stuck there,")
                                        print("for the rest of your days.")
                                        print("GAME OVER! You lose!")

                                        '###########END OF PATH###########'

                                    elif answer.lower().strip() == "sword":
                                        print("Great choice!")
                                        print("You start your adventure.")
                                        print("After about one week,")
                                        print("of trecking up the mountain,")
                                        print("you finally arrive.")
                                        print("You enter the druids tower,")
                                        print("to stop his reign.")
                                        print("You search,")
                                        print("and find a spell book.")
                                        print("Then,")
                                        print("You see your sword glow.")
                                        print("Will you search,")
                                        print("or go to the spell book?")

                                        answer = input("(book/search)")

                                        if answer.lower().strip() == "book":
                                            print("You walk toward the book,")
                                            print("and ignore your sword.")
                                            print("Then,")
                                            print("there is a blast of light,")
                                            print("because he was behind you.")
                                            print("You then,")
                                            print("find yourself in a cage.")
                                            print("You have no way to escape,")
                                            print("because magic locked it.")
                                            print("You were stuck there,")
                                            print("for the rest of your days.")
                                            print("GAME OVER! You lose!")

                                            '###########END OF PATH###########'

                                        elif answer.lower().strip() == "search":
                                            print("You search the room,")
                                            print("and realize,")
                                            print("something is behind you.")
                                            print("You turn around,")
                                            print("and see the druid")
                                            print("casting a spell.")
                                            print("You tackle him,")
                                            print("which starts a fight")
                                            print("You two are sharing blows,")
                                            print("back and forth,")
                                            print("until you have him,")
                                            print("beat on the ground.")
                                            print("You have your sword")
                                            print("pointing to him,")
                                            print("and he asks for mercy.")
                                            print("Will you take him hostage,")
                                            print("or strike him down?")

                                            answer = input("(kill/hostage)")

                                            if answer.lower().strip() == "hostage":
                                                print("You bring him back")
                                                print("to the town,")
                                                print("and there is cheering,")
                                                print("you have defeated him.")
                                                print("You take him")
                                                print("to his cell.")
                                                print("You are gifted gold,")
                                                print("for your trouble.")
                                                print("Your their hero,")
                                                print("and your a legend,")
                                                print("whom will never die.")
                                                print("CONGRATS!")
                                                print("You became a hero!")
                                                print("That is the end!")

                                                '#######END OF STORY!#######'

                                            elif answer.lower.strip() == "kill":
                                                print("You attempt to")
                                                print("strike him down,")
                                                print("but he has ward on.")
                                                print("This protects him,")
                                                print("from death.")
                                                print("It kills the person")
                                                print("trying to kill him.")
                                                print("GAME OVER! You lose!")

                                                '########END OF PATH#######'

                                    elif answer.lower().strip() == "no":
                                        print("You continue on your journey.")
                                        print("A couple days later")
                                        print("you realize,")
                                        print("that you still need food.")
                                        print("You continue,")
                                        print("and find a dead animal,")
                                        print("on the ground.")
                                        print("Due to the lack of food,")
                                        print("you go and take the animal.")
                                        print("As you eat the animal,")
                                        print("there is a coyote")
                                        print("that wants the food.")
                                        print("It sneaks up behind you,")
                                        print("and attacks,")
                                        print("and you were not ready.")
                                        print("The coyote kills you.")
                                        print("GAME OVER! YOU DIED!")

                                        '###### END OF PATH ######'

                                elif answer.lower().strip() == "cactus":
                                    print("You go to the cactus,")
                                    print("and cut it open,")
                                    print("and drink the water.")
                                    print("After you drink the water,")
                                    print("you look for the lizard.")
                                    print("The lizard is gone,")
                                    print("and now you have no food.")
                                    print("A long time later")
                                    print("30 days ago starvation set in,")
                                    print("You have yet to find any food.")
                                    print("4 days later")
                                    print("GAME OVER! YOU DIED! :(")

                                    '###### END OF PATH #####'

                        elif answer.lower().strip() == "help him":
                            print("Thank you adventurer!")
                            print("We have to be quiet in order to escape,")
                            print("if we are not the Ogres,")
                            print("will find us and eat us.")
                            print("The only way out is,")
                            print("the way we came so we must hurry.")
                            print("You take the hunter,")
                            print("and help him through the woods,")
                            print("You start to get close to the exit,")
                            print("you put him on his horse,")
                            print("and he rides off to Prust.")
                            print("Thats when you hear,")
                            print("something behind you,")
                            print("then everything goes black.")
                            print("You awaken at a Ogre village.")
                            print("There is a fire in front of you,")
                            print("and you are tied to a log.")
                            print("You have none of your weapons,")
                            print("and you start to look around,")
                            print("for something to get yourself free.")
                            print("You see a knife near your feet,")
                            print("and the fire is behind you.")
                            print("How will you escape?")

                            answer = input("(cut out/ burn the rope)")

                            if answer.lower().strip() == "cut out":
                                print("You reach for the knife and grab it.")
                                print("You had no clue but it was a trap,")
                                print("The Ogres wanted you")
                                print("to grab the knife.")
                                print("They now decide t")
                                print("o put you over the fire.")
                                print("You now have no way out,")
                                print("and end up burning alive.")
                                print("GAME OVER! YOU DIED! :(")

                                '###### END OF PATH #####'

                            elif answer.lower().strip() == "burn the rope":
                                print("You start to wiggle towards the fire.")
                                print("The Ogres have no idea,")
                                print("what you doing.")
                                print("You get close to the fire,")
                                print("and the rope starts to burn.")
                                print("In order to burn the rope,")
                                print("you must burn your hands.")
                                print("You take the sacrafice,")
                                print("and burn your hands.")
                                print("After a bit you are free,")
                                print("and sneak away.")
                                print("You make your way out of the woods,")
                                print("then you have to start wrapping")
                                print("your hands in cloth")
                                print("in order to protect them")
                                print("from futher harm.")
                                print("You escaped,")
                                print("but lost your share of food,")
                                print("because of the Ogres.")
                                print("Your hourse is gone,")
                                print("and you must walk back to Prust.")
                                print("6 days later")
                                print("You arrived in Prust,")
                                print("and you are greeted with open arms.")
                                print("You see the hunter you saved,")
                                print("and he asks")
                                print("what happened to your hands.")
                                print("You explain it to crowd,")
                                print("and that you lost the food.")
                                print("They said that they are not worried")
                                print("about the food,")
                                print("They are more worried")
                                print("about your hands and healing them.")
                                print("They say that there is a healer,")
                                print("who can help,")
                                print("or you can heal your hand.")
                                print("What do you want to do?")

                                answer = input("(healer/by yourself)")

                                if answer.lower().strip() == "healer":
                                    print("Welcome adventurer...")

                                    import time
                                    time.sleep(1.5)

                                    print("You see a hooded figure.")
                                    print("I see your hand is severly burned.")
                                    print("I have two choices for you...")
                                    print("The first one is")
                                    print("the double-edged potion.")
                                    print("The second is an herb,")
                                    print("that takes a while to work.")
                                    print("Which one do you want?")

                                    answer = input("(herb/potion)")

                                    if answer.lower().strip() == "herb":
                                        print("You take take the herb,")
                                        print("and you heal,")
                                        print("but it takes weeks to heal.")
                                        print("The town has one last request.")
                                        print("There is a monster")
                                        print("that is outside our walls.")
                                        print("This monster")
                                        print("keeps us from leaving,")
                                        print("and holds us hostage.")
                                        print("Can you help us?")

                                        answer = input("(yes/no)")

                                        if answer.lower().strip() == "yes":
                                            print("The monster")
                                            print("is known as the Fargwa,")
                                            print("says the towns people.")
                                            print("This monster")
                                            print("may not be that big,")
                                            print("but it is dangerous.")
                                            print("You leave in order to")
                                            print("find the Fargwa,")
                                            print("and find dead soldiers.")
                                            print("You investigate them.")
                                            print("Then you hear the roar")
                                            print("of the Fargwa")
                                            print("You must kill it.")
                                            print("You attack and attack,")
                                            print("but it does nothing.")
                                            print("Then,")
                                            print("you decide to lead it,")
                                            print("towards the rapids.")
                                            print("You jump on a rock")
                                            print("in the rapids,")
                                            print("and the Fargwa follows.")
                                            print("It hits a rock that moved,")
                                            print("and it slipped")
                                            print("into the rapids,")
                                            print("and it was gone forever.")
                                            print("You make your way back")
                                            print("to the village.")
                                            print("When you get back,")
                                            print("you are greated")
                                            print("like a hero.")
                                            print("CONGRATS!")
                                            print("You completed the story,")
                                            print("and became a hero!")
                                            print("This is the end!")

                                        elif answer.lower().strip() == "no":
                                            print("Well I guess we aren't")
                                            print("that important to you.")
                                            print("Go about your life.")
                                            print("We will have to live")
                                            print("in fear now.")
                                            print("GAME OVER!")

                                            '####End of Path####'

                                    elif answer.lower().strip() == "potion":
                                        print("This potion healed you,")
                                        print("but made you lose your memory,")
                                        print("of why you were there.")
                                        print("You go on with your life,")
                                        print("without any recolection")
                                        print("of who you are.")
                                        print("GAME OVER!")

                                        '#####End of Path#####'

                                elif answer.lower().strip() == "by yourself":

                                    print("You know some healing.")
                                    print("The most basic potion")
                                    print("I know is the green potion.")
                                    print("This potion heals you,")
                                    print("but takes a day to work.")
                                    print("Or,")
                                    print("I could let myself heal over time.")
                                    print("How should I heal myself?")

                                    answer = input("(over time/green potion)")

                                    if answer.lower().strip() == "over time":
                                        print("The burn heals over time.")
                                        print("THe issue is that you lost")
                                        print("the function of that hand.")
                                        print("This forces you stop")
                                        print("your adventuring,")
                                        print("and quit being a hunter.")
                                        print("GAME OVER!")

                                        '#####End of Path#####'

                                    elif answer.lower().strip() == "green potion":
                                        print("You heal after a couple days.")
                                        print("The people")
                                        print("of the village thank you,")
                                        print("for your help with the food.")
                                        print("You are given gold,")
                                        print("and a large house")
                                        print("in the village.")
                                        print("The people hold a celebration,")
                                        print("and you are granted")
                                        print("the rank HERO!")
                                        print("CONGRATS! YOU WON!")
                                        print("That is the end!")

                                        '#####End of Story#####'

                    elif answer.lower().strip() == "settlement":
                        print("Cool!")
                        print("You are going to get our supplies!")
                        print("You need to make your way to Numenthorn.")
                        print("There you will find supplies")
                        print("that were stolen from us.")
                        print("The commoners there can be hostile,")
                        print("so bring your weapons.")
                        print("You reach your Numenthorn,")
                        print("and it is quiet.")
                        print("It looks like everyone left,")
                        print("and in hurry.")
                        print("You hear a roar,")
                        print("and look behind you,")
                        print("and realize what scared them.")

                        import time
                        time.sleep(1)

                        print("A giant Basilisk is staring right at you.")
                        print("HURRY YOU MUST CHOOSE WHAT TO DO!")

                        answer = input("What do you do? (attack/hide)")

                        if answer.lower().strip() == "attack":
                            print("You fight the Basilisk,")
                            print("and end up getting scraped")
                            print("by one of its fangs.")
                            print("This poisons you,")
                            print("but you must finish what you started.")
                            print("You continue to fight,")
                            print("and end up being in a fight")
                            print("that takes hours and hours.")
                            print("You eventually end up")
                            print("on top of a building,")
                            print("and you jump off,")
                            print("and stab the basalisk.")
                            print("The snake falls motionless")
                            print("to the ground.")
                            print("You collect the supplies,")
                            print("and return to the village.")
                            print("You live rest of you years,")
                            print("and grow old,")
                            print("and you remembered as a hero.")
                            print("CONGRATS! YOU WON!")
                            print("This is the end!")

                        elif answer.lower().strip() == "hide":
                            print("You hide from the snake.")
                            print("But Basalisks have a great")
                            print("sense of smell,")
                            print("and it finds you.")
                            print("It bites you")
                            print("which ends up killing you.")
                            print("GAME OVER!")

                            '#####End of Path#####'

            elif int(answer) > 80:
                print("Sorry, but you are too old Hunter.")
                print("Your age will only hold you back.")

        else:
            print("We respect your answer.")
            print("But it dosent fit the parameters of the game.")

