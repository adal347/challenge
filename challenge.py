class Value(object):
    position = .25
    budget = .2
    lastTen = .2
    isLocal = .15
    lastVs = .15
    lastSeason = .05

class Team(object):

    """docstring for Team."""
    def __init__(self, name, sede, position, budget, lastTen, isLocal, lastVs, lastSeason):
        self.name = name
        self.sede = sede
        self.position = position
        self.budget = budget
        self.lastTen = lastTen
        self.isLocal = isLocal
        self.lastVs = lastVs
        self.lastSeason = lastSeason
        self.finalProbability = 0

    def obtainProbability(self, probabilty):
        self.finalProbability += probabilty

def positionProbability(teamA, teamB):
    probabiltyTeamA = (1 - (float(teamA.position)/float(teamA.position + teamB.position))) * Value.position
    probabiltyTeamB = (1 - (float(teamB.position)/float(teamA.position + teamB.position))) * Value.position
    teamA.obtainProbability(probabiltyTeamA)
    teamB.obtainProbability(probabiltyTeamB)

def budgetProbability(teamA, teamB):
    probabiltyTeamA = (float(teamA.budget)/float(teamA.budget + teamB.budget)) * Value.budget
    probabiltyTeamB = (float(teamB.budget)/float(teamA.budget + teamB.budget)) * Value.budget
    teamA.obtainProbability(probabiltyTeamA)
    teamB.obtainProbability(probabiltyTeamB)

def lastTenProbability(teamA, teamB):
    probabiltyTeamA = (float(teamA.lastTen)/float(teamA.lastTen + teamB.lastTen)) * Value.lastTen
    probabiltyTeamB = (float(teamB.lastTen)/float(teamA.lastTen + teamB.lastTen)) * Value.lastTen
    teamA.obtainProbability(probabiltyTeamA)
    teamB.obtainProbability(probabiltyTeamB)

def isLocalProbability(teamA, teamB):
    probabiltyTeamA = teamA.isLocal * Value.isLocal
    probabiltyTeamB = teamB.isLocal * Value.isLocal
    teamA.obtainProbability(probabiltyTeamA)
    teamB.obtainProbability(probabiltyTeamB)

def lastVsProbability(teamA, teamB):
    probabiltyTeamA = (float(teamA.lastVs)/float(teamA.lastVs + teamB.lastVs)) * Value.lastVs
    probabiltyTeamB = (float(teamB.lastVs)/float(teamA.lastVs + teamB.lastVs)) * Value.lastVs
    teamA.obtainProbability(probabiltyTeamA)
    teamB.obtainProbability(probabiltyTeamB)

def lastSeasonProbability(teamA, teamB):
    probabiltyTeamA = (1 - (float(teamA.lastSeason)/float(teamA.lastSeason + teamB.lastSeason))) * Value.lastSeason
    probabiltyTeamB = (1 - (float(teamB.lastSeason)/float(teamA.lastSeason + teamB.lastSeason))) * Value.lastSeason
    teamA.obtainProbability(probabiltyTeamA)
    teamB.obtainProbability(probabiltyTeamB)

def checkWinner(teamA, teamB):
    positionProbability(teamA, teamB)
    budgetProbability(teamA, teamB)
    lastTenProbability(teamA, teamB)
    isLocalProbability(teamA, teamB)
    lastVsProbability(teamA, teamB)
    lastSeasonProbability(teamA, teamB)
    if teamA.finalProbability < teamB.finalProbability:
        print('Game ' + teamA.name + ' vs ' + teamB.Name)
        print('Winner: ' + teamB.sede + ' ' + teamB.name)
    else:
        print('Game ' + teamA.name + ' vs ' + teamB.Name)
        print('Winner: ' + teamA.sede + ' ' + teamA.name)

if __name__ == '__main__':
