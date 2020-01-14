from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from floyd_warshall.algo.algo import launch_floyd_warshall
import json


def home(request):
    return redirect('/authenticate')


@csrf_exempt
def handle_auth(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            d = form.cleaned_data
            user = authenticate(username=d['username'], password=d['password'])
            if user is not None:
                login(request, user)
                return HttpResponse('OK', status=200)
            return HttpResponse('Unauthorized', status=401)
        return HttpResponse('Bad request', status=400)
    else:
        form = AuthenticationForm()
        return render(request, 'auth.html', {'form': form})


def handle_logout(request):
    logout(request)
    return redirect('/authenticate')


@require_http_methods(["POST"])
def floyd_warshall(request):
    if not request.user.is_authenticated:
        return HttpResponse('Unauthorized', status=401)
    data = json.loads(request.body)
    if 'data' not in data:
        return HttpResponse("Couldn't find \"data\" field in request body", status=400)
    csv = data['data']
    return HttpResponse(launch_floyd_warshall(csv))
