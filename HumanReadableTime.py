def make_readable(seconds):
    # Do something
    hours = math.floor(seconds/3600)
    seconds = seconds - (hours*3600)
    minutes = math.floor(seconds/60)
    seconds = seconds - (minutes*60)
    return '{}:{}:{}'.format(add_zero(hours), add_zero(minutes), add_zero(seconds))
    
def add_zero(number):
    if number >= 10:
        return str(number)
    else:
        return "0" + str(number)