import os

# 8 days behind, these solutions won't be pretty, but they will work

def part_one():
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

def part_two():
    # find how often number from A appears in B
    # multiply A by that amount, add up all numbers

    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    separator = '   '

    column_a = []
    # number, count of times appear
    column_b_dict = {}

    with open(os.path.join(__location__, 'inputs.tsv')) as tsv:
        for line in tsv:
            content = line.split(separator)
            column_a.append(int(content[0]))
            column_b_number = int(content[1])
            
            if not column_b_number in column_b_dict:
                column_b_dict[column_b_number] = 1
            else:
                column_b_dict[column_b_number] += 1

    # Now have A, plus dict for B containing number, number of times occurs

    similarity_score = 0

    for a_value in column_a:
        # Find if A exists in B, get count and multiply
        multiplier = column_b_dict.get(a_value, 0)
        similarity_score += (a_value * multiplier)

    print("Similarity Score: " + str(similarity_score))

part_two() # 24869388