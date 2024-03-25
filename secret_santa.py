from random import randint, sample

def check_fisher_yates_accuracy(drawn_map: dict): 
    count = 0
    for key, value in drawn_map.items():
        if drawn_map[value] == key:
            count += 1 
    return count

def fisher_yates_shuffle(n: int):
    members_list = sample(range(n), n)
    for i in range(n - 1, 0, -1):
        j = randint(0, i) 
        members_list[i], members_list[j] = members_list[j], members_list[i]
    return members_list

if __name__ == "__main__":
    drawn_map = {}
    n = 1000
    members_list = fisher_yates_shuffle(n)
    for i in range(len(members_list)):
        drawn_map[members_list[i]] = members_list[(i + 1) % len(members_list)]
    
    result = check_fisher_yates_accuracy(drawn_map)
    print(result)
    