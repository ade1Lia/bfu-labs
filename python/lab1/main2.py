from pathlib import Path
dir = input()
Path(dir).mkdir(exist_ok = True)
with open('file2.txt') as file:
    lines = list(file.read().split('\n'))[:-1]
    for i in range(len(lines)):
        open(dir + '/' + lines[i], 'w')