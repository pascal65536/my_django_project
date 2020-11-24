from django.shortcuts import render
from django.http import HttpResponse

from .forms import Form

DIRNAME = "web_form"

def form(request):
    reset = False
    form = Form(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            name = request.POST.get("field")
            return HttpResponse("Сообщение " + name + " отправленно!")
        else:
            reset = True
            return render(request, DIRNAME + '/form.html', {'form': form, 'reset': reset})

    else:
        return render(request, DIRNAME + '/form.html', {'form': form, 'reset': reset})