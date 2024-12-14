import os
import csv
import math
import itertools
import threading
import numpy

def check_pages_in_rules(pages, rules) -> bool:
    # if any page exist in rules, return true,
    # otherwise return false

    for page in pages:
        for rule in rules:
            if page == rule:
                # A page that is only allowed after the page under test exists before it
                return True
            
    return False

def part_one():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    rules_dict = {} # Page, [Pages that must be after it]

    # build rules dict
    # for each number in line, assert that numbers before it are not in dict

    with open(os.path.join(__location__, 'rules.txt')) as input:
        filereader = csv.reader(input, quoting = csv.QUOTE_NONNUMERIC, delimiter="|")
        for rule in filereader:

            key = rule[0]
            allowed_page = rule[1]

            if key not in rules_dict:
                rules_dict[key] = [allowed_page]
            else:
                rules_dict[key].append(allowed_page)

    print("Rules built")
    
    correct_update_middle_page_totals= 0
    
    total_update_count = 0
    safe_updates = 0
    unsafe_updates = 0

    with open(os.path.join(__location__, 'input.txt')) as input:
        filereader = csv.reader(input, quoting = csv.QUOTE_NONNUMERIC, delimiter=",")
        for update in filereader:
            total_update_count += 1
            # Check the update, for each number, assert that the numbers behind it aren't in the rule dict
            # This is definitely inefficient from a code perspective, but NOT ineffecient from a brain perspective
            for index, page_number in enumerate(update):
                if index == 0:
                    continue # Nothing to check behind first page
                if page_number in rules_dict:
                    # Assert none of the prior pages are in the rules
                    prior_page_in_rules = check_pages_in_rules(update[:index-1], rules_dict[page_number])
                    #all(rule in rules_dict[page_number] for prior_page in update[:index-1])
                    if prior_page_in_rules:
                        unsafe_updates += 1
                        break # Update line is incorrect, no need to check rest of it
                
                # update is valid, grab the middle page number
                # If at last element, record it, otherwise just continue to next 
                if index == len(update) - 1:
                    safe_updates += 1
                    correct_update_middle_page_totals += update[(math.ceil((len(update)-1)/2))]
    
    print("Total updates: " + str(total_update_count))
    print("Safe updates:" + str(safe_updates))
    print("Unsafe updates: " + str(unsafe_updates))      
    print("Total of correct update middle page values: " + str(correct_update_middle_page_totals)) # 7307

def terrible_impl(incorrect_updates, rules_dict) -> int:
    fixed_updates_middle_sum = 0
    for unsafe_update in incorrect_updates:
        # print("creating combinations size " + str(len(unsafe_update)))
        possible_combinations = itertools.permutations(unsafe_update, len(unsafe_update)) # lmao
        combi_found = False
        for loop, combi in enumerate(possible_combinations):
            #print(loop)
            if combi_found:
                break # Correct combination has been found for this update, do not continue checking
            # Check to see if this adheres to the rules
            for index, page_number in enumerate(combi):
                if index == 0:
                    continue # Nothing to check behind first page
                if page_number in rules_dict:
                    # Assert none of the prior pages are in the rules
                    prior_page_in_rules = check_pages_in_rules(combi[:index-1], rules_dict[page_number])
                    #all(rule in rules_dict[page_number] for prior_page in update[:index-1])
                    if prior_page_in_rules:
                        break # Update line is incorrect, no need to check rest of it
                
                # update is valid, grab the middle page number
                # If at last element, record it, otherwise just continue to next 
                if index == len(combi) - 1:
                    print("found")
                    fixed_updates_middle_sum += combi[(math.ceil((len(combi)-1)/2))]
                    combi_found = True # dont check additional combinations
    return fixed_updates_middle_sum

def split_array(array, count):
    array_length = len(array)
    segment_size = array_length/count
    response_array = []
    for i in range(0, array_length, count):
        yield array[i:i+count]
        




