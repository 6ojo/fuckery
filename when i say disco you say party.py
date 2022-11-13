import time

def repeat():
    print('I say disco, you say party')
    time.sleep(1.8)
    print('disco')
    time.sleep(0.4)
    print('disco')
    user_input = input('\n')
    my_str = 'party party'
    if user_input == my_str:
        print('\n')
    else:
        print('Wrong.')
        time.sleep(3)
        print('do better next time')
        time.sleep(2)
    return user_input, my_str
    
for i in range(2):
   user_input, my_str=repeat()


if user_input == my_str:
    print('SOLO!')
    time.sleep(2.3)
    print('fantastic!')
    time.sleep(1.2)
    print('applause!')
    time.sleep(0.4)
    print('you hear raging applause')
    
else:
    print('you missed your chance to solo')
