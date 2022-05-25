from django.shortcuts import render
from rest_framework.views import APIView

class Sub2(APIView):
    def get(self, request):
        return render(request,"myapp/main.html")

    def post(self, request):
        return render(request,"myapp/main.html")    
