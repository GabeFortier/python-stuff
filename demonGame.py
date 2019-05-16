import random

direction = ['l','r']
lives = 5
turns = 0
grade ='\nYou realize too late you made the wrong choice as you run back you only find scattered remains.\nYou have seen enough carnage for one lifetime now.\nDuring your time hunting the demon you saved %d village(s).(Grade = %s)'

name = raw_input('Welcome hero. Your goal is to follow a demon and protect the residents of the\nvillages he seeks to destroy. Pray tell, what is your name? ')
print('\nWell %s, your journey begins...\nAs you walk down a path it forks, one direction follows the demon,\nthe other will delay you and result in the death of many.'% (name))
characters = {name:'','demon':''}
while lives > 0:
    characters['demon'] = random.choice(direction)
    characters[name] = raw_input('Which direction will you go?(type L or R)')
    if characters['demon'] == characters[name].lower():
        print('\nYou have saved a village! The demon is gone though, and you come to a new fork in the road...')
        turns += 1
    else:
        lives -= 1
        if lives > 0:
            print('\nYou realize too late you made the wrong choice as you run back you only find scattered remains,\nand another fork in the road...')   
        else:
            if turns < 6:
                print(grade%(turns,'F'))
            elif turns > 7 and turns < 10:
                print(grade%(turns,'D'))
            elif turns > 9 and turns < 12:
                print(grade%(turns,'C'))
            elif turns > 11 and turns < 15:
                print(grade%(turns,'B'))
            elif turns > 14 and turns < 20:
                print(grade%(turns,'A'))
            elif turns > 19:
                print(grade%(turns,'S'))