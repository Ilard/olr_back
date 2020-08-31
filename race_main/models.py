from django.db import models


class InGame(models.Model):
    name = models.CharField(default='', max_length=20)
    # player2_name = models.CharField(default='', max_length=20)
    # player3_name = models.CharField(default='', max_length=20, blank=True)
    # player4_name = models.CharField(default='', max_length=20, blank=True)

    def __str__(self):
        return f"{self.name} "


class WaitingRoom(models.Model):
    name = models.CharField(default='No name', max_length=20)
    in_comming_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class WinnerList(models.Model):
    name = models.CharField(default='', max_length=20)

    def __str__(self):
        return f"{self.name}"
