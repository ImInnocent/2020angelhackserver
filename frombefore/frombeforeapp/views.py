from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.views import generic
from django.core import serializers
from django.db.models import Max
from .models import Message
import random

# Create your views here.
def message(request):
    if request.method == "POST":
        try:
            dday = request.POST.get('dday')
            text = request.POST.get('text')

            new_message = Message(dday=dday, text=text)
            new_message.save()
        except ObjectDoesNotExist:
            return Http404("dday or text not exist")

        return HttpResponse("ok")
    else:
        target_dday = int(request.GET.get('dday', '-1'))

        if target_dday >= 0:         
            message = Message.objects.filter(dday=target_dday).order_by("?").first()
        else:
            max_id = Message.objects.all().aggregate(max_id=Max("id"))['max_id']

            while True:
                pk = random.randint(1, max_id)
                message = Message.objects.filter(pk=pk).first()

                if message:
                    break

        return JsonResponse(json.dumps(message.as_dict(), ensure_ascii=False), safe=False)
        # return render(request, 'frombeforeapp/index.html', { 'message': message })

def test(request):
    if request.method == "POST":
        try:
            dday = request.POST.get('dday')
            text = request.POST.get('text')

            new_message = Message(dday=dday, text=text)
            new_message.save()
        except ObjectDoesNotExist:
            return Http404("dday or text not exist")

        return redirect('test')
        # return HttpResponse("ok")
    else:
        return render(request, 'frombeforeapp/test.html')
