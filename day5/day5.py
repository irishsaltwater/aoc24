import os
import csv
import math


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

part_one()