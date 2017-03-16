#part of the Missouri Trail game
#by Erik B & David I (davidizzy)

import random, outcomes

def is_prime(n):
  '''Check to see if a given number is prime'''

  # Check that n is not a special case (i.e. 0 or 1)
  if n == 0 or n == 1:
    return False

  # Count number of divisors n has. Anything greater than 2 means
  # n has more than 1 and itself as divisors, therefore not prime
  count = 0
  for i in range(1, n+1):
    if n % i == 0:
      count += 1
    if count > 2:
      return False
  return True

def forward(player): #move wagon forward random number of spaces
    spaces = random.randint(0,50)
    player.distanceTraveled += spaces
    if is_prime(spaces):
        return(bad_move(player, spaces))
    else:
        return "The road is rough, but you're pressing onward!"

def bad_move(player, spaces):
    if spaces <= 13:
        return outcomes.safe_move(player)
    elif spaces > 13 and spaces < 29:
        return outcomes.dysentery(player)
    else:
        return outcomes.wolf_attack(player)
