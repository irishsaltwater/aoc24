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

part_one()