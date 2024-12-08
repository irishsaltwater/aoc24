import os
import re

def parse_multiplication(command: str) -> int:
    # Extract first and second set of digits
    regex = '[0-9]{1,3}'
    numbers = re.findall(regex, command)
    return int(numbers[0]) * int(numbers[1])

def part_one():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    regex = 'mul\([0-9]{1,3},[0-9]{1,3}\)' # finds mul(1-3digits,1-3digits)
    
    matches = []

    with open(os.path.join(__location__, 'inputs.csv')) as input:
        for line in input:
            matches += re.findall(regex, line)
    print("Matches found, size: " + str(len(matches)))

    # Parse each command
    total_result = 0

    for command in matches:
        total_result += parse_multiplication(command)

    print("Result: " + str(total_result))

def part_two():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    # do() - start taking account of muls after that
    # don't() - ignore following muls until do

    # so, ah- if going through input in order, just append in order
    # match mul, or do or don't

    # then when iterating, step each one, either calc, or flip boolean if do or dont
    do_raw= "do()"
    dont_raw = "don't()"
    do_regex = 'do\(\)'
    dont_regex = "don't\(\)"
    command_regex = 'mul\([0-9]{1,3},[0-9]{1,3}\)' # finds mul(1-3digits,1-3digits)
    
    full_regex = do_regex + '|' + dont_regex + '|' + command_regex

    matches = []

    with open(os.path.join(__location__, 'inputs.csv')) as input:
        for line in input:
            matches += re.findall(full_regex, line)
    print("Matches found, size: " + str(len(matches)))

    # Parse each command
    total_result = 0
    
    enabled = True

    for command in matches:
        if command == do_raw:
            enabled = True
        elif command == dont_raw:
            enabled = False
        elif enabled: # At this point, know command is a multiplication
            total_result += parse_multiplication(command)

    print("Result: " + str(total_result))

# part_one() # 178886550
# part_two() # 87163705