# create a priority queue 
# score will be the priority and name will be stored as data
import queue
scores = queue.PriorityQueue(maxsize=5)

def add_score(score, name):
    if scores.full():
        min_score = scores.get()
        if min_score[0] < score:
            scores.put((score, name))
        else:
            scores.put(min_score)
    else:
        scores.put((score, name))