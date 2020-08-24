from django.http import JsonResponse
from django.shortcuts import render
from .models import WaitingRoom, InGame, WinnerList


def test_view(request):
    data = {
        'status': False,
        'waitingRoom': [
            'Thierry',
            'Nekroface',
            'WOoOinux',
            'JC_onLine'
        ]
    }
    return JsonResponse(data)


def status_display(request):
    in_game = InGame.objects.all()
    waiting_room = WaitingRoom.objects.all()
    winner_list = WinnerList.objects.all()
    context = {
        'status': True,
        'in_game': in_game,
        'waiting_room': waiting_room,
        'winner_list': winner_list
    }
    return render(request,
                  'home.html',
                  context)

