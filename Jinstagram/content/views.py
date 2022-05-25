from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed


class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id')
        for feed in feed_list:
            print(feed)


        return render(request, "jinstagram/main.html", context=dict(feeds=feed_list))