def classify_sentiment(string):
    """
    This function takes a string and 
    classifies its sentiment as either
    positive or negative.
    """
    if string.lower().find("positive") != -1 or string.lower().find("amazing") !=-1:
        return "positive"
    elif string.lower().find("negative") != -1:
        return "negative"
    else:
        return "neutral"