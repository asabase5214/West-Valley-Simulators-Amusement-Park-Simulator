import random, time, sys
from termcolor import colored

billboards = 0
achievements = 0
a1, a2, a3, a4, a5 = False, False, False, False, False
money = 500000
TVends = 0
socialmediaads = 0
TVcommercials = 0
Bends = 0
seasonal_factors = {
    "January": 0.8,
    "February": 0.9,
    "March": 1.0,
    "April": 1.1,
    "May": 1.2,
    "June": 1.2,
    "July": 1.1,
    "August": 1.0,
    "September": 0.9,
    "October": 0.8,
    "November": 0.7,
    "December": 0.5
}
seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
monthLengths = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
rides = [['roller coaster', 'Screaming Serpent', 1], ['carousel', 'Woodland Animals', 1]]
unownedUpgrades = [['Parking Lot', 750000], ['Restaurant', 1000000], ['Fast-Food Restaurant', 500000], ['Gift Shop', 350000], ['Bowling Alley', 2000000], ['Arcade', 200000], ['Enhance Security', 100000]]
unownedSmallUpgrades = [['Ice Cream Kiosk', 100000], ['Park Map', 30000], ['Photo Kiosk', 70000], ['Virtual Reality Experience', 350000]]
ownedUpgrades = []
ownedSmallUpgrades = []
entryPrice = 10
FastPrice = 15

def simulateGuestsAndIncome(month):
  if len(rides) > 0:
    numOfGuests = random.randint(1_000_000, 5_000_000)
    numOfGuests /= entryPrice
    numOfGuests /= 365
    numOfGuests *= len(rides)
    numOfGuests = int(numOfGuests)
    hooligans = random.randint(0, numOfGuests)
    if ['Enhance Security', 100000] in ownedUpgrades:
      hooligans -= random.randint(0, hooligans)
    numOfGuests -= hooligans
    allGuests = numOfGuests + hooligans
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
    numOfGuests *= seasonal_factors[month]
    for i in range(billboards):
      numOfGuests *= random.randint(102, 105)/100
    for i in range(TVcommercials):
      numOfGuests *= random.randint(110, 300)/100
    for i in range(socialmediaads):
      numOfGuests *= random.randint(110, 250)/100
    return price, hooligans, allGuests
  else:
    return -100, 0, 0

def prettyPrintNum(num):
  num = str(num)
  if '.' in num:
      num_split = num.split('.')
      num = num_split[0]
  num = num[::-1]
  result = ''
  for i in range(len(num)):
      if i % 3 == 0 and i != 0:
          result += ','
      result += num[i]
  num = result[::-1]
  if num[0] == ',':
      num = num[1:]
  if len(num) >= 2 and num[-2] == '.':
      num = list(num)
      num.append('0')
      num = ''.join(num)
  elif '.' not in num:
      num = list(num)
      num.append('.00')
      num = ''.join(num)
  return num

def calculateDay(month, day):
  if month == 'January':
    return day
  elif month == 'February':
    return day - 31
  elif month == 'March':
    return day - 59
  elif month == 'April':
    return day - 90
  elif month == 'May':
    return day - 120
  elif month == 'June':
    return day - 151
  elif month == 'July':
    return day - 181
  elif month == 'August':
    return day - 212
  elif month == 'September':
    return day - 243
  elif month == 'October':
    return day - 273
  elif month == 'November':
    return day - 304
  else:
    return day - 334

print('YOU recently moved into a small town called West Valley, which got its name because it is located in between to mountains. Your uncle, the beloved owner of West Valley Amusement Park, has entrusted you with the keys to this bustling amusement park. Are you ready to embark on a journey to create your own roller coaster rides, ferris wheels, fast-food restaurants and more? The future of West Valley Amusement Park is in your hands. You have 1 year to get the park back into business. Are you ready?')
input('Press ENTER to begin!')

