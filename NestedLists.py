if __name__ == "__main__":
    scores = []
    names = []
    selected = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        names.append(name)
    secondLowest = sorted(list(set(scores)))[1]
    scoreIndexes = [i for i, x in enumerate(scores) if x == secondLowest]
    for x in scoreIndexes:
        selected.append(names[x])
    for x in sorted(selected):
        print(x)
