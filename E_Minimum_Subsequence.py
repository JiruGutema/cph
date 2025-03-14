def process_test_case():
    length = int(input())  
    binary_string = input()
    groups = []  
    group_map = {}  
    available = {'0': [], '1': []}  
    for index, char in enumerate(binary_string):
        if available[char]:  
            group_id = available[char].pop()
        else:
            group_id = len(groups) + 1
            groups.append([])
        groups[group_id - 1].append(index + 1)  
        group_map[index] = group_id
        available['1' if char == '0' else '0'].append(group_id)    
    print(len(groups))
    print(*[group_map[i] for i in range(length)])

test_cases = int(input())
for _ in range(test_cases):
    process_test_case()
