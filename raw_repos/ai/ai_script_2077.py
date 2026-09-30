"""
Generate a function to calculate the probability of an event
"""
def calculate_probability(num_outcomes, num_favourable_outcomes):
    # calculate probability 
    probability = float(num_favourable_outcomes) / float(num_outcomes)
    return probability
    
if __name__ == '__main__': 
    num_outcomes = 36
    num_favourable_outcomes = 9
    print("Probability of an event is: " + str(calculate_probability(num_outcomes, num_favourable_outcomes)))