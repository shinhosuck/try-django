from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm



'''
messages.debug(request, '%s SQL statements were executed.' % count)
messages.info(request, 'Three credits remain in your account.')
messages.success(request, 'Profile details updated.')
messages.warning(request, 'Your account expires in three days.')
messages.error(request, 'Document deleted.')
'''

def register_view(request):
    form = UserCreationForm()
    context = {"form": form}
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            form.save()
            return redirect("users:login")
    return render(request, "users/register.html", context)

def login_view(request):
    # can check user status here or in the login template
    # if request.user.is_authenticated:
    #     messages.warning(request, "You are logged in already!")
    #     return redirect("articles:home")
    # if request.method == "POST":
    #     username = request.POST.get("username")
    #     password = request.POST.get("password")
    #     if username and password:
    #         # user_exist = User.objects.filter(username__exact=username).first()
    #         user = authenticate(request, username=username, password=password)
    #         # this checks user's credential
    #         if user:
    #             login(request, user)
    #             messages.success(request, "Succefully logged in!")
    #             return redirect("articles:home")
    #         else:
    #             messages.error(request, "Username or password did not match!")
    #             return render(request, "users/login.html", context=None)
    #     else:
    #         messages.error(request, "Username and password cannot be empty!")
    #         return redirect("users:login")
    # else:
    #     return render(request, "users/login.html", context=None)
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("articles:home")
        else:
            context = {"form": form}
            return render(request, "users/login.html", context)

    form = AuthenticationForm(request)
    context = {"form": form}
    return render(request, "users/login.html", context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.warning(request, "You are logged out!")
        return redirect("users:login")
    else:
        return render(request, "users/logout.html", context=None)
