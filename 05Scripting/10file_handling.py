path = "/Users/mekalathuruchenchaiah/Desktop/PROGRAMMING/AI Programming with Python - Bertelsmann/05Scripting/camelot.txt"
camelot_lines = []
with open(path) as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)