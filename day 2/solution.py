#A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.
#The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.
# #Winning every time would be suspicious, so the responses must have been carefully chosen.
#(1 for Rock(X, A), 2 for Paper(Y B), and 3 for Scissors(Z C))
#(0 if you lost, 3 if the round was a draw, and 6 if you won)
def fight_part1(list_of_moves):
    score = 0
    oponent = 0
    you = 0
    print('--')
    print(list_of_moves)
    print('==')
    for moves in list_of_moves:
        if 'X' in moves: #Rock
            you = 1
            print('you got Rock')
        if 'Y' in moves: #Paper
            you = 2
            print('you got Paper')
        if 'Z' in moves: #Scissors
            you = 3
            print('you got Scissors')
        if 'A' in moves: #Rock
            oponent = 1
            print('oponnent got Rock')
        if 'B' in moves: #Paper
            oponent = 2
            print('oponnent got Paper')
        if 'C' in moves: #Scissors
            oponent = 3
            print('oponnent got Scissors')

    if you == 1 and oponent == 3: #2
        print('you won')
        score = (you + 6)
    if you == 1 and oponent == 2: #1
        print('you lost')
        score = you
    if you == 1 and oponent == 1: #0
        print('you draw')
        score = (you + 3)

    if you == 2 and oponent == 3: #1
        print('you lost')
        score = you
    if you == 2 and oponent == 2: #0
        print('you draw')
        score = (you + 3)
    if you == 2 and oponent == 1: #-1
        print('you won')
        score = (you + 6)

    if you == 3 and oponent == 3: #0
        print('you draw')
        score =(you + 3)
    if you == 3 and oponent == 2: #-1
        print('you won')
        score = (you + 6)
    if you == 3 and oponent == 1:#-2
        print('you lost')
        score = you

    print(str(score))
    print('--')
    return score

def fight_part2(list_of_moves):
    match = ''
    score = 0
    oponent = 0
    you = 0
    print('--')
    print(list_of_moves)
    print('==')
    for moves in list_of_moves:
        if 'X' in moves: #Rock
            match = 'L'
            print('you need to lose')
        if 'Y' in moves: #Paper
            match = 'D'
            print('you need to draw')
        if 'Z' in moves: #Scissors
            match = 'W'
            print('you need to win')
        if 'A' in moves: #Rock
            oponent = 1
            print('oponnent got Rock')
        if 'B' in moves: #Paper
            oponent = 2
            print('oponnent got Paper')
        if 'C' in moves: #Scissors
            oponent = 3
            print('oponnent got Scissors')

        if match == 'L' and oponent == 1:
            you = 3
            score = you
        if match == 'L' and oponent == 2:
            you = 1
            score = you
        if match == 'L' and oponent == 3:
            you = 2
            score = you
        if match == 'D' and oponent == 1:
            you = 1
            score = you + 3
        if match == 'D' and oponent == 2:
            you = 2
            score = you + 3
        if match == 'D' and oponent == 3:
            you = 3
            score = you + 3
        if match == 'W' and oponent == 1:
            you = 2
            score = you + 6
        if match == 'W' and oponent == 2:
            you = 3
            score = you + 6
        if match == 'W' and oponent == 3:
            you = 1
            score = you + 6
    print('you: '+str(you))
    print('oponent: '+str(oponent))
    print(str(score))
    print('--')
    return score

def main():
    points = []
    strategies = open('input', 'r')
    strategies = strategies.readlines()
    for strat in strategies:
        splited = strat.split()
        print(splited)
        score = fight_part2(splited)
        points.append(score)
    print(sum(points))
if __name__ == '__main__':
    main()