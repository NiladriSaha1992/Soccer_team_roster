players = {}

for i in range(1, 6):
  print("Enter player " + str(i) + "'s jersey number: ")
  jersey_number = int(input())
  print("Enter player " + str(i) + "'s rating: ")
  players[jersey_number] = int(input())
  print()

# function to output Roster
def outputRoster():
  keys = list(players.keys())
  keys.sort()
  print("ROSTER")
  for key in keys:
    print("Jersey number: %d, Rating: %d" % (key, players[key]))

# function to add a player
def addPlayer():
  print("Enter player's jersey number:")
  j_number = int(input())
  print("Enter player's rating:")
  players[j_number] = int(input())
  print()
  print("***player added successfully!")
  print()
  outputRoster()

# function to remove player
def remPlayer():
  print("Enter the player's jersey number, whom you want to remove:")
  j_number = int(input())
  if j_number in players:
    players.pop(j_number)
    print()
    print("***player removed successfully!")
    print()
    outputRoster()
  else:
    print()
    print("***sorry, no such player found!")
    print()

# function to update a player info
def updatePlayer():
  print("Enter the player's jersey number, whom you want to update:")
  j_number = int(input())
  if j_number in players:
    print("Enter the new rating:")
    player_new_rating = int(input())
    players[j_number] = player_new_rating
    print()
    print("***player's info updated successfully!")
    print()
    outputRoster()
  else:
    print()
    print("***sorry, no such player found!")
    print()

# function to find players above a rating
def playersAboveARating():
  print("Please enter a rating:")
  rating = int(input())
  sortedJerseys = list()
  for jersey_number, playerRating in players.items():
    if playerRating > rating:
      sortedJerseys.append(jersey_number)
  sortedJerseys.sort()
  print()
  print("Players with rating above %d are: " % (rating))
  for j in sortedJerseys:
    print("Jersey number: %d, Rating: %d" % (j, players[j]))
  print()

# This is the main function which will call itself again and again after the outcome of each option you choose (to let this program continue until you choose the 'q' option i.e. quit the program)
def main():
  print()
  print("MENU")
  print("a - Add player")
  print("d - Remove player")
  print("u - Update player rating")
  print("r - Output players above a rating")
  print("o - Output roster")
  print("q - Quit")
  print()
  print("Choose an option:")

  option = input()

  if option == 'a':
    addPlayer()
    main()
  elif option == 'd':
    remPlayer()
    main()
  elif option == 'u':
    updatePlayer()
    main()
  elif option == 'r':
    playersAboveARating()
    main()
  elif option == 'o':
    outputRoster()
    main()
  elif option == 'q':
    exit()

# calling the main function
main()