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
    print('\nTest 2\n')

    teamA = Team('Raptors', 'Toronto', 5, 108699969, 8, 0, 1, 4)
    teamB = Team('Cavaliers', 'Cleveland', 5, 127511146, 6, 1, 4, 3)
    checkWinner(teamA, teamB) # Success Winner -> CLE

    teamA = Team('Celtics', 'Boston', 4, 93465328, 8, 1, 3, 7)
    teamB = Team('Wizards', 'Washington', 9, 101312813, 6, 0, 2, 17)
    checkWinner(teamA, teamB) # Success Winner -> Boston

    teamA = Team('Warriors', 'Golden State', 1, 101725630, 9, 1, 4, 1)
    teamB = Team('Jazz', 'Utah', 5, 80498193, 6, 0, 1, 19)
    checkWinner(teamA, teamB) # Success Winner -> Warriors

    teamA = Team('Spurs', 'San Antonio', 2, 108574574, 5, 1, 4, 2)
    teamB = Team('Rockets', 'Houston', 3, 90738581, 7, 0, 1, 17)
    checkWinner(teamA, teamB) # Fail Winner -> Rockets

    print('Test 1\n')

    teamM = Team('Celtics', 'Boston', 3, 93465328, 7, 0, 3, 6)
    teamN = Team('Bulls', 'Chicago', 12, 92571386, 7, 1, 2, 9)
    checkWinner(teamM, teamN) # Success Winner -> Celtics

    teamC = Team('Wizards', 'Washington', 7, 101312813, 5, 0, 3, 10)
    teamD = Team('Hawks', 'Atlanta', 9, 96294035, 6, 1, 2, 5)
    checkWinner(teamC, teamD) # Fail Winner -> Wizards

    teamE = Team('Raptors', 'Toronto', 5, 108699969, 8, 0, 3, 2)
    teamF = Team('Bucks', 'Milwaukee', 11, 93818786, 5, 1, 2, 12)
    checkWinner(teamE, teamF) # Success Winner -> Raptors Toronto

    teamG = Team('Clippers', 'Los Angeles', 4, 116217504, 8, 0, 3, 4)
    teamH = Team('Jazz', 'Utah', 6, 80498193, 7, 1, 2, 11)
    checkWinner(teamG, teamH) # Success Winner -> LA Clippers

    teamI = Team('Rockets', 'Houston', 2, 90738581, 5, 1, 4, 8)
    teamJ = Team('Thunder', 'Ocklahoma City', 8, 91380089, 6, 0, 1, 3)
    checkWinner(teamI, teamJ) # Success Winner -> Houston Rockets

    teamK = Team('Spurs', 'San Antonio', 1, 108574574, 5, 0, 3, 1)
    teamL = Team('Grizzles', 'Memphis', 10, 110981223, 3, 1, 2, 7)
    checkWinner(teamK, teamL) # Success Winner -> SAS

    print('\nPrediction\n')

    teamA = Team('Raptors', 'Toronto', 5, 108699969, 7, 0, 1, 4)
    teamB = Team('Cavaliers', 'Cleveland', 5, 127511146, 6, 1, 4, 3)
    checkWinner(teamA, teamB) # Predict Winner -> Cleveland

    teamA = Team('Celtics', 'Boston', 4, 93465328, 8, 0, 4, 7)
    teamB = Team('Wizards', 'Washington', 9, 101312813, 5, 1, 1, 17)
    checkWinner(teamA, teamB) # Predict Winner -> Boston

    teamA = Team('Warriors', 'Golden State', 1, 101725630, 9, 1, 4, 1)
    teamB = Team('Jazz', 'Utah', 5, 80498193, 6, 0, 1, 19)
    checkWinner(teamA, teamB) # Predict Winner -> Golden State

    teamA = Team('Spurs', 'San Antonio', 2, 108574574, 4, 1, 3, 2)
    teamB = Team('Rockets', 'Houston', 3, 90738581, 7, 0, 2, 17)
    checkWinner(teamA, teamB) # Predict Winner -> San Antonio
