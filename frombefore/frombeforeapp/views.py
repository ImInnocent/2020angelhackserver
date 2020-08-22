from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.views import generic
from django.core import serializers
from django.db.models import Max
from .models import Message, UserData
import random
import json
from django.views.decorators.csrf import csrf_exempt

def standardResponse(json):
    return JsonResponse(json.dumps(message.as_dict(), ensure_ascii=False), safe=False)

def standardRequest(jsonStr):
    return json.loads(jsonStr.decode('utf8').replace("'", '"'))

# Create your views here.
@csrf_exempt
def message(request):
    if request.method == "POST":
        try:
            json_body = standardRequest(request.body)
            dday = json_body.get('dday')
            text = json_body.get('text')
            subject = json_body.get('subject')

            new_message = Message(dday=dday, text=text, subject=subject)
            new_message.save()
        except ObjectDoesNotExist:
            return Http404("dday or text not exist")

        return HttpResponse("ok")
    else:
        target_dday = int(request.GET.get('dday', '-1'))
        # default to 
        target_subject = request.GET.get('subject', 'college')

        message = None

        if target_dday >= 0:         
            message = Message.objects.filter(dday=target_dday, subject=target_subject).order_by("?").first()

            if message is None:
                message = Message.objects.filter(subject=target_subject).order_by("?").first()

            if message is None:
                message = Message.objects.all().order_by("?").first()
        else:
            max_id = Message.objects.all().aggregate(max_id=Max("id"))['max_id']

            while True:
                pk = random.randint(1, max_id)
                message = Message.objects.filter(subject=target_subject).first()

                if message is not None:
                    break

        return standardResponse(json)
        # return JsonResponse(json.dumps(message.as_dict(), ensure_ascii=False), safe=False)
        # return render(request, 'frombeforeapp/index.html', { 'message': message })

@csrf_exempt
def user(request):
    if (request.method == "GET"):
        target_uuid = request.GET.get("uuid", "none")
        target_user = get_object_or_404(UserData, pk=target_uuid)

        return standardResponse(target_user)
    else:
        try:
            json_body = standardRequest(request.body)
            uuid = json_body.get('uuid')
            subject = json_body.get('subject')

            new_user = UserData(uuid=uuid, subject=subject)
            new_user.save()
        except ObjectDoesNotExist:
            return Http404("dday or text not exist")

        return HttpResponse("ok")

@csrf_exempt
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
