from django.http import JsonResponse
# from django.shortcuts import render


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

