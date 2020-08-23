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
    waiting_room = WaitingRoom.objects.get()
    in_game = InGame.objects.get()
    winner_list = WinnerList.objects.get()
    context = {
        'waiting_room': waiting_room,
        'in_game': in_game,
        'winner_list': winner_list
    }
    return render(request,
                  'reporting/template/activity_template_details.html',
                  context)

