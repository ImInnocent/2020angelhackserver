from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.core import serializers
from .models import Message

# Create your views here.
class IndexView(generic.ListView):
    def get(self, request):
        # messages = serializers.serialize('json', Message.objects.all()[:5])
        messages = [dict(m) for m in Message.objects.all()[:5].values()]

        return render(request, 'frombeforeapp/index.html', { 'messages': messages })
        # return JsonResponse(messages, safe=False)

    def post(self, request):
        print("Post 요청을 잘받았다")
        return HttpResponse("Post 요청을 잘받았다")

    def put(self, request):
        return HttpResponse("Put 요청을 잘받았다")

    def delete(self, request):
        return HttpResponse("Delete 요청을 잘받았다")