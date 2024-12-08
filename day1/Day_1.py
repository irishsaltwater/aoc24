import os

# 8 days behind, these solutions won't be pretty, but they will work

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

separator = '   '

columnA = []
columnB = []

with open(os.path.join(__location__, 'inputs.tsv')) as tsv:
    for line in tsv:
        content = line.split(separator)
        columnA.append(int(content[0]))
        columnB.append(int(content[1]))

columnA.sort() # lol
columnB.sort()

total_distance = 0

for idx, a_value in enumerate(columnA):
    # Get the diff between value in col A, col B, add to total distance
    total_distance += abs(a_value - columnB[idx])

print("Total Distance: " + str(total_distance)) # 1110981