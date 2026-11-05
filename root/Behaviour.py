import intups as I
def make_pop_dictionary():
    global population
    population = [
    ]
    for i in int(I.people):
        population.append({"person":int(I.people), "x position": 0, "y position": 0, "x speed": 0, "y speed": 0,"status":"", "immune":False},)

def make_immune():
    for i in int(I.pop_of_immunity) * int(I.people):
        population[i]["immune"] = True

def Infection_checks():
    pass
