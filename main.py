import random, time, sys

money = 500000
rides = [['roller coaster', 'Screaming Serpent', 1], ['carousel', 'Woodland Animals', 1]]
unownedUpgrades = [['Parking Lot', 750000], ['Restaurant', 1000000], ['Fast-Food Restaurant', 500000], ['Gift Shop', 350000], ['Bowling Alley', 2000000], ['Arcade', 200000], ['Enhance Security', 100000]]
unownedSmallUpgrades = [['Ice Cream Kiosk', 100000], ['Park Map', 30000], ['Photo Kiosk', 70000], ['Virtual Reality Experience', 350000]]
ownedUpgrades = []
ownedSmallUpgrades = []
entryPrice = 10
FastPrice = 15

def simulateGuestsAndIncome():
  if len(rides) > 0:
    numOfGuests = random.randint(100_000, 500_000)
    numOfGuests /= 365
    numOfGuests *= len(rides)
    numOfGuests = int(numOfGuests)
    hooligans = random.randint(0, numOfGuests)
    if ['Enhance Security', 100000] in ownedUpgrades:
      hooligans -= random.randint(0, hooligans)
    numOfGuests -= hooligans
    allGuests = numOfGuests + hooligans
    # 10 - 20% of people get the fastpass
    fastpassChance = random.randint(10, 20)
    num = numOfGuests / 100
    num *= fastpassChance
    numOfGuests -= num
    round(numOfGuests, 0)
    round(num, 0)
    price = numOfGuests*entryPrice + num*FastPrice
    if (['Restaurant', 1000000] in ownedUpgrades or ['Fast-Food Restaurant', 500000] in ownedUpgrades) or (['Fast-Food Restaurant', 500000] in ownedUpgrades and ['Restaurant', 1000000] in ownedUpgrades):
      oneMeal = allGuests / 10 * 7
      twoMeals = allGuests / 10 * 2
      threeMeals = allGuests / 10 * 0.5
      price += oneMeal * random.randint(10, 20)
      price += twoMeals * random.randint(20, 40)
      price += threeMeals * random.randint(40, 80)
    if ['Ice Cream Kiosk', 100000] in ownedSmallUpgrades:
      iceCream = allGuests * random.randint(30, 40)
      price += iceCream * 5
    if ['Photo Kiosk', 70000] in ownedSmallUpgrades:
      photo = allGuests * random.randint(20, 30)
      price += photo * 12
    if ['Virtual Reality Experience', 350000] in ownedSmallUpgrades:
      VR = allGuests * random.randint(10, 20)
      price += VR * 15
    if ['Gift Shop', 350000] in ownedUpgrades:
      GS = allGuests * random.randint(20, 30)
      price += GS * random.randint(0.50, 50)
    if ['Bowling Alley', 2000000] in ownedUpgrades:
      BA = allGuests * random.randint(10, 20)
      price += BA * 8
    if ['Arcade', 200000] in ownedUpgrades:
      Arcade = allGuests * random.randint(20, 30)
      price += Arcade * random.randint(0.25, 10)
    return price, hooligans, allGuests
  else:
    return -100, 0, 0

print('YOU recently moved into a small town called West Valley, which got its name because it is located in between to mountains. Your uncle, the beloved owner of West Valley Amusement Park, has entrusted you with the keys to this bustling amusement park. Are you ready to embark on a journey to create your own roller coaster rides, ferris wheels, fast-food restaurants and more? The future of West Valley Amusement Park is in your hands. You have 1 year to get the park back into business. Are you ready?')
input('Press ENTER to begin!')

for i in range(365):
  print('Number of days so far:', i+1)
  money = round(money, 2)
  print(f'Money: ${money}')
  print(f'Entry price: ${entryPrice} (per person)')
  print(f'Fast-pass price: ${FastPrice} (per person)')
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
  print('9. Set entry price.')
  print('10. Set FastPass price.')
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
      print('The cost of making the ferris wheel is $5,000,000. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 5000000:
          money -= 5000000
          print('You have created a ferris wheel called', name)
          rides.append(['ferris wheel', name, 1])
        else:
          print('You do not have enough money to make this ride.')
    elif answer == '2':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the roller coaster is $15,000,000. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 15000000:
          money -= 15000000
          print('You have created a roller coaster called', name)
          rides.append(['roller coaster', name, 1])
        else:
          print('You do not have enough money to make this ride.')
    elif answer == '3':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the swing ride is $250,000. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 250000:
          money -= 250000
          print('You have created a swing ride called', name)
          rides.append(['swing ride', name, 1])
        else:
          print('You do not have enough money to make this ride.')
    elif answer == '4':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the carousel is $750,000. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 750000:
          money -= 750000
          print('You have created a carousel called', name)
          rides.append(['carousel', name, 1])
        else:
          print('You do not have enough money to make this ride.')
    elif answer == '5':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the haunted house is $2,000,000. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 2000000:
          money -= 2000000
          print('You have created a haunted house called', name)
          rides.append(['haunted house', name, 1])
        else:
          print('You do not have enough money to make this ride.')
    elif answer == '6':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the water flume is $4,000,000. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 4000000:
          money -= 4000000
          print('You have created a water flume called', name)
          rides.append(['water flume', name, 1])
        else:
          print('You do not have enough money to make this ride.')
    elif answer == '7':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the bumper cars is $1,000,000. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 1000000:
          money -= 1000000
          print('You have created a bumper cars ride called', name)
          rides.append(['bumper cars', name, 1])
        else:
          print('You do not have enough money to make this ride.')
    elif answer == '8':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the drop tower is $2,500,000. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 2500000:
          money -= 2500000
          print('You have created a drop tower called', name)
          rides.append(['drop tower', name, 1])
        else:
          print('You do not have enough money to make this ride.')
    elif answer == '9':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the funhouse is $1,000,000. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 1000000:
          money -= 1000000
          print('You have created a funhouse called', name)
          rides.append(['funhouse', name, 1])
        else:
          print('You do not have enough money to make this ride.')
    elif answer == '10':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the teacup ride is $350,000. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 350000:
          money -= 350000
          print('You have created a teacup ride called', name)
          rides.append(['teacup ride', name, 1])
        else:
          print('You do not have enough money to make this ride.')
    elif answer == '11':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the motion simulator is $1,000,000. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 1000000:
          money -= 1000000
          print('You have created a motion simulator called', name)
          rides.append(['motion simulator', name, 1])
        else:
          print('You do not have enough money to make this ride.')
    elif answer == '12':
      print('What would you like to name your ride?')
      name = input('> ')
      print('The cost of making the boat ride is $2,000,000. Are you sure you want to make this ride? (y/n)')
      answer = input('> ')
      if answer.lower().startswith('y'):
        if money >= 2000000:
          money -= 2000000
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
  elif answer == '9':
    print('What would you like the entry price to be?')
    answer = input('> ')
    if answer.isdigit():
      answer = int(answer)
      entryPrice = answer
  elif answer == '10':
    print('What would you like the FastPAss price to be?')
    answer = input('> ')
    if answer.isdigit():
      answer = int(answer)
      FastPrice = answer
  earned, hoolies, guests = simulateGuestsAndIncome()
  print(f'You earned ${earned} today.')
  money += earned
  print(f'{hoolies} people got into your park without paying today. (You got {hoolies} hooligans today)')
  print(f'{guests} people bought passes into your park today.')