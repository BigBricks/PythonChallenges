def to_camel_case(text):
    # your code here
    if text == "":
        return ""
    text = text.replace("_", "-")
    s = text.split("-")
    for x in range(len(s)):
        if x == 0:
            continue
        else:
            s[x] = s[x].capitalize()

    return "".join(s)