def part_two():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    rules_dict = {} # Page, [Pages that must be after it]

    # build rules dict
    # for each number in line, assert that numbers before it are not in dict

    with open(os.path.join(__location__, 'rules.txt')) as input:
        filereader = csv.reader(input, quoting = csv.QUOTE_NONNUMERIC, delimiter="|")
        for rule in filereader:

            key = rule[0]
            allowed_page = rule[1]

            if key not in rules_dict:
                rules_dict[key] = [allowed_page]
            else:
                rules_dict[key].append(allowed_page)

    print("Rules built")

    incorrect_updates = []

    with open(os.path.join(__location__, 'input.txt')) as input:
        filereader = csv.reader(input, quoting = csv.QUOTE_NONNUMERIC, delimiter=",")
        for update in filereader:
            # Check the update, for each number, assert that the numbers behind it aren't in the rule dict
            # This is definitely inefficient from a code perspective, but NOT ineffecient from a brain perspective
            for index, page_number in enumerate(update):
                if index == 0:
                    continue # Nothing to check behind first page
                if page_number in rules_dict:
                    # Assert none of the prior pages are in the rules
                    prior_page_in_rules = check_pages_in_rules(update[:index-1], rules_dict[page_number])
                    #all(rule in rules_dict[page_number] for prior_page in update[:index-1])
                    if prior_page_in_rules:
                        incorrect_updates.append(update)
                        break # Update line is incorrect, no need to check rest of it

    # fix incorrect updates
    print("Resolving incorrect updates")
    print("Unsafe update count: " + str(len(incorrect_updates))) # expect 82
    
    fixed_updates_middle_sum = 0

    split_incorrect_updates = split_array(incorrect_updates, 20)

    threads = []
    for split in split_incorrect_updates:
        threads.append(threading.Thread(target=terrible_impl, args=(split, rules_dict)))

    for t in threads:
        t.start()

    for t in threads:
        fixed_updates_middle_sum += t.join() 
    
    print("Fixed updates middle sum: " + str(fixed_updates_middle_sum))
    
    
def part_two_actual():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    rules_dict = {} # Page, [Pages that must be after it]

    # build rules dict
    # for each number in line, assert that numbers before it are not in dict

    with open(os.path.join(__location__, 'rules.txt')) as input:
        filereader = csv.reader(input, quoting = csv.QUOTE_NONNUMERIC, delimiter="|")
        for rule in filereader:

            key = rule[0]
            allowed_page = rule[1]

            if key not in rules_dict:
                rules_dict[key] = [allowed_page]
            else:
                rules_dict[key].append(allowed_page)

    print("Rules built")

    incorrect_updates = []
    updates_made = 0

    with open(os.path.join(__location__, 'input.txt')) as input:
        filereader = csv.reader(input, quoting = csv.QUOTE_NONNUMERIC, delimiter=",")
        for update in filereader:
            # Check the update, for each number, assert that the numbers behind it aren't in the rule dict
            # This is definitely inefficient from a code perspective, but NOT ineffecient from a brain perspective
            for index, page_number in enumerate(update):
                if index == 0:
                    continue # Nothing to check behind first page
                if page_number in rules_dict:
                    # Assert none of the prior pages are in the rules
                    prior_page_in_rules = check_pages_in_rules(update[:index-1], rules_dict[page_number])
                    #all(rule in rules_dict[page_number] for prior_page in update[:index-1])
                    if prior_page_in_rules:
                        incorrect_updates.append(update)
                        break # Update line is incorrect, no need to check rest of it

    # fix incorrect updates
    print("Resolving incorrect updates")
    print("Unsafe update count: " + str(len(incorrect_updates))) # expect 82
    
    fixed_updates_middle_sum = 0

    for unsafe_update in incorrect_updates:
        response_array = unsafe_update.copy()
        for i, page in enumerate(unsafe_update):
            # Check that rules for current page are adhered to in response array
            # if not, find left-most rule page in response array, move current to before it
            rules_current_page = rules_dict[page]
            # any numbers in rules exist from start:i?
            for j, other_page in enumerate(unsafe_update[:i]):
                if other_page in rules_current_page:
                    # found first page that should be ahead of current page
                    print("Found first page that needs to be in front")
                    print("array before: ")
                    print(response_array)

                    response_array.insert(j, response_array.pop(i)) # order for this page now fixed
                    # no need to continue checking the rules for this specific page
                    print("array after: ")
                    print(response_array)
                    #[32.0, 99.0, 27.0, 62.0, 48.0, 64.0, 46.0, 98.0, 14.0]
                    # problem: what if 98 needs 14 ahead, but 14 needs to be behind 32?
                    # can't just look at what needs to be in front
                    # ok, so, rules_dict contains everything that has to be in front
                    # inverted, everything else not in that needs to be behind
                    break

            # if at last index, then find middle sum
            if i == len(unsafe_update) - 1:
                updates_made+=1
                fixed_updates_middle_sum += response_array[(math.ceil((len(response_array)-1)/2))]
    
    print("Updates made:" + str(updates_made))
    print("Fixed updates middle sum: " + str(fixed_updates_middle_sum))
    
    
#part_one()
#part_two()
part_two_actual()