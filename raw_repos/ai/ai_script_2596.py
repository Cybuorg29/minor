"""
Model the evolution of a population
"""

class Population:
    def __init__(self):
        self.population = []
        self.generation = 0

    def add_member(self, member):
        self.population.append(member)

    def next_generation(self):
        self.generation += 1
        self.population = self.population.create_next_generation()

class Member:
    def __init__(self, data):
        self.data = data


    def create_next_generation(self):
        next_gen_data = []
        # perform population evolution algorithm
        # ...
        return [Member(g) for g in next_gen_data]