from rock_paper_scissors import play

letter = False
gold_coin = False

name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")
answer = input("You are at a fork. Do you want to go left or right? ").lower()

if answer == "left":
    answer2 = input("You come across a bridge. You can either cross the bridge or go around. cross/go around: ").lower()

    if answer2 == 'cross':
        print('Suddenly you are confronted with a troll, he challenges you to a game of rock, paper, '
              + 'scissors. ')
        win = play()

        if not win:
            print("You have lost the most important game of rock, paper, scissors of your life. You are eaten by "
                  + "the troll.")
        elif win:
            item = input('The troll congratulates you on your win and offers you 3 items, '
                         'which do you choose? gold/sword/medicine ').lower()
            answer5 = input('You continue across the bridge and find a mountain, what do you do? '
                            ' climb it/go around/wait at the base ').lower()

            if answer5 == 'climb it':
                answer6 = input("You climb and climb until you reach the peak, you see a town in the distance. "
                                + 'What do you do? turn around/go to town ').lower()
                if answer6 == 'turn around':
                    print('You turn around and soon realize that you are lost, you wander the mountain for days until '
                          + 'you eventually run out of water and die. ')
                elif answer6 == 'go to town':
                    input('You eventually reach the town and upon arrival are surrounded by the town guard and ' +
                          "questioned about the whereabouts of a bandit, what do you say? haven't seen them/know them ")

                    print('The guards claim you are lying and throw you in jail, taking all of your belongings.')
                    if item == 'medicine':
                        answer7 = input('The guard asks you if you are a doctor, what do you say? yes/no ').lower()
                        if answer7 == 'yes':
                            print('You are freed from prison and become the town doctor. You live out the rest of your'
                                  + ' life treating the wounded and learning medicine on the job.')
                        elif answer7 == 'no':
                            print('The guard leaves you alone, you are forgotten in the jail cell and live out the rest'
                                  + ' of your life behind bars.')
                        else:
                            print('Not a valid option. You lose.')
                    else:
                        print('The guard leaves you alone, you are forgotten in the jail cell and live out the rest'
                              + ' of your life behind bars.')
                else:
                    print('Not a valid option. You lose.')

            elif answer5 == 'go around':
                answer6 = input("You are confronted with a bandit, he asks for everything you have or he will kill you."
                                'What do you do? refuse/give in/fight back ').lower()

                if answer6 == 'refuse':
                    print("The bandit attacks you, takes your belongings, and leaves you there to die.")
                elif answer6 == 'give in':
                    if item == 'gold':
                        print()
                    elif item == 'sword' or item == 'medicine':
                        print(f'The bandit takes your {item} and then kills you.')
                elif answer6 == 'fight back':
                    if item == 'sword':
                        print('You best the bandit with the help of your weapon and continue around the mountain.')
                        answer7 = (' You find yourself at a castle and meet the guard at the gate, what do you do?'
                                   'talk/fight ')
                        if answer7 == 'fight':
                            print('You find that this guard is a much better swordsman than the bandit, '
                                  + 'and you are bested in battle and left to die.')
                        elif answer7 == 'talk':
                            answer8 = input('The guard offers you a job, what do you do? take it/refuse ')
                            if answer8 == 'take it':
                                print('You live out the rest of your life protecting the castle fighting bandits '
                                      + 'slaying dragons.')
                            elif answer8 == 'refuse':
                                print('Archers appear from atop the walls of the castle and rain arrows down on you, '
                                      + 'you are dead.')
                            else:
                                print('Not a valid option. You lose.')

                    elif item == 'medicine' or item == 'gold':
                        print("You attempt to fight, but do to your lack of weapon the bandit gets the upper hand and"
                              + " you die")
                    else:
                        print('Not a valid option. You lose.')
                else:
                    print('Not a valid option. You lose.')
            elif answer5 == 'wait at the base':
                print('You wait at the base, falling asleep. You wake up to find a boulder barreling toward you. '
                      + 'You are squashed by the boulder and die.')
            else:
                print('Not a valid option. You lose.')
        else:
            print('Not a valid option. You lose.')

    elif answer2 == 'go around':
        answer3 = input("You come across a river, what do you do? swim/walk along bank ")
        if answer3 == 'swim':
            print('As you are swimming across, a crocodile appears and eats you whole. You are dead.')
        elif answer3 == 'walk along bank':
            answer4 = \
                input('You come across an old man, he asks you to help him, what do you do? help him/refuse ').lower()
            if answer4 == 'help him':
                answer5 = input('The man asks you to deliver a letter to his daughter for him, what do you do '
                                'agree/refuse ')
                if answer5 == 'agree':
                    print('You accept the letter and leave the old man.')
                    letter = True
                elif answer5 == 'refuse':
                    print('You leave the old man.')
                else:
                    print('Not a valid option. You lose.')

                answer6 = input('You continue walking along the bank, You are confronted with a bandit, he asks for'
                                + ' everything you have or he will kill you. What do you do? '
                                + 'refuse/give in/fight back ').lower()
                if answer6 == 'refuse' or answer6 == 'fight back':
                    print('The bandit overpowers you and kills you. You are dead.')
                elif answer6 == 'give in':
                    print('The bandit sees that you have nothing of value and lets you move along.')
                    answer7 = input('You continue walking and stumble upon a small cottage, what do you do?'
                                    + ' knock/walk in/continue walking ').lower()
                    if answer7 == 'continue walking':
                        answer8 = input('You continue walking and come across a castle the guard at the gate asks '
                                        'your name, what do you do? give name/refuse ').lower()
                        if answer8 == 'give name':
                            print('The guard mistakes you for a known criminal in the area and kills you on the spot.')
                        elif answer8 == 'refuse':
                            print('A row of archers appears from the wall of the castle and arrows rain down on you'
                                  ' You are dead.')
                        else:
                            print('Not a valid option. You lose.')
                    elif answer7 == 'knock':
                        answer8 = input("A beautiful woman answers the door and invites you in, what do you do? "
                                        "go inside/refuse ")
                        if answer8 == 'refuse':
                            print('You turn from the house and continue walking.')
                            answer9 = input('You continue walking and come across a castle the guard at the gate asks '
                                            'your name, what do you do? give name/refuse ').lower()
                            if answer9 == 'give name':
                                print(
                                    'The guard mistakes you for a known criminal in the area and '
                                    'kills you on the spot.')
                            elif answer9 == 'refuse':
                                print('A row of archers appears from the wall of the castle and arrows rain down on you'
                                      ' You are dead.')
                            else:
                                print('Not a valid option. You lose.')
                        elif answer8 == 'go inside':
                            print('You exchange pleasantries and then remember the old man and wonder if this '
                                  'could be his daughter')
                            if letter:
                                answer9 = input('You realize you have the letter, what do you do? give letter/'
                                                'ignore it ').lower()
                                if answer9 == 'give letter':
                                    answer10 = input('The woman begins to cry, she tells you that the letter explained '
                                                     'how kind you were to her father and that she should marry this '
                                                     'person if the letter ever reached her. What do you do? '
                                                     'propose/leave ').lower()
                                    if answer10 == 'propose':
                                        answer11 = input('The woman then laughs in your face explaining that the '
                                                         'letter was not intended for her and refuses your proposal. '
                                                         'She then take a knife and demands you to hand over all of '
                                                         'your belongings, what do you do? run/give in ')
                                        if answer11 == 'run':
                                            print('You try to escape but she throws the knife and it hits you in the '
                                                  'back of your neck. The woman stands over you as you bleed out. '
                                                  'You are dead')
                                        elif answer11 == 'give in':
                                            print('The woman sees that you have nothing but kills you anyway.'
                                                  ' You are dead.')
                                        else:
                                            print('Not a valid option. You lose.')
                                    elif answer10 == 'leave':
                                        print('As you turn to leave, the woman throws the knife and it hits you in the '
                                              'neck. The last thing you see is the woman standing over you, '
                                              'laughing. You are dead.')
                                    else:
                                        print('Not a valid option. You lose.')
                                elif answer9 == 'ignore it':
                                    print('You ignore it and continue talking. You begin to realize something is off '
                                          'but think nothing of it. You then slowly begin to lose consciousness.')
                                    answer10 = input('You wake up to find yourself tied to a chair and the woman is '
                                                     'holding an axe. She then asks you if you know who the man was '
                                                     'that gave you this letter, what do you say? no/yes ').lower()
                                    if answer10 == 'no':
                                        answer11 = input('She smiles, unties you and then asks you to marry her, '
                                                         'what do you do?'
                                                         ' accept/deny ').lower()
                                        if answer11 == 'accept':
                                            print('The two of you live out the rest of your life in the quaint cottage')
                                        elif answer11 == 'deny':
                                            print('The woman becomes enraged and brutally murders you with a knife. '
                                                  'You are dead.')
                                        else:
                                            print('Not a valid option. You lose.')
                                    elif answer10 == 'yes':
                                        print('The woman becomes visibly angry and starts to shout at you. You cower '
                                              'in fear and then try to escape but she shoots you with a bow and arrow.'
                                              ' You are dead.')
                                    else:
                                        print('Not a valid option. You lose.')
                                else:
                                    print('Not a valid option. You lose.')
                            elif not letter:
                                answer9 = input('You then forget about the letter and begin to really '
                                                'enjoy the company of this'
                                                ' woman. Within an hour you are ready to marry her, what do you do? '
                                                'propose/leave ').lower()
                                if answer9 == 'propose':
                                    print('The woman laughs in your face and then gets visibly angry. You fear for '
                                          'your life but as you turn to leave you are struck with a brick. '
                                          'You are dead')
                                elif answer9 == 'leave':
                                    print('You leave the house but notice that it has begun to storm. You only walk a '
                                          'few steps before you are struck by lightning. You are dead.')
                                else:
                                    print('Not a valid option. You lose.')
                        else:
                            print('Not a valid option. You lose.')
                    elif answer7 == 'walk in':
                        print('You walk in and are immediately confronted with a knife flying at you through the air.'
                              'You are hit in the head, you are dead.')
                    else:
                        print('Not a valid option. You lose.')
                else:
                    print('Not a valid option. You lose.')
            elif answer4 == 'refuse':
                answer5 = input('You continue walking and come across a fork, which way do you go? right/left ')
                if answer5 == 'right':
                    answer6 = input('You continue walking until you come across a sleeping giant, what do you do? '
                                    'wake it/leave ').lower()
                    if answer6 == 'wake it':
                        print('The giant wakes up and is immediately thankful for he says that he was going to '
                              'be late to his meeting. The giant then gives you '
                              'a giant gold coin for this kind gesture.')
                        gold_coin = True
                        answer7 = input('You then stumble upon a forest, what do you do? enter/'
                                        'continue walking ').lower()
                        if answer7 == 'enter':
                            answer8 = input('Upon entering the forest you are greeted by a merchant who sees your giant'
                                            ' gold coin and asks if you want to buy a sword. buy/refuse ')
                            if answer8 == 'buy':
                                answer9 = input('You purchase the sword and continue along your way '
                                                'until you come across a '
                                                'knight who challenges you to a duel. fight/refuse ')
                                if answer9 == 'fight':
                                    answer10 = input('Due to your earlier purchase, you are able to best the knight wi'
                                                     'th your sword. You keep walking until you come across a castle.'
                                                     ' ask to enter/keep walking ')
                                    if answer10 == 'ask to enter':
                                        print('You are allowed to enter and are forced to become a knight. You live out'
                                              'the rest of your days serving the lord of the castle.')
                                    elif answer10 == 'keep walking':
                                        print('As you turn to keep walking, archers appear on the wall of the castle '
                                              'and arrows rain down on you. You are dead.')
                                    else:
                                        print('Not a valid option. You lose.')
                                elif answer9 == 'refuse':
                                    print('The knight sees that you have a sword and does not accept your refusal, he'
                                          'strikes you down anyway. You are dead.')
                                else:
                                    print('Not a valid option. You lose.')
                            elif answer8 == 'refuse':
                                print('It turns out that the merchant was actually a bandit and kills you with the '
                                      'very sword he was offering, looks like you made the wrong choice. You are dead.')
                            else:
                                print('Not a valid option. You lose.')
                        elif answer7 == 'continue walking':
                            print('You eventually come across a hoard of goblins who spots your gold coin and decides'
                                  'to murder you for it. You are dead.')
                        else:
                            print('Not a valid option. You lose.')
                    elif answer6 == 'leave':
                        print('You continue walking only to hear a rumbling in the distance. The same giant you saw is'
                              ' now running towards you and he eventually tramples you. You are dead.')
                    else:
                        print('Not a valid option. You lose.')
                elif answer5 == 'left':
                    print('You are walking when suddenly a bear appears and proceeds to maul you. You are dead.')
                else:
                    print('Not a valid option. You lose.')
            else:
                print('Not a valid option. You lose.')
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')
elif answer == "right":
    print('You are walking when suddenly a bear appears and proceeds to maul you. You are dead.')
else:
    print('Not a valid option. You lose.')
