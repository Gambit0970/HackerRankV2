def minion_game(string):
    vowels = 'AEIOU'
    Stuart = 0
    Kevin = 0
    for i,letter in enumerate(string):
        if letter in vowels:
            Kevin += len(range(i,len(string)))
        else:
            Stuart += len(range(i,len(string)))
    if Kevin > Stuart:
        print(f"Kevin {Kevin}")
    elif Stuart > Kevin:
        print(f"Stuart {Stuart}")        
    else:
        print("Draw")

