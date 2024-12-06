import functools

def partOne(data: list) -> int:
    #split the input on the empty '' delimiter to separate the rules and pages
    rules, pages = data[:data.index('')], data[data.index('')+1:]
    
    #The goal of this puzzle is to identify which arrays of page numbers are in the correct order according to the rules
    #Once we've made this determination, we need to grab the middle element of each list and add them up to get the answer
    
    #For each list, we need to get all relevant rules to the numbers in said list
    
    #Then, iterate through the page numbers
    #for each number, get its applicable rules using the left number
    #check the list for the position and index of each number
    #does it exist? If so, ensure that the index of x < y (to ensure it occurs earlier in the list)
    #if this condition returns false, then the list isn't valid and we should not add it to our iterator
    
    middlePageNumberSum = 0
    
    for page in pages:
        # integers = [int(num) for num in page.split(",")]
        integers = page.split(",")
        
        flag = False
        for rule in rules:
            x, y = rule.split("|")
            if {x, y}.issubset(integers):
                if integers.index(y) > integers.index(x):
                    print("rule working", rule, integers)
                    
                else:
                    print("vibes were off", rule, integers)
                    flag = True
                    break
        
        if (flag):
            flag = False
        else:
            flag = False
            middlePageNumberSum += int(integers[len(integers) // 2])
            
    return middlePageNumberSum

def partTwo(data):
    rules, pages = data[:data.index('')], data[data.index('')+1:]
    
    middlePageNumberSum = 0
    rule_pairs = [tuple(map(int, rule.split("|"))) for rule in rules]
    
    #adjust incorrect lists based on our rules
    def compare(a, b):
        for x, y in rule_pairs:
            if a == x and b == y:
                return -1
            if a == y and b == x:
                return 1
        return 0
    
    for page in pages:
        integers = page.split(",")
        
        is_incorrect = False
        for rule in rules:
            x, y = rule.split("|")
            if {x, y}.issubset(integers):
                if integers.index(y) > integers.index(x):
                    continue
                else:
                    is_incorrect = True
                    break
        
        if is_incorrect:
            int_list = [int(num) for num in integers]
            sorted_list = sorted(int_list, key=functools.cmp_to_key(compare))
            
            #did this work                
            for x, y in rule_pairs:
                if x in sorted_list and y in sorted_list:
                    if sorted_list.index(x) > sorted_list.index(y):
                       print(f"big oof {int_list}")
            
            middlePageNumberSum += sorted_list[len(sorted_list) // 2]
    
    return middlePageNumberSum
    

    

if __name__ == "__main__":

    with open("inputs/day05.txt") as f:
        data = f.read().splitlines()
    
        print("Part 1:", partOne(data))
        print("Part 2:", partTwo(data))