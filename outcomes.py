#part of the Missouri Trail game
#by Erik B & David I (davidizzy)

def wolf_attack(player):
    if player.wolfAttackSurvival == True:
        player.wolfAttackSurvival = False
        return "There was a wolf attack!\nYou survived, thanks to your expert hunting skills!"
    else:
        player.isAlive = False
        return "There was a wolf attack!\nUnfortunately, the wolves ate you.\n\nAt least THEY aren't hungry anymore."

def dysentery(player):
    if player.dysenterySurvival == True:
        player.dysenterySurvival = False
        return "Dysentery is rough!\nYou survived, thanks to your medical knowledge."
    else:
        player.isAlive = False
        return "You have died of dysentery."

def safe_move(player):
    return "Onward!"
