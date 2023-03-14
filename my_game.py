import mafia_game

striyska = mafia_game.Street("Striyska street")
striyska.set_description("Street where the big flag is located.")

kozelnytska = mafia_game.Street("Kozelnytska street")
kozelnytska.set_description("Small street where Ukranian Catolic University is")

shota_rustaveli = mafia_game.Street("Shota Rustaveli street")
shota_rustaveli.set_description("Street with public transport stops")

halytskia = mafia_game.Street("Halytskia street")
halytskia.set_description("Street in the centre with a lot of people.")

krakivska = mafia_game.Street("Krakivska street")
krakivska.set_description("Dark and close street.")

rynok = mafia_game.Street("Rynok square")
rynok.set_description("Square with the city council .")

striyska.link_street(kozelnytska, "north")
kozelnytska.link_street(striyska, "south")
kozelnytska.link_street(shota_rustaveli, "west")
shota_rustaveli.link_street(kozelnytska, "east")
shota_rustaveli.link_street(halytskia, "south")
halytskia.link_street(shota_rustaveli, "north")
halytskia.link_street(krakivska, "west")
krakivska.link_street(halytskia, "east")
krakivska.link_street(rynok, "north")
rynok.link_street(krakivska, "south")


dave = mafia_game.Person("Denis", "Tall boy with flowers")
dave.set_conversation("Aaaaaa, don't murder me. I'm just citizen")
striyska.set_character(dave)

anna = mafia_game.Person("Maria", "Girl with green eyes.")
anna.set_conversation("Tsssss.... I'm a witch...")
anna.set_weakness("chocolate")
kozelnytska.set_character(anna)

sofi = mafia_game.Person("Sofi", "Woman in glasses with a big bag")
sofi.set_conversation("I'm doctor and I can cure you")
shota_rustaveli.set_character(sofi)

max = mafia_game.Person("Max", "Strange man in a hat and big coat")
max.set_conversation("Tell your last words... I'm mafia.")
max.set_weakness("knife")
krakivska.set_character(max)

jack = mafia_game.Person("Petro", "Big man in black clothes")
jack.set_conversation("I'm a policeman. Be careful walking here at night")
halytskia.set_character(jack)

chocolate = mafia_game.Item("chocolate")
chocolate.set_description("A large block of dark chocolate")
halytskia.set_item(chocolate)

knife = mafia_game.Item("knife")
knife.set_description("A big and sharp knife")
kozelnytska.set_item(knife)

current_Street = striyska
backpack = []

dead = False
aim = 0
print("This is Lviv Mafia.\nYou should kill Mafia and Witch.\nYou will win, when you reach Rynok Square.")

while dead == False:

    print("\n")
    current_Street.get_details()

    inhabitant = current_Street.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_Street.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_Street = current_Street.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:
                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    aim += 1
                    current_Street.character = None
                else:
                    # What happens if you lose?
                    if inhabitant.weakness is None:
                        print("You killed an innocent person.")
                        print("That's the end of the game")
                        dead = True
                    else:
                        print("That's the end of the game")
                        dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_Street.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)

    if current_Street == rynok and aim == 2:
        print(current_Street.get_details())
        print("Congratulations, you have reached your home")
        dead = True