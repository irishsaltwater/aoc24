import os
import itertools

allowed_operations = '+*'

def generate_op_lists(size, operations):
    ops = list(operations)
    return list(itertools.product(ops, repeat=size))

def part_one():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    total_calibration_result = 0
    with open(os.path.join(__location__, 'input.txt')) as input:
        for line in input:
            row = line.strip()
            # split into sum and numbers
            split_line = row.split(':')
            
            sum = int(split_line[0])
            # Cheap hack to avoid first space
            numbers = list(map(int,split_line[1].split(' ')[1:]))

            # Determine if any possible variation of operators inserted can add to sum
            possible_operations = generate_op_lists(len(numbers)-1, allowed_operations)

            # loop through each operation
            # op 0 is applied between numbers[0] and numbers [1]
            for operation in possible_operations:
                # Check if the current operation variant will get the sum
                
                # Apply each operation
                running_total = numbers[0]
                for index, current_op in enumerate(operation):
                    
                    if current_op == '+':
                        running_total = running_total + numbers[index+1]
                    if current_op == '*':
                        running_total = running_total * numbers[index+1]
                
                # Have applied all operations in current set
                if running_total == sum:
                    total_calibration_result += running_total
                    break # no need to continue checking this line

    print("Complete, total of sums that can be fixed: " + str(total_calibration_result)) # 2437272016585 # lol, I assumed that was wrong and almost didn't check it



part_one()