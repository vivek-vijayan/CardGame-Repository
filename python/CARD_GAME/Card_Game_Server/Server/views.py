from django.shortcuts import render
from .models import *
from django.db.models import Sum
from django.db.models import F

# Create your views here.


def homepage(request, gameid):
    players = GamePlayer.objects.all()
    lastgameWinnerName, lastgameWinnerScore = None, None
    lastwinner = GamePlay.objects.all().order_by('-gameplayID')[:1]
    gameActive = None
    gA = GameSet.objects.filter(gameID = gameid)
    for x in gA:
        if x.gameOver:
            gameActive = False
        else:
            gameActive = True
    for x in lastwinner:
        lastgameWinnerScore = x.score
        lastgameWinnerName = x.playerID

    gameflow = GamePlay.objects.all().order_by('-gameplayID')[:5]

    gameplayPlayerwise = GamePlay.objects.filter(gameID=gameid).values('playerID', 'gameID').order_by(
        'playerID', 'gameID').annotate(total=Sum('score'))
    return render(request=request, template_name="index.html", context={
        'players': players,
        'gameplayPlayerwise': gameplayPlayerwise,
        'gameid': gameid,
        'lastWinnerName': lastgameWinnerName,
        'lastWinnerScore': lastgameWinnerScore,
        'gameActive': gameActive,
        'gameflow': gameflow
    })


def winner(request, gameid,  winnerID, score, total):
    gamesetinstance = None
    playerinstance = None
    for x in GameSet.objects.filter(gameID=gameid):
        gamesetinstance = x
    for x in GamePlayer.objects.filter(playerID=winnerID):
        playerinstance = x
    g = GamePlay.objects.create(
        gameID=gamesetinstance,
        playerID=playerinstance,
        score=score,
    )
    player = GamePlayer.objects.filter(playerID=winnerID)
    winnername = ""
    for x in player:
        winnername = x
    g.save()

    if total >= 50:
        GamePlayer.objects.filter(playerID = winnerID).update(Star = F('Star') + 1)
        GameSet.objects.filter(gameID=gameid).update(gameOver = True)

    return render(request=request, template_name="congrats.html", context={
        'winner': winnername,
        'score': score,
        'gameid' : gameid,
    })
