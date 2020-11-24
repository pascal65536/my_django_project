from django.shortcuts import render
from django.http import HttpResponse

from .forms import InputForm
from .models import Message

DIRNAME = 'web_form'


def list_forms(request):
    list_obj = Message.objects.all()
    return render(request, DIRNAME + '/list.html', {'list': list_obj})


def form_create(request):
    obj = InputForm(request.POST or None)
    reset = False

    if request.method == "POST":
        if obj.is_valid():
            obj.save()
            title = request.POST.get("user_name")
            return HttpResponse("Сообщение " + title + " отправленно!")
        else:
            reset = True
            return render(request, DIRNAME + '/create.html', {'form': obj, 'reset': reset})
    else:
        return render(request, DIRNAME + '/create.html', {'form': obj, 'reset': reset})


def form(request, form_id):
    try:
        obj = Message.objects.get(id=form_id)
    except:
        return HttpResponse("Статья не найденна!")
    return render(request, DIRNAME + '/form.html', {'form': obj})