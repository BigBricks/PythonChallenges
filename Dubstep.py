def song_decoder(song):
    arr = []
    x = song.split("WUB")
    for e in x:
        if e != "":
            arr.append(e)
    return " ".join(arr)
