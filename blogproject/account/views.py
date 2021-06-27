from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm


def login_view(request):
    # AuthenticationForm : 장고에서 제공하는 로그인 기능 폼
    if request.method =='POST':  # 유효성 검사
        form = AuthenticationForm(request=request, data= request.POST)
        if form.is_valid():  # 데이터가 유효하다면
            username = form.cleaned_data.get("username")
            # cleaned_data : 검증에 통과한 값을 사전 타입으로 만듦
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:    # 유저가 데이터에 존재한다면
                login(request, user)
        return redirect('home')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request) # 장고에서 제공하는 로그아웃 기능
    return redirect('home')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("home")
    else:
        form = SignupForm() # 장고에서 제공하는 회원가입 폼
        return render(request, 'signup.html',{'form':form})