for i in range(365):
  if Bends == i+1:
    print('It has been 4 weeks since you bought those billboards. They have now expired.')
    billboards = 0
  if TVends == i+1:
    print('It has been 4 weeks since you made those TV commercials. They have now expired.')
    TVcommercials -= 1
  if i+1 < 32:
    month = 'January'
  elif i+1 < 60:
    month = 'February'
  elif i+1 < 91:
    month = 'March'
  elif i+1 < 121:
    month = 'April'
  elif i+1 < 152:
    month = 'May'
  elif i+1 < 182:
    month = 'June'
  elif i+1 < 213:
    month = 'July'
  elif i+1 < 244:
    month = 'August'
  elif i+1 < 274:
    month = 'September'
  elif i+1 < 305:
    month = 'October'
  elif i+1 < 335:
    month = 'November'
  elif i+1 < 366:
    month = 'December'
  print(f'It is {month} {calculateDay(month, i+1)}.')
  if i+1 == 359:
    print('Merry Christmas!')
    time.sleep(3)
  elif i+1 == 304:
    print('Happy Halloween!')
    time.sleep(3)
  elif i+1 == 89:
    print('Happy Easter!')
    time.sleep(3)
  if month in ['December', 'January', 'February']:
    print('It is currently Winter.')
  elif month in ['March', 'April', 'May']:
    print('It is currently Spring.')
  elif month in ['June', 'July', 'August']:
    print('It is currently Summer.')
  elif month in ['September', 'October', 'November']:
    print('It is currently Autumn.')
  print('Number of days so far:', i+1)
  money = round(money, 2)
  original_money = money
  print(f'Money: ${prettyPrintNum(money)}')
  if money >= 1_000_000_000:
    if not a5:
      a5 = True
      print('\n'*60)
      print(colored('Congrats! You earned an achievement: \"BILLIONAIRE\"', 'yellow'))
      print(colored('Have $1,000,000,000 in your bank acount.', 'yellow'))
      achievements += 1
      time.sleep(5)
  print(f'Entry price: ${prettyPrintNum(entryPrice)} (per person)')
  print(f'Fast-pass price: ${prettyPrintNum(FastPrice)} (per person)')
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
  print('11. Begin an advertising campaign.')
  if i+1 == 359:
    print('12. Put up Christmas decorations!')
  if i+1 == 304:
    print('12. Put up Halloween decorations!')
  if i+1 == 89:
    print('12. Put up Easter decorations!')
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
  elif answer == '11':
    print('Choose a type of advertisment:')
    print('1. Billboards')
    print('2. TV commercials')
    print('3. Social Media Ads')
    print('Enter back to go back.')
    print()
    answer = input('> ')
    if answer == '1':
      print('How many billboards would you like to make? It costs $6,000 per billboard, and each billboard lasts 4 weeks (about 1 month). If you already have billboards, then if you choose to get more, the older ones will disappear. Enter 0 if you have changed your mind about this.')
      answer = input('> ')
      if answer.isdigit():
        answer = int(answer)
        if answer > 0:
          if money >= answer*6000:
            money -= answer*6000
            print('You have made', answer, 'billboards.')
            billboards = answer
            Bends = i+29
            if not a1:
              a1 = True
              print('\n'*60)
              print(colored('Congrats! You earned an achievement: \"Create your first billboard\"', 'yellow'))
              achievements += 1
              time.sleep(5)
          else:
            print('You do not have enough money to make this many billboards.')
        else:
          print('0 billboards have been made.')
    elif answer == '2':
      concept  = input('Enter the basic concept for your commercial here.')
      scripting_fee = random.randint(500, 3000)
      casting_fee = random.randint(500, 2000)
      filming_fee = random.randint(2000, 12000)
      editing_fee = random.randint(1000, 5000)
      print('To make your desired commercial, the estimated cost will be $'+str(scripting_fee+casting_fee+filming_fee+editing_fee)+ '. ' +'Enter 1 to confirm, or enter 0 to go back.')
      answer = input('> ')
      if answer == '1':
        if money >= scripting_fee+casting_fee+filming_fee+editing_fee:
          money -= scripting_fee+casting_fee+filming_fee+editing_fee
          print('You have made a TV commercial.')
          TVcommercials += 1
          TVends = i+29
        else:
          print('You do not have enough money to make this TV commercial.')
    elif answer == '3':
      input('Enter what you want to include in your ad here: ')
      cost = random.randint(200, 2000)
      print('To make your desired ad, the estimated cost will be $'+str(cost)+'. Enter 1 to confirm, or 0 to go back.')
      answer = input('> ')
      if answer == '1':
        if money >= cost:
          money -= cost
          print('You have made a social media ad.')
          socialmediaads += 1
        else:
          print('You do not have enough money to make this social media ad.')
  elif answer == '12':
    if i+1 == 359:
      print('Your amusement park is now decorated with Christmas trees, lights, snowmen, and more!')
    elif i+1 == 304:
      print('Your amusement park is now decorated with pumpkins, ghost, witches, and more!')
    elif i+1 == 89:
      print('Your amusement park is now decorated with eggs, bunnies, and more!')
    time.sleep(5)
  if original_money - money >= 1000000:
    if not a3:
      a3 = True
      print('\n'*60)
      print(colored('Congrats! You earned an achievement: \"Budget Buster\"', 'yellow'))
      print(colored('Spend at least 1 million dollars in a single day.', 'yellow'))
      achievements += 1
      time.sleep(5)
  earned, hoolies, guests = simulateGuestsAndIncome(month)
  print(f'You earned ${prettyPrintNum(earned)} today.')
  money += earned
  print(f'{hoolies} people got into your park without paying today. (You got {hoolies} hooligans today)')
  if hoolies < 100:
    if not a2:
      a2 = True
      print('\n'*60)
      print(colored('Congrats! You earned an achievement: \"Hooligan Hunter\"', 'yellow'))
      print(colored('Have only 100 hooligans get into your park one day.', 'yellow'))
      achievements += 1
      time.sleep(5)
  print(f'{guests} people bought passes into your park today.')
  RCs = 0
  for i in range(len(rides)):
    if rides[i][0] == 'roller coaster':
      RCs += 1
  if RCs >= 10:
    if not a4:
      a4 = True
      print('\n'*60)
      print(colored('Congrats! You earned an achievement: \"Roller Coaster King\"', 'yellow'))
      print(colored('Have 10 roller coasters in your park.', 'yellow'))
      achievements += 1
      time.sleep(5)

print('Congratulations! You have made it to the end of the year! You have made $'+ str(money - 500000) +'.')
time.sleep(5)
print(f'You had {len(rides)} rides.')
time.sleep(3)
print(f'You earned {achievements} achievements.')
time.sleep(3)
print()
print('Thank you for playing!')
sys.exit()