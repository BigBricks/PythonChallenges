import string
def generate_hashtag(s):
    #your code here
    s = string.capwords(s)
    x = s.replace(" ", "")
    result = "#" + x
    if len(result) > 140 or result == "#":
        return False
    return result