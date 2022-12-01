rations = []
total_unsorted = []


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
    print(max(total_unsorted))
    file.close()


if __name__ == '__main__':
    main()
