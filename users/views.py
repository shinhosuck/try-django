from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

'''
messages.debug(request, '%s SQL statements were executed.' % count)
messages.info(request, 'Three credits remain in your account.')
messages.success(request, 'Profile details updated.')
messages.warning(request, 'Your account expires in three days.')
messages.error(request, 'Document deleted.')
'''

def login_view(request):
    if request.method == "POST":
        # if not request.user.is_authenticated:
            username = request.POST.get("username")
            password = request.POST.get("password")
            if username and password:
                # user_exist = User.objects.filter(username__exact=username).first()
                user = authenticate(request, username=username, password=password)
                # this checks user's credential
                if user:
                    login(request, user)
                    # messages.success(request, "Succefully logged in!")
                    return redirect("articles:home")
                else:
                    messages.error(request, "Username or password did not match!")
                    return render(request, "users/login.html", context=None)
            else:
                messages.error(request, "Username and password cannot be empty!")
                return redirect("users:login")
        # else:
        #     messages.warning(request, "You are logged in already")
        #     return render(request, "users/login.html", context=None)
    else:
        return render(request, "users/login.html", context=None)
   
