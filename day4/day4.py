import os
import numpy

# Coordinate moves
# y, x / up-down, side to side
# I'm sure there's a smarter way to do this
up_left = (-1, -1)
up = (-1, 0)
up_right = (-1, 1)
left = (0, -1)
right = (0, 1)
down_left = (1, -1)
down = (1, 0)
down_right = (1, 1)

directions = [up_left, up, up_right, left, right, down_left, down, down_right]

def part_one():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    word_search = []

    # build 2 array, brute traverse
    with open(os.path.join(__location__, 'input.txt')) as input:
        for line in input:
            word_search.append(list(line))

    print("Word search built")

    # For any word: lazy
    # Traverse till find first letter
    # Then step in one direction, check letter, if match for second, step in same direction, continue
    # step in next direction, etc, until all have been checked

    word = 'XMAS'

    word_count = 0

    for y, line in enumerate(word_search):
        for x, character in enumerate(line):
            if character == word[0]:
                # Check all directions for subsequent letters, only move in same direction 
                for direction in directions:
                    location_yx = (y,x)
                    for letter_index,part in enumerate(word[1:]):
                        # Step in a certain direction
                        location_yx = numpy.add(location_yx, direction)
                        
                        if location_yx[1] > (len(line) - 1) or location_yx[1] < 0:
                            # outside bounds, stop checking this direction
                            break
                        if location_yx[0] > (len(word_search) - 1) or location_yx[0] < 0:
                            # outside bounds, stop checking
                            break

                        # check if location contains current part
                        if word_search[location_yx[0]][location_yx[1]] == part:
                            # Found next letter

                            # If at last letter
                            if letter_index == len(word[1:]) - 1:
                               word_count += 1
                                # Search is finished, at last letter
                            # Otherwise found next letter, but need to keep searching
                        else:
                            # Didn't find part, stop searching this direction
                            break
                            
    print("Word found count: " + str(word_count)) # 2549

part_one()