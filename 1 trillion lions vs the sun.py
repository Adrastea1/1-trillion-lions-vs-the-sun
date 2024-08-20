# 1 trillion lions vs the sun (please expand)
fighter1 = 0
fighter2 = 0
mass_of_a_lion = 1
mass_of_the_sun = 1.989 * 10 ** 30
answer = 0

# if masses are pre-set
def mass_prefilled(answer):

    while True:
        print("\nEnter fighter 1")
        print("sun", "lion", "(c to cancel)", sep=", ")
        fighter_one = input()

        if fighter_one == "c":
            break
        elif fighter_one != "sun" or fighter_one != "lion":
            continue
        else:
            print("\nHow many " + str(fighter_one) + "s will there be?")
            number_of_fighter1 = input()

            while True:
                print("\nEnter fighter 2")
            fighter_two = input()

            if fighter_two == "c":
                break
            elif fighter_two != "sun" or fighter_two != "lion":
            continue
            else:
                print("\nHow many " + str(fighter_two) + "s will there be?")
            number_of_fighter2 = input()

            print("In a fight with " + str(fighter_one)
        break


# if masses are submitted by user
def mass_prefilled_not(answer):
    print("no")


print("Who would win between the sun and a trillion lions? (if we compressed both into black holes)")

# calculation
while True:
    print("Use set masses rather than your own? (y/n)(c to cancel)")
    mass = input()
    if mass == "y" or mass == "Y":
        mass_prefilled(answer)
    elif mass == "n" or mass == "N":
        mass_prefilled_not(answer)
    elif mass == "c" or mass == "C":
        break
