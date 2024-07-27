import random, time, sys

money = 1000
rides = []
unownedUpgrades = [['Parking Lot', 100], ['Resturaunt', 100], ['Fast-Food Resturaunt', 100], ['Gift Shop', 100], ['Bowling Alley', 100], ['Arcade', 100], ['Enhance Security', 100]]
unownedSmallUpgrades = [['Ice Cream Kiosk', 50], ['Park Map', 50], ['Photo Kiosk', 50], ['Virtual Reality Experience', 50]]
ownedUpgrades = []
ownedSmallUpgrades = []

print('YOU recently moved into a small town called West Valley, which got its name because it is located in between to mountains. Your uncle, the beloved owner of West Valley Amusement Park, has entrusted you with the keys to this bustling amusement park. Are you ready to embark on a journey to create your own roller coaster rides, ferris wheels, fast-food restraunts and more? The future of West Valley Amusement Park is in your hands. You have 1 year to get the park back into business. Are you ready?')
input('Press ENTER to begin!')

for i in range(365):
  print('Number of days so far:', i+1)
  money = round(money, 2)
  print(f'Money: ${money}')
  print()
  print('Here are your options:')
  print('1. Create a ride.')
  print('2. View rides.')
  print('3. Upgrade a ride.')
  print('4. Destroy a ride.')
  print('5. Install a large upgrade.')
  print('6. Install a small upgrade.')
  print('7. View large upgrades.')
  print('8. View small upgrades.')
  answer = input('> ')
  if answer == '1':
    print('What type of ride would you like to create?')
    print('1. Ferris Wheel')
    print('2. Roller Coaster')
    print('3. Swing Ride')
    print('4. Carousel')
    print('5. Haunted House')
    print('6. Water Flume Ride')
    print('7. Bumper Cars')
    print('8. Drop Tower')
    print('9. Funhouse')
    print('10. Teacup Ride')
    print('11. Motion Simulator')
    print('12. Boat Ride')
    print()
    answer = input('> ')
    if answer == '1':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the ferris wheel is $100. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 100:
          money -= 100
          print('You have created a ferris wheel called', name)
          rides.append(['ferris wheel', name, 1])
        else:
          print('You do not have enough money to make this ride.')
    elif answer == '2':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the roller coaster is $100. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 100:
          money -= 100
          print('You have created a roller coaster called', name)
          rides.append(['roller coaster', name, 1])
        else:
          print('You do not have enough money to make this ride.')
    elif answer == '3':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the swing ride is $100. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 100:
          money -= 100
          print('You have created a swing ride called', name)
          rides.append(['swing ride', name, 1])
        else:
          print('You do not have enough money to make this ride.')
    elif answer == '4':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the carousel is $100. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 100:
          money -= 100
          print('You have created a carousel called', name)
          rides.append(['carousel', name, 1])
        else:
          print('You do not have enough money to make this ride.')
    elif answer == '5':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the haunted house is $100. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 100:
          money -= 100
          print('You have created a haunted house called', name)
          rides.append(['haunted house', name, 1])
        else:
          print('You do not have enough money to make this ride.')
    elif answer == '6':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the water flume is $100. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 100:
          money -= 100
          print('You have created a water flume called', name)
          rides.append(['water flume', name, 1])
        else:
          print('You do not have enough money to make this ride.')
    elif answer == '7':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the bumper cars is $100. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 100:
          money -= 100
          print('You have created a bumper cars ride called', name)
          rides.append(['bumper cars', name, 1])
        else:
          print('You do not have enough money to make this ride.')
    elif answer == '8':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the drop tower is $100. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 100:
          money -= 100
          print('You have created a drop tower called', name)
          rides.append(['drop tower', name, 1])
        else:
          print('You do not have enough money to make this ride.')
    elif answer == '9':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the funhouse is $100. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 100:
          money -= 100
          print('You have created a funhouse called', name)
          rides.append(['funhouse', name, 1])
        else:
          print('You do not have enough money to make this ride.')
    elif answer == '10':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the teacup ride is $100. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 100:
          money -= 100
          print('You have created a teacup ride called', name)
          rides.append(['teacup ride', name, 1])
        else:
          print('You do not have enough money to make this ride.')
    elif answer == '11':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the motion simulator is $100. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 100:
          money -= 100
          print('You have created a motion simulator called', name)
          rides.append(['motion simulator', name, 1])
        else:
          print('You do not have enough money to make this ride.')
    elif answer == '12':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the boat ride is $100. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 100:
          money -= 100
          print('You have created a boat ride called', name)
          rides.append(['boat ride', name, 1])
        else:
          print('You do not have enough money to make this ride.')
  elif answer == '2':
    for i in range(len(rides)):
      print(str(i+1)+'. A '+rides[i][0]+' called '+rides[i][1]+'. (Level ' + str(rides[i][2]) + ')')
  elif answer == '3':
    print('Which ride would you like to upgrade? It costs $100 to upgrade.')
    for i in range(len(rides)):
      print(str(i+1)+'. A '+rides[i][0]+' called '+rides[i][1]+'.')
    answer = input('> ')
    if answer.isdigit():
      answer = int(answer)
      if answer > 0 and answer <= len(rides):
        if money >= 100:
          rides[answer-1][2] += 1
          print('You upgraded', rides[answer-1][1])
          money-=100
  elif answer == '4':
    print('Which ride would you like to destroy? Enter back to go back.')
    for i in range(len(rides)):
      print(str(i+1)+'. A '+rides[i][0]+' called '+rides[i][1]+'. (Level ' + str(rides[i][2]) + ')')
    answer = input('> ')
    if answer.isdigit():
      answer = int(answer)
      if answer > 0 and answer <= len(rides):
        rides.pop(answer-1)
  elif answer == '5':
    print('Choose a large upgrade to install (or enter back to go back):')
    for i in range(len(unownedUpgrades)):
      print(str(i+1)+'. '+unownedUpgrades[i][0]+' ($'+str(unownedUpgrades[i][1])+')')
    answer = input('> ')
    if answer.isdigit():
      answer = int(answer)
      if answer > 0 and answer <= len(unownedUpgrades):
        if money >= unownedUpgrades[answer-1][1]:
          money -= unownedUpgrades[answer-1][1]
          print('You have installed the', unownedUpgrades[answer-1][0])
          ownedUpgrades.append(unownedUpgrades[answer-1][0])
          unownedUpgrades.pop(answer-1)
  elif answer == '6':
    print('Choose a small upgrade to install (or enter back to go back):')
    for i in range(len(unownedSmallUpgrades)):
      print(str(i+1)+'. '+unownedSmallUpgrades[i][0]+' ($'+str(unownedSmallUpgrades[i][1])+')')
    answer = input('> ')
    if answer.isdigit():
      answer = int(answer)
      if answer > 0 and answer <= len(unownedSmallUpgrades):
        if money >= unownedSmallUpgrades[answer-1][1]:
          money -= unownedSmallUpgrades[answer-1][1]
          print('You have installed the', unownedSmallUpgrades[answer-1][0])
          ownedSmallUpgrades.append(unownedSmallUpgrades[answer-1][0])
          unownedSmallUpgrades.pop(answer-1)
  elif answer == '7':
    for i in range(len(ownedUpgrades)):
      print(str(i+1)+'. '+ownedUpgrades[i])
  elif answer == '8':
    for i in range(len(ownedSmallUpgrades)):
      print(str(i+1)+'. '+ownedSmallUpgrades[i])