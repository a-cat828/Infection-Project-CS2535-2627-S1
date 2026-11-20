import intups as I
import random
from itertools import product
def make_pop_dictionary():
    global population
    population = [
    ]
    for i in int(I.people-1):
        population.append({"person":int(I.people), "x position": 0, "y position": 0, "x speed": 0, "y speed": 0,"status":"", "immune":False},)

def make_immune():
    for i in int(I.pop_of_immunity) * int(I.people):
        population[i]["immune"] = True

# do not use, use Infection_checks() insted
def successfully_infected():
    if I.infectiousness >= random.randint(1,100) and population[combination[0]]["immune"] == True:
        population[combination[0]]["status"] = ""
    elif I.infectiousness >= random.randint(1,100) and population[combination[1]]["immune"] == True:
        population[combination[1]]["status"] = ""


def Infection_checks():
    global population, combination
    for combination in product(population,population):
        if population[combination[0]]["status"] == "dead" or population[combination[1]]["status"] == "dead":
            pass
        elif (population[combination[0]]["status"] == "infected" or population[combination[1]]["status"] == "infected") and ((abs(population[combination[0]]["x posititon"] - population[combination[1]]["x posititon"]) >= I.transmissibility) or (abs(population[combination[0]]["y posititon"] - population[combination[1]]["y posititon"]) >= I.transmissibility)):
            population[combination[0]]["status"] = "infected"
            population[combination[1]]["status"] = "infected"
            successfully_infected()
def death():
    for i in len(population):
        if population[i]["status"] == "infected" and I.lethality <=random.randint(1,100):
            population[i]["status"] = "dead"

def recovery():
    for i in len(population):
        if population[i]["status"] == "infected" and I.recoverability <=random.randint(1,100):
            population[i]["status"] = ""
