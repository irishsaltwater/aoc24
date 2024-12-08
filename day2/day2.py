import os
import csv

input_location = 'input.csv'

def part_one():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    total_reports = 0

    safe_reports = 0
    unsafe_reports = 0
    
    with open(os.path.join(__location__, input_location)) as input:
        filereader = csv.reader(input, quoting = csv.QUOTE_NONNUMERIC, delimiter=" ")
        
        # for each report, step through, determine if diff between two adjacent numbers is within safety
        # AND assert that each report only ever increases or decreases
        
        safety_min = 1
        safety_max = 3
        for row in filereader:
            total_reports += 1
            # determine if report increasing or decreasing
            diff_modifier = None

            initial_diff = row[0] - row[1]

            if initial_diff == 0:
                # Report not increasing or decreasing, unsafe
                unsafe_reports += 1
                continue
            elif initial_diff > 0:
                # decreasing
                diff_modifier = 1
            else:
                diff_modifier = -1

            # definitely smarter way to do above, but again, way behind

            # iterate through row
            for i, value in enumerate(row):
                # diff should always be positive, if not, going in wrong direction
            
                # Current number - Next number. If always expect decrease, mult by 1, otherwise by -1 
                diff = (row[i] - row[i+1]) * diff_modifier
                safe = diff <= safety_max and diff >= safety_min
                if not safe:
                    # Unsafe, can also stop checking this row
                    unsafe_reports += 1
                    break
                # If at second last number, and its safe, record as safe, and break
                if i == len(row)-2 and safe:
                    safe_reports +=1
                    break

    print("Safe reports: " + str(safe_reports)) # 269
    print("Unsafe reports: " + str(unsafe_reports)) # 731

# returns true if list is safe
def safe_checker(row: list, safety_min: int, safety_max: int) -> bool:
    # determine if report increasing or decreasing
    diff_modifier = None

    initial_diff = row[0] - row[1]

    if initial_diff == 0:
        # Report not increasing or decreasing, unsafe
        return False
    elif initial_diff > 0:
        # decreasing
        diff_modifier = 1
    else:
        diff_modifier = -1

    # iterate through row
    i = 0
    end = len(row)
    while i < end:
        diff = (row[i] - row[i+1]) * diff_modifier
        safe = diff <= safety_max and diff >= safety_min
        if not safe:
            # Unsafe, can also stop checking this row
            # If line is unsafe just....ugh, lol. brute force it
            # Try every variant of line with 0, 1, 2 etc index removed.
            return False
        # If at second last number, and its safe, record as safe, and break
        if i == len(row)-2 and safe:
            return True
        i += 1

def part_two():
    # problem dampener
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    total_reports = 0

    safe_reports = 0
    unsafe_reports = 0
    
    with open(os.path.join(__location__, input_location)) as input:
        filereader = csv.reader(input, quoting = csv.QUOTE_NONNUMERIC, delimiter=" ")
        
        # for each report, step through, determine if diff between two adjacent numbers is within safety
        # AND assert that each report only ever increases or decreases
        
        safety_min = 1
        safety_max = 3
        for row in filereader:
            total_reports += 1
            is_safe = safe_checker(row, safety_min, safety_max)
            if is_safe:
                safe_reports += 1
            else:
                # Brute force, try every variant of list with one value removed
                end = len(row)
                to_remove = 0
                result = False

                while to_remove < end:
                    modified_row = row[:]
                    del modified_row[to_remove]
                    result = safe_checker(modified_row, safety_min, safety_max)
                    if result:
                        break # no need to check further variants
                    to_remove += 1

                if result:
                    safe_reports += 1
                else:
                    unsafe_reports +=1
    

    print("Safe reports: " + str(safe_reports)) # 337
    print("Unsafe reports: " + str(unsafe_reports)) # 663


# part_one()
part_two()

"""
## # If dampener enabled, remove next element, try again, only once per row
                    if problem_dampener_enabled:
                        # figure out
                        # either this - i+2
                        # or i-1 - i+1 (exclude this) are within range
                        ## verify not at start or end

                        # Check if removing current i resolves
                        if i > 0 and i < end-2: # not at first or last items
                            alt_diff = row[i-1] - row[i+1]
                            alt_safe = alt_diff <= safety_max and diff >= safety_min
                            # if safe, remove current
                        elif i == end - 2: # if at last number, and that causes error, just remove it
                            safe_reports +=1
                            break
                        elif i == 0: # if at very start, then could remove i or i+1
                            # see if i + i + 2 is safe
                            # removing very first one causes issue, need to recalculate if increase/decrease
                 """           
        