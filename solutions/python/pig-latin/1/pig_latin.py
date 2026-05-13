""" This function takes in an English text and transform it into Pig Latin, which is a made-up childern's language."""

def translate(text):
    """Transform the input English text to Pig Latin.
    Rule 1: If a word begins with a vowel, or starts with "xr" or "yt", add an "ay" sound to the end of the word.
    Rule 2: If a word begins with one or more consonants, first move those consonants to the end of the word and then add an "ay" sound to the end of the word.
    Rule 3: If a word starts with zero or more consonants followed by "qu", first move those consonants (if any) and the "qu" part to the end of the word, and then add an "ay" sound to the end of the word.
    Rule 4: If a word starts with one or more consonants followed by "y", first move the consonants preceding the "y"to the end of the word, and then add an "ay" sound to the end of the word.

    :param text: str - English word or phrase
    :result: str - transformed English word or phrase to Pig Latin
    """
    
    vowels = ('a','e','i','o','u','xr','yt')
    is_qu = "qu"
    add_ay = "ay"
    is_y = "y"
    new_word = ''
    result_final = ''
    words = text.split()
    result_list = []

    for word in words:
        
        if word.startswith(vowels):
            new_word = [word + add_ay]
            
        elif not word.startswith(vowels):
            if is_y in word:
                if word.startswith(is_y):
                    new_word = [word[1:] + word[0] + add_ay]
                else:
                    while word[0] not in vowels and word[0] != is_y:
                        word = word[1:] + word[0]
                    new_word = [word + add_ay]
                    
            elif is_qu in word:
                if word.startswith(is_qu):
                    new_word = [word[2:] + word[:2] + add_ay]
                else:
                    while word[0] not in vowels:
                        word = word[1:] + word[0]
                        if word.startswith(is_qu):
                            word = word[2:] + word[:2]
                    new_word = [word + add_ay]
            
            else:
                while word[0] not in vowels:
                    word = word[1:] + word[0]
                new_word = [word + add_ay]
        
        result_list = result_list + new_word #combine the transformed word to a list
        result_final = " ".join(result_list) #transform list to a string
        
    return result_final