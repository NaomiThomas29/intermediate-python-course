import random
def main():
  dice_rolls = int(input('How many dice would you like to roll? '))
  dice_size = int(input('How many sides are the dice? '))
  
  dice_sum = 0
  for i in range(0, dice_rolls):
    # adding more inputs - like player or team name
    player = input('Who is rolling? ')
    roll = random.randint(1,dice_size)
    if roll == 1:
      print(f'{player} rolled a {roll}! Critical Fail')
    elif roll == dice_size:
      print(f'{player} rolled a {roll}! Critical Success!')
    else:
      print(f'{player} rolled a {roll}')
    dice_sum+= roll
    
  print(f'Total rolled is {dice_sum}')

if __name__== "__main__":
  main()
