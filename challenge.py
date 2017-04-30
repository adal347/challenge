class Value(object):
    position = .25
    budget = .2
    lastTen = .2
    isLocal = .15
    lastVs = .15
    lastSeason = .05

class Team(object):

    finalProbability = 0

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

    def obtainProbability(probabilty):
        finalProbability += probabilty

def positionProbability(teamA, teamB):
    probabiltyTeamA = (1 - (teamA.position/(teamA.position + teamB.position))) * Value.position
    probabiltyTeamB = (1 - (teamB.position/(teamA.position + teamB.position))) * Value.position
    teamA.obtainProbability(probabiltyTeamA)
    teamB.obtainProbability(probabiltyTeamB)

def budgetProbability(teamA, teamB):
    probabiltyTeamA = (teamA.budget/(teamA.budget + teamB.budget)) * Value.budget
    probabiltyTeamB = (teamB.budget/(teamA.budget + teamB.budget)) * Value.budget
    teamA.obtainProbability(probabiltyTeamA)
    teamB.obtainProbability(probabiltyTeamB)

def lastTenProbability(teamA, teamB):
    probabiltyTeamA = (teamA.lastTen/(teamA.lastTen + teamB.lastTen)) * Value.lastTen
    probabiltyTeamB = (teamB.lastTen/(teamA.lastTen + teamB.lastTen)) * Value.lastTen
    teamA.obtainProbability(probabiltyTeamA)
    teamB.obtainProbability(probabiltyTeamB)

def isLocalProbability(teamA, teamB):
    probabiltyTeamA = teamA.isLocal * Value.isLocal
    probabiltyTeamB = teamB.isLocal * Value.isLocal
    teamA.obtainProbability(probabiltyTeamA)
    teamB.obtainProbability(probabiltyTeamB)

def lastVsProbability(teamA, teamB):
    probabiltyTeamA = (teamA.lastVs/(teamA.lastVs + teamB.lastVs)) * Value.lastVs
    probabiltyTeamB = (teamB.lastVs/(teamA.lastVs + teamB.lastVs)) * Value.lastVs
    teamA.obtainProbability(probabiltyTeamA)
    teamB.obtainProbability(probabiltyTeamB)

def lastSeasonProbability(teamA, teamB):
    probabiltyTeamA = (1 - (teamA.lastSeason/(teamA.lastSeason + teamB.lastSeason))) * Value.lastSeason
    probabiltyTeamB = (1 - (teamB.lastSeason/(teamA.lastSeason + teamB.lastSeason))) * Value.lastSeason
    teamA.obtainProbability(probabiltyTeamA)
    teamB.obtainProbability(probabiltyTeamB)

def checkWinner(teamA, teamB):
    positionProbability(teamA, teamB)
    budgetProbability(teamA, teamB)
    lastTenProbability(teamA, teamB)
    isLocalProbability(teamA, teamB)
    lastVsProbability(teamA, teamB)
    lastSeason(teamA, teamB)
    if teamA.finalProbability < teamB.finalProbability:
        print('Winner: ' + teamB.sede, teamB.name)
    else:
        print('Winner: ' + teamA.sede, teamA.name)

if __name__ == '__main__':
    teamA = new Team('Rockets', 'Houston', 2, 90738581, 5, 1, 4, 8)
    TeamB = new Team('Thunder', 'Ocklahoma City', 8, 91380089, 6, 0, 1, 3)
    checkWinner(teamA, teamB)
