def minion_game(string):
    # your code goes here
    string=string.upper()
    l=len(string)
    vowels='AEIOU'
        
    Kevin=0
    Stuart=0

    for i in range(l):
        if string[i] in vowels:
            Kevin+=(l-i)
        else:
            Stuart+=(l-i) 

    if Kevin > Stuart:
        print('Kevin',Kevin)
    elif Stuart > Kevin:
        print('Stuart',Stuart)
    else:
        print('Draw')

