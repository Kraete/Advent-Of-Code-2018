players = 9
highest_marble = 25
scores = [0 for x in range(players+1)]

circle = []
current_marble = 0
marbles = range(highest_marble+1)
turn = 0


def add_marble(circle, marble):
    global current_marble
    global turn
    if marble % 23 == 0 and turn > 0:
        index = turn % players if turn % players else players
        print("Player: "+str(index))
        print("Marble: "+str(marble) + ' Index: '+str(circle.index(current_marble)))
        scores[index] += marble
        to_pop = circle.index(current_marble) - 7
        marble = circle.pop(to_pop)
        print("Marble: "+str(marble) + ' Index: '+str(to_pop))
        scores[index] += marble
        print("Score: "+str(scores[index]))
        current_marble = circle[to_pop]
        print("Current Marble: "+str(current_marble))
        print("")
    else:
        if len(circle) < 2:
            index = 0
            circle.append(marble)
        else:
            index = (circle.index(current_marble) + 2) % len(circle)
            if index == 0:
                circle.append(marble)
            else:
                circle.insert(index, marble)
        current_marble = marble
# print(str(turn) + ' ' + ','.join(str(x) for x in circle) + ' -' + str(current_marble))
    turn += 1


while len(marbles):
    add_marble(circle, marbles.pop(0))

print(scores)
