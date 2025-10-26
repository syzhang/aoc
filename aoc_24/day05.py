"""
day 5
"""
from aocd import get_data
data = get_data(year=2024, day=5)

# part 1
input = data
rules, updates = input.split('\n\n')
rules = rules.split('\n')
updates = updates.split('\n')

valids = []
for update in updates:
    update_list = update.split(',')
    update_set = set(update_list)
    is_valid = True
    for rule in rules:
        num1, num2 = rule.split('|')
        if (num1 in update_set and num2 in update_set):
            pos1 = update_list.index(num1)
            pos2 = update_list.index(num2)
            if pos1 > pos2:
                is_valid = False
                break
    if is_valid:
        valids.append(update)

valid_mids = []
for valid in valids:
    v = valid.split(',')
    m = v[len(v)//2]
    valid_mids.append(int(m))

final = sum(valid_mids)
print(final)

# part 2
incorrects = []
for update in updates:
    update_list = update.split(',')
    update_set = set(update_list)
    is_incorrect = False
    for rule in rules:
        num1, num2 = rule.split('|')
        if (num1 in update_set and num2 in update_set):
            pos1 = update_list.index(num1)
            pos2 = update_list.index(num2)
            if pos1 > pos2:
                is_incorrect = True
                break
    if is_incorrect:
        incorrects.append(update)

corrected = []
for incorrect in incorrects:
    update_list = incorrect.split(',')
    update_set = set(update_list)
    
    has_violations = True
    while has_violations:
        has_violations = False
        for rule in rules:
            num1, num2 = rule.split('|')
            if (num1 in update_set and num2 in update_set):
                pos1 = update_list.index(num1)
                pos2 = update_list.index(num2)
                if pos1 > pos2:
                    update_list[pos1] = num2
                    update_list[pos2] = num1
                    has_violations = True
    
    corrected.append(update_list)

corrected_mids = []
for c in corrected:
    m = c[len(c)//2]
    corrected_mids.append(int(m))

final = sum(corrected_mids)
print(final)