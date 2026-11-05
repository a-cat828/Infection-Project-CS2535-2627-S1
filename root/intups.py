def inputs():
    print("hi this is the Infection sim")
    new_sim_input()
    previous_simulation_input()
    num_of_people()
    infectiousness()
    transmissibility()
    lethality()
    recoverability()
    pop_of_immunity()
    immunity_efficacy()
    name_of_disease()


def new_sim_input():
    global new_sim
    while True:
        new_sim = input("do you what to start a new simulation?(yes/no)")
        if new_sim == "yes":
            return True
        elif new_sim == "no":
            return False
        else:
            print("please enter yes or no")

def previous_simulation_input():
    global previous_sim
    while True:
        previous_sim = input("do you what to view a previous simulation?(yes/no)")
        if previous_sim == "yes":
            return True
        elif previous_sim == "no":
            return False
        else:
            print("please enter yes or no")
def num_of_people():
    global people
    while True:
        try:
            people = int(input("how many people are going to simulate?"))
            return people
        except ValueError:
            print("please enter a number")
def infectiousness():
    global infectiousness
    while True:
        try:
            infectiousness = int(input("what is the infectiousness percentage?(%)"))
            if infectiousness >100:
                print("can not be bigger than 100")
            elif infectiousness <0:
                print("can not be smaller than 0")
            else:
                return infectiousness
        except ValueError:
            print("please enter a number")

def transmissibility():
    global transmissibility
    while True:
        try:
            transmissibility = int(input("what is thr distance infection can travel in pixels?"))
            return transmissibility
        except ValueError:
            print("please enter a number")

def lethality():
    global lethality
    while True:
        try:
            lethality = int(input("what is the lethality percentage?(%)"))
            if lethality >100:
                print("can not be bigger than 100")
            elif lethality <0:
                print("can not be smaller than 0")
            else:
                return lethality
        except ValueError:
            print("please enter a number")

def recoverability():
    global recoverability
    while True:
        try:
            recoverability = int(input("what is the recoverability percentage?(%)"))
            if recoverability >100:
                print("can not be bigger than 100")
            elif recoverability <0:
                print("can not be smaller than 0")
            else:
                return recoverability
        except ValueError:
            print("please enter a number")
def pop_of_immunity():
    global pop_of_immunity
    while True:
        try:
            pop_of_immunity = int(input("what is the percentage of pepole with immunity?(%)"))
            if pop_of_immunity >100:
                print("can not be bigger than 100")
            elif pop_of_immunity <0:
                print("can not be smaller than 0")
            else:
                return pop_of_immunity
        except ValueError:
            print("please enter a number")

def immunity_efficacy():
    global immunity_efficacy
    while True:
        try:
            immunity_efficacy = int(input("what is the percentage efficay of immunity?(%)"))
            if immunity_efficacy >100:
                print("can not be bigger than 100")
            elif immunity_efficacy <0:
                print("can not be smaller than 0")
            else:
                return immunity_efficacy
        except ValueError:
            print("please enter a number")
def name_of_disease():
    global name
    name = input("what is the name of this disease?")
    return name