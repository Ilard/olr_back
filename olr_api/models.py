from django.db import models


class WaitingRoom(models.Model):
    name = models.CharField(default='No name', max_length=20)
    in_comming_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class InGame(models.Model):
    player1_name = models.CharField(default='', max_length=20)
    player2_name = models.CharField(default='', max_length=20)

    def __str__(self):
        return f"{self.player1_name} {self.player1_name}"


class WinnerList(models.Model):
    name = models.CharField(default='', max_length=20)

    def __str__(self):
        return f"{self.name}"
