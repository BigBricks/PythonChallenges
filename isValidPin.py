def validate_pin(pin):
    #return true or false
    if len(pin) != 4 and len(pin) != 6:
        return False
    try:
        int(pin)
        return pin.isdigit()
    except:
        return False