import sys
input = sys.stdin.readline
cases = int(input())
respuesta = 0
respuestas = []


for _ in range(cases):
    numTeams = int(input())
    playedWinners = numTeams-1
    numTeamsLosers = playedWinners
    playedLosers = numTeamsLosers-1
    respuesta = playedLosers+playedWinners
    respuestas.append(respuesta+1)

for i in respuestas:
    print(i)