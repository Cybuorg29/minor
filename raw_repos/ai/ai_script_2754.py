def find_num_distinct_states(matrix):
    states = set()
    for row in matrix:
        state = "".join([str(x) for x in row])
        states.add(state)
    return len(states)