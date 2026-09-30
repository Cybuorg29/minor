def rating(reviews):
    score = 0
    
    positive = ["great", "amazing", "funny", "entertaining"]
    negative = ["bad", "mediocre", "average", "boring"]
    
    for comment in reviews:
        for word in positive:
            if word in comment.lower():
                score += 1
        for word in negative:
            if word in comment.lower():
                score -= 1
    
    return score / len(reviews)