from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login 
# Create your views here.

class SignInView(View):

    def get(self, request):
        return render(request, 'observe_login/signin.html')

    def post(self, request):
        email = request.POST["email"]
        password = request.POST["password"]
        user_obj = authenticate(request=request, email=email, password=password)
        print("認証されればUserオブジェクト、失敗ならNoneの表示 : ",user_obj)
        if user_obj:
            login(request, user_obj)
        return render(request, 'observe_login/signin.html')