from django.shortcuts import render
from django.http import HttpResponse

from .forms import InputForm

DIRNAME = 'web_form'

def sendMessage(request):
    form = InputForm(request.POST or None)
    reset = False

    if request.method == "POST":
        if form.is_valid():
            name = request.POST.get("userName")
            return HttpResponse("Сообщение пользователя " + name + " отправленно!")
        else:
            reset = True
            return render(request, DIRNAME + '/form.html', {'form': form, 'reset': reset})

    else:
        return render(request, DIRNAME + '/form.html', {'form': form, 'reset': reset})