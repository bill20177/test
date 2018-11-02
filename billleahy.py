

while True:
    player1= raw_input ("choose rock paper scissor\n")
    player2= raw_input ("choose rock paper scissor\n")
    spellck = True

    while spellck:
        if player1  == "rock":
            spellck= False
        elif player1  == "scissor":
            spellck= False
        elif player1  == "paper":
            spellck= False
        else:
            player1 = raw_input ("check your spelling yo")
    spellck = True
    while spellck:
        if player2 == "rock":
            spellck = False
        elif player2 == "scissor":
            spellck = False
        elif player2 == "paper":
            spellck = False
        else:
            player2 = raw_input("check your spelling yo")

    if player1 == "rock" and player2 == "scissor" :
        print ("player1 wins")
    elif player1 == "paper" and player2 == "rock":
        print ("player1 wins")
    elif player1 == "scissor" and player2 == "paper":
        print ("player1 wins")
    elif player1==player2:
        print ("tie")
    else :
        print ("player2 wins")







