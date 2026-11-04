def inputs():
    print("hi this is the Infection sim")
    new_sim_input()
    previous_simulation_input()
    num_of_people()
    infectiousness()
    transmissibility()
    lethality()


def new_sim_input():
    while True:
        new_sim = input("do you what to start a new simulation?(yes/no)")
        if new_sim == "yes":
            return True
        elif new_sim == "no":
            return False
        else:
            print("please enter yes or no")

def previous_simulation_input():
    while True:
        previous_sim = input("do you what to view a previous simulation?(yes/no)")
        if previous_sim == "yes":
            return True
        elif previous_sim == "no":
            return False
        else:
            print("please enter yes or no")
def num_of_people():
    while True:
        try:
            people = int(input("how many people are going to simulate?"))
            return people
        except ValueError:
            print("please enter a number")
def infectiousness():
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
    while True:
        try:
            transmissibility = int(input("what is thr distance infection can travel in pixels?"))
            return transmissibility
        except ValueError:
            print("please enter a number")

def lethality():
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