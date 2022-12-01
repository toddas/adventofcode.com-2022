rations = []
total_unsorted = []

# https://www.geeksforgeeks.org/python-program-to-find-n-largest-elements-from-a-list/
def Nmaxelements(list1, N):
    final_list = []

    for i in range(0, N):
        max1 = 0

        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j];

        list1.remove(max1);
        final_list.append(max1)

    return (final_list)


def main():
    total_list = 0
    file = open('input', 'r')
    input_string = file.readlines()
    for symbol in input_string:
        if symbol != '\n':
            symbol = symbol.strip('\n')
            rations.append(symbol)
        if symbol == '\n':
            for kal in range(0, len(rations)):
                total_list = total_list + int(rations[kal])
            total_unsorted.append(total_list)
            total_list = 0
            rations.clear()
    top3 = Nmaxelements(total_unsorted, 3)
    top3_total = 0
    for numb in top3:
        top3_total += numb
    print(top3)
    print(top3_total)
    file.close()


if __name__ == '__main__':
    main()
