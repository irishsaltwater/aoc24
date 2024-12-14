import os
import numpy

up = (-1, 0)
right = (0, 1)
down = (1, 0)
left = (0, -1)

def calc_new_direction(current_direction):
    if current_direction == up:
        return right
    if current_direction == right:
        return down
    if current_direction == down:
        return left
    if current_direction == left:
        return up


def part_one():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    rules_dict = {} # Page, [Pages that must be after it]

    # build rules dict
    # for each number in line, assert that numbers before it are not in dict
    map_array = []
    location_marker = 'x'
    obstacle_marker = '#'

    x_max = 0
    
    # y, x
    starting_position = (0,0)


    turn_direction_order = [up, right, down, left]
    
    with open(os.path.join(__location__, 'input.txt')) as map_input:
        for y, line in enumerate(map_input):
            current_line = list(line)
            map_array.append(current_line)
            # check for starting position as iterating
            if '^' in current_line:
                print("Found starting location")
                starting_position = (y, current_line.index('^'))
            # mark the maximum size of X, bit of a lazy cheat, know all lines same length
            if len(current_line) > x_max:
                x_max = len(current_line)

    print("Map built")

    # figure out step direction based on <>v^ (so will get 0,1, -1,0 etc)

    # make current location x
    # determine direction
    # modify location by tuple math
    # if new location contains #, instead of moving, just rotate
    # if new location out of bounds, break loop
    current_location = starting_position
    current_step_direction = up # cheating a bit, know starting direction is ^

    unique_locations = 0
    while True:
        # Mark current place with X
        current_info = map_array[current_location[0]][current_location[1]] 
        if current_info != location_marker:
            unique_locations +=1
            map_array[current_location[0]][current_location[1]] = location_marker

        

        next_location = numpy.add(current_location, current_step_direction)
        
        # Assert next location not out of bounds
        if next_location[0] < 0 or next_location[0] > len(map_array):
            break
        if next_location[1] < 1 or next_location[1] > x_max:
            break

        if map_array[next_location[0]][next_location[1]]  == obstacle_marker:
            current_step_direction = calc_new_direction(current_step_direction)
            continue

        # No obstacle, everything fine, update location
        current_location = next_location

    print("Map traversed, unique locations: " + str(unique_locations)) # 4696

part_one()