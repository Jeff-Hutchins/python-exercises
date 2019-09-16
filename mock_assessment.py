def normalize_name(string):
    """
    Takes in a string and loops through string.  Uses the isidentifier string
    method to remove anything that isn't an alpha-numberic or underscore and
    replaces it with a space.  Also removes any numbers preceding the first
    alpha and replaces them with a space.  Next line uses string methods to
    lowecase any captial letters, remove white spaces from both ends, and
    replaces white spaces in between with underscores.
    
    """
    for i in string:
        if not i.isidentifier():
            string = string.replace(i, " ")
    string = string.lower().strip('%').strip().replace(" ", "_") 
    return string

def cumsum(list):
    """
    takes in a list of numbers and adds each number to its previous number
    returns a list of cummulative numbers.

    """
    for number in range(1, len(list)):
        list[number] = list[number] + sum(list[number-1:number])
    return list
