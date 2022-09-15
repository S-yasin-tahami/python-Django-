from django.shortcuts import render
from .form import SignUpForm,LoginFrom
from .models import User
from re import *
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        signup = SignUpForm(request.POST)
        if signup.is_valid():
            new_user = signup.cleaned_data
            if User.objects.filter(username=new_user['username']).exists():
                messages.error(request, 'username already exist', 'username_message')
            else:
                if new_user['password'] == new_user['confirm_password']:
                    User.objects.create(name = new_user['name'], email = new_user['email'], username = new_user['username'], password = new_user['password'])                                                                                                                               
                    messages.success(request, 'your account registered', 'registered_message') 
                else:
                    messages.error(request, 'password doesn\'t match', 'password_message')                
    else:
        signup = SignUpForm()
    return render(request, 'signup.html', {'signup':signup})


def login(request):
    if request.method == "POST":
        Login = LoginFrom(request.POST)
        if Login.is_valid():
            user = Login.cleaned_data
            if User.objects.filter(username=user['username']).exists():
                user_info = User.objects.filter(username=user['username'] , password=user['password']).values('name')
                if user_info.exists():
                    messages.success(request, 'welcome  {}'.format(user_info[0]['name'] ) , 'welcome_message')
                else:
                    messages.error(request, 'wrong password', 'password_message')
            else:
                messages.error(request, 'username doesn\'t exist', 'username_message')    
    else:
        Login = LoginFrom()
    return render(request, 'login.html',{'Login':Login})