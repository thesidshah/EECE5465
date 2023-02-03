def to_lower_case(s):
    """ Convert a string to lowercase. E.g., 'BaNaNa' becomes 'banana'. 
    """
    return s.lower()


def create_list_from_file(filename):
    """Read words from a file and convert them to a list.
   
    Input:
    - filename: The name of a file containing one word per line.
    
    Returns
    - wordlist: a list containing all the words in the file, as strings.

    """
    wordlist = []
    with open(filename) as f:
        line = f.readline()
        while line:
            wordlist.append(line.strip())
            line = f.readline()
        return wordlist     


def strip_non_alpha(s):
    """ Remove non-alphabetic characters from the beginning and end of a string. 

    E.g. ',1what?!"' should become 'what'. Non-alphabetic characters in the middle 
    of the string should not be removed. E.g. "haven't" should remain unaltered."""
    pass


def is_inflection_of(s1,s2):
    """ Tests if s1 is a common inflection of s2. 

    The function first (a) converts both strings to lowercase and (b) strips
    non-alphabetic characters from the beginning and end of each string. 
    Then, it returns True if the two resulting two strings are equal, or 
    the first string can be produced from the second by adding the following
    endings:
    (a) 's
    (b) s
    (c) es
    (d) ing
    (e) ed
    (f) d
    """
    pass

def same(s1,s2):
    "Return True if one of the input strings is the inflection of the other."
    pass

def find_match(word,word_list):
    """Given a word, find a string in a list that is "the same" as this word.

    Input:
    - word: a string
    - word_list: a list of stings

    Return value:
    - A string in word_list that is "the same" as word, None otherwise.
    
    The string word is 'the same' as some string x in word_list, if word is the inflection of x,
    ignoring cases and leading or trailing non-alphabetic characters.
    """
    pass

if __name__=="__main__":
    
    # Test strip_non_alpha


    # Test is_inflection_of and same

    # Test find_match 
    
    pass
