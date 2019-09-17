def extract_time_components(time):
    '''
>>> extract_time_components('21:30:00')
{'hours': 21, 'minutes': 30, 'seconds': 0}
>>> extract_time_components('09:01:53')
{'hours': 9, 'minutes': 1, 'seconds': 53}
    '''
    hours, minutes, seconds = [int(n) for n in time.split(':')]

    time_dict = {
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds
    }

    return time_dict

    #or

    # parts = time.split(':')

    # hours = parts[0]
    # minutes = parts[1]
    # seconds = parts[2]

    # time_dict = {}
    # time_dict['hours'] = int(hours)
    # time_dict['minutes'] = int(minutes)
    # time_dict['seconds'] = int(seconds)

    # return time_dict

extract_time_components('21:30:00')