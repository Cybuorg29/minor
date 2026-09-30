def add_period(phrase):
    if not isinstance(phrase, str):
        raise ValueError("phrase should be a String")
    return phrase + "."