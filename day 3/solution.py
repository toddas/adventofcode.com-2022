import string

lower_case = [letters for letters in string.ascii_lowercase]
upper_case = [letters for letters in string.ascii_uppercase]


def find_badges(list_of_group_dic):
    unique_list = []
    badges_list = []
    for items in list_of_group_dic:
        for lett in items[1]:
            if lett not in unique_list:
                unique_list.append(lett)

        for lett in unique_list:

            if lett in items[2] and lett in items[3]:
                    badges_list.append(lett)
        unique_list = []

    return badges_list

def split_to_groups(list_of_rutsacks):
    all_groups_dic = {}
    list_of_groups = []
    count = 1
    for item in range(len(list_of_rutsacks)):
        if count <= 3:
            all_groups_dic[count] = list_of_rutsacks[item].strip('\n')
            count += 1
        if count > 3:
            list_of_groups.append(all_groups_dic.copy())
            all_groups_dic.clear()
            count = 1

    return list_of_groups

def split_rutsack(rutsack):
    list_of_same_items = []
    length = len(rutsack)
    compartment1 = rutsack[:length // 2]
    compartment2 = rutsack[length // 2:]
    list_of_items = [compartment1, compartment2]
    for lett in list_of_items[0]:
        if lett in list_of_items[1]:
            if lett not in list_of_same_items:
                list_of_same_items.append(lett)

    return list_of_same_items

def determine_priority(item_list):
    score = 0
    score_lt = 0
    for lett in item_list:
        if lett.isupper() == True:
            score_lt = int(upper_case.index(lett)) + 27
        if lett.isupper() == False:
            score_lt = int(lower_case.index(lett)) + 1
    score = score + score_lt
    return score

def main():
    score = 0
    file = open('input', 'r')
    list_of_rutsacks = file.readlines()
    list_of_group_dic = split_to_groups(list_of_rutsacks)
    badges_list = find_badges(list_of_group_dic)

    #part1
    # for rutsack in list_of_rutsacks:
    #     same_item_list = split_rutsack(rutsack)
    #     score += determine_priority(same_item_list)

    #part2
    for badge in badges_list:
        score = determine_priority(badge) + score


    print(score)

if __name__ == '__main__':
    main()
