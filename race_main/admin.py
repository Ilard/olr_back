from django.contrib import admin
from .models import WaitingRoom, InGame, WinnerList


admin.site.register(WaitingRoom)
admin.site.register(InGame)
admin.site.register(WinnerList)

