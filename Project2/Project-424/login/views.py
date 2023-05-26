from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def logina(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') # replace 'home'with the name of your home page URL pattern
        else:
            # handle invalid login credentials
            pass
    else:
        return render(request, 'login/loginH.html')



