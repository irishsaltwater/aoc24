import os
import numpy
import copy
from collections import defaultdict

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


def part_two():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

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
    # the coordinates of each of the unique locations that an obstruction can be placed
    unique_location_y_x = []
    while True:
        # record unique locations
        current_info = map_array[current_location[0]][current_location[1]] 
        if current_info != location_marker:
            unique_locations +=1
            map_array[current_location[0]][current_location[1]] = location_marker
            unique_location_y_x.append(current_location)

        

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
    # Remove the starting position from possible obstacle locations
    unique_location_y_x.pop(unique_location_y_x.index(starting_position))
    print("Map traversed") # Now have recording of each possible location that obstacle could exist on
    print("unqiue locations : " + str(len(unique_location_y_x)) + " expected 1 less than: " + str(unique_locations))

    # for each unique location
    # build copy of map with obstruction in that location
    obstruction_marker = 'O'

    possible_obstruction_locations_count = 0
    print("Total variants: " + str(len(unique_location_y_x)))

    # otherwise, tracking loop, keep map of all movements, identify when segment increasing by 2?
    # am I making this far too complex?
    # if hit ANY location more than once facing in same direction, must be in loop
    for counter, obs_loc_yx in enumerate(unique_location_y_x):
        print("Testing variant: " + str(counter+1))
        map_variant = copy.deepcopy(map_array)
        map_variant[obs_loc_yx[0]][obs_loc_yx[1]] = obstruction_marker

        # Simulate guard walking through new map
        # if guard hits same side of obstruction twice, know is in loop
        # otherwise eventually guard will go out of bounds, know obstruction location no good
        # key: movement direction, 0
        loop_loc_counter = defaultdict(int)
        #obstruction_hit_counter[current_step_direction] +=1

        current_location = starting_position
        current_step_direction = up
        variant_step_count = 0
        while True:
            current_info = map_variant[current_location[0]][current_location[1]] 

            # removed check for unique location

            next_location = numpy.add(current_location, current_step_direction)
            
            # Assert next location not out of bounds
            if next_location[0] < 0 or next_location[0] >= len(map_variant):
                break
            if next_location[1] < 0 or next_location[1] >= x_max:
                break

            if map_variant[next_location[0]][next_location[1]]  == obstacle_marker or map_variant[next_location[0]][next_location[1]]  == obstruction_marker:
                current_step_direction = calc_new_direction(current_step_direction)
                continue

            # No obstacle, everything fine, update location
            current_location = next_location
            # If actually moving, record new location with counter
            place_key = str(current_location) + str(current_step_direction)
            loop_loc_counter[place_key] +=1

            if loop_loc_counter[place_key] == 2:
                # If been here twice, in loop
                possible_obstruction_locations_count += 1
                break # no need to continue, try next obstacle location
    
    print("All variants attempted, possible obstruction location count: " + str(possible_obstruction_locations_count)) # 1443

def part_one():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
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

#part_one()
part_two()