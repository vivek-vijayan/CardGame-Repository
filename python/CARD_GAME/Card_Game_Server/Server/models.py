
from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.


class GamePlayer(models.Model):
    playerID = models.AutoField(primary_key=True)
    playerName = models.CharField(max_length=200)
    playerPhoto = models.CharField(max_length=200, default="")
    Star = models.IntegerField()

    def __str__(self) -> str:
        return str(self.playerName)


class GameSet(models.Model):
    gameID = models.AutoField(primary_key=True)
    gameName = models.CharField(max_length=200)
    gameStarted = models.DateTimeField(auto_now=True)
    gameEnded = models.DateTimeField()
    gameOver = BooleanField(default=False)

    def __str__(self) -> str:
        return (str(self.gameID) + ' - ' + str(self.gameName) + ' Started on ' + str(self.gameStarted))


class GamePlay(models.Model):
    gameplayID = models.AutoField(primary_key=True)
    gameID = models.ForeignKey(GameSet, on_delete=models.CASCADE)
    playerID = models.ForeignKey(GamePlayer, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self) -> str:
        return (str(self.gameplayID) + " -> Game ID : " + str(self.gameID) + " --> Player ID : " + str(self.playerID))
