from audioop import reverse


def reverse_result(theirs, result):
    translation = {
        'A': {
            'X': 'C', # lose
            'Y': 'A', # draw
            'Z': 'B', # win
        },
        'B': {
            'X': 'A', # lose
            'Y': 'B', # draw
            'Z': 'C', # win
            },
        'C': {
            'X': 'B', # lose
            'Y': 'C', # draw
            'Z': 'A', # win
            },
    }
    return translation[theirs][result]

def result(theirs, ours):
    translation = {
        'A':{
            'X': 3,
            'A': 3,
            'Y': 6,
            'B': 6,
            'Z': 0,
            'C': 0,
        },
        'B':{
            'X': 0,
            'A': 0,
            'Y': 3,
            'B': 3,
            'Z': 6,
            'C': 6,
        },
        'C':{
            'X': 6,
            'A': 6,
            'Y': 0,
            'B': 0,
            'Z': 3,
            'C': 3,
        },
    }
    return translation[theirs][ours]

def main():
    translation = {
        'values': {
            'A':1,
            'X':1,
            'B':2,
            'Y':2,
            'C':3,
            'Z':3,
        },
        'results': {
            'X': 'lose',
            'Y': 'draw',
            'Z': 'win',
        }
    }
    
    total = 0
    with open('day2\input.txt', 'r') as file:
        for line in file.readlines(): # full load
        # for line in file.readlines()[:20]: # sample load
            theirs, expected_result = line.strip('\n').split(' ');
            # theirs, ours = line.strip('\n').split(' ');
            # outcome = translation['values'][ours] + result(theirs, ours)
            played = reverse_result(theirs, expected_result)
            outcome = translation['values'][played] + result(theirs, played)
            total += outcome

            # print(f'theirs: {theirs} ours {played} expected {translation["results"][expected_result]} outcome: {outcome}')
            
            # print(f'theirs: {theirs} ours {ours} outcome: {outcome}')

    print(total)        


if __name__ == "__main__":
    main()