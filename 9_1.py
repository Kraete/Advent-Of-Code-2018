players = 9
highest_marble = 25
scores = range(players+1)

circle = []
current_marble = 0
marbles = range(highest_marble+1)
turn = 0

def add_marble(circle, marble):
  global current_marble
  global turn
  if (marble % 23):
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
    print(str(turn) + ' ' + ','.join(str(x) for x in circle) + ' -' + str(current_marble))
    turn += 1
  else:
    index = turn % players if turn%players else 9
    scores[index] += marble
    marble = circle.pop(current_marble - 7)
    print("popped:" + marble)
    scores[index] += marble

while len(marbles):
  add_marble(circle, marbles.pop(0))

