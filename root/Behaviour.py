import intups as I
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

def Infection_checks():
    for combination in product(population,population):
        if population[combination[0]]["status"] == "dead" or population[combination[1]]["status"] == "dead":
            pass
        elif (population[combination[0]]["status"] == "infected" or population[combination[1]]["status"] == "infected") and ((abs(population[combination[0]]["x posititon"] - population[combination[1]]["x posititon"]) >= I.transmissibility) or (abs(population[combination[0]]["y posititon"] - population[combination[1]]["y posititon"]) >= I.transmissibility)):
            population[combination[0]]["status"] == "infected"
            population[combination[1]]["status"] == "infected"



