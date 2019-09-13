def normalize_name(string):
    for i in string:
        if not i.isidentifier():
            string = string.replace(i, " ")
    string = string.lower().strip('%').strip().replace(" ", "_") 
    return string

def cumsum(list):
    for number in range(1, len(list)):
        list[number] = list[number] + sum(list[number-1:number])
    return list