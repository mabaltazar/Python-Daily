"""This function provides responses when you say something or ask Bob a question."""

def response(hey_bob):
    """
    The function takes in a value and provide an output based on the input value.
    "Sure." This is his response if you ask him a question, such as "How are you?"
    "Whoa, chill out!" This is his answer if you YELL AT HIM.
    "Calm down, I know what I'm doing!" This is what he says if you yell a question at him.
    "Fine. Be that way!" This is how he responds to silence.
    "Whatever." This is what he answers to anything else.

    :param hey_bob: str - the value that you say or ask bob.
    :result : str - response of bob based on the input. ("Sure.", Whoa, chill out!", "Calm     down, I know what I'm doing!", "Fine. Be that way!", "Whatever.")
    
    """
    questions = None
    bob_says = None
    
    if hey_bob.isupper():
        questions = hey_bob.strip()
    else:
        questions = hey_bob.lower().strip()

    if questions[:].endswith("?") and not questions.isupper():
        bob_says = "Sure."
    elif questions.isupper() and not questions[:].endswith("?"):
        bob_says = "Whoa, chill out!"
    elif questions[:].endswith("?") and questions.isupper():
        bob_says = "Calm down, I know what I'm doing!"
    elif questions == "":
        bob_says = "Fine. Be that way!"
    else:
        bob_says = "Whatever."
            
    return bob_says
