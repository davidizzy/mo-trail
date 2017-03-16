#part of the Missouri Trail game
#by Erik B & David I (davidizzy)

#classes for Missouri Trail
import movements

class player:
    #base conditions for character types
    def __init__(self, initName):
        self.name = initName
        self.isAlive = True
        self.distanceTraveled = 0
        self.wolfAttackSurvival = False
        self.dysenterySurvival = False

    def getName(self):
        return self.name

    def getDistance(self):
        return self.distanceTraveled

    def moveForward(self):
        return movements.forward(self)

class doctor(player):
    #doctor should include the ability to suvive dysentary once
    def __init__(self, initName):
        player.__init__(self, initName)
        self.name = initName
        self.dysenterySurvival = True

class hunter(player):
    #hunter should include the ability to suvive wolf attack once
    def __init__(self, initName):
        player.__init__(self, initName)
        self.name = initName
        self.wolfAttackSurvival = True
