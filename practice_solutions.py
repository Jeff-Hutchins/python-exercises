# def extract_time_components(time):
#     '''
# >>> extract_time_components('21:30:00')
# {'hours': 21, 'minutes': 30, 'seconds': 0}
# >>> extract_time_components('09:01:53')
# {'hours': 9, 'minutes': 1, 'seconds': 53}
#     '''
#     hours, minutes, seconds = [int(n) for n in time.split(':')]

#     time_dict = {
#         'hours': hours,
#         'minutes': minutes,
#         'seconds': seconds
#     }

#     return time_dict

    #or
    # time_dict = {}
    # parts = time.split(':')

    # hours = parts[0]
    # minutes = parts[1]
    # seconds = parts[2]

    # time_dict = {}
    # time_dict['hours'] = int(hours)
    # time_dict['minutes'] = int(minutes)
    # time_dict['seconds'] = int(seconds)

    # return time_dict

# extract_time_components('21:30:00')

def keep_long_words(words):
    '''
    >>> keep_long_words(['ls', 'codeup', 'code', 'pip', 'bayes'])
    ['codeup', 'bayes']
    >>> keep_long_words(['cd', 'ls', 'pwd'])
    []
    >>> keep_long_words(['python', 'algorithm'])
    ['python', 'algorithm']
    '''
    long_words = []
    for word in words:
        if len(word) > 4:
            long_words.append(word)
    return long_words

print(keep_long_words(['ls', 'codeup', 'code', 'pip', 'bayes']))
def make_model(cars):
    '''
    >>> cars = []
    >>> cars.append({'make': 'Toyota', 'model': 'Camry'})
    >>> cars.append({'make': 'Honda', 'model': 'Accord'})
    >>> cars.append({'make': 'Ford', 'model': 'Fiesta'})
    >>> cars.append({'make': 'Ford', 'model': 'F-150'})
    >>> make_model(cars)
    ['Toyota Camry', 'Honda Accord', 'Ford Fiesta', 'Ford F-150']
    '''
    makes_and_models = []
    for car in cars:
        makes_and_models.append(car['make'] + ' ' + car['model'])
    return makes_and_models

def extract_time_components(s):
    '''
    >>> extract_time_components('21:30:00')
    {'hours': 21, 'minutes': 30, 'seconds': 0}
    >>> extract_time_components('09:01:53')
    {'hours': 9, 'minutes': 1, 'seconds': 53}
    '''
    hours, minutes, seconds = [int(i) for i in s.split(':')]

    my_dict = {
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds
    }
    return my_dict


def greeting(x='hello', y = 'world'):
    return x + ' ' + y

print(greeting("whats", "up"))

def list_of_numbers(*x):
    numbers = []
    for i in x:
        if int(i) > 3:
            numbers.append(x)
    return numbers

print(list_of_numbers(1))

