from django.shortcuts import render, redirect
from . models import Event
from django.contrib.auth import authenticate , login , logout
from. forms import LoginForm, UserRegistrationForm

from . forms import EventForm

# Create your views here.


def Home_view(request):
    data=Event.objects.all()
    context={'data':data}
    return render(request, "EventApp/home.html", context)

def userlogin_view(request):
    form = LoginForm()
    context = {"form":form}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username , password = password)
        if user:
            login(request,user)
            return redirect("home")

    return render(request, "EventApp/userlogin.html", context)





def register(request):
    form = UserRegistrationForm()
    context = {'form': form}
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    
    return render(request, 'EventApp/registration.html',context )


def signout_view(request):
    logout(request)
    return redirect('home')

def addevent(request):
    forms = EventForm(request.POST, request.FILES)
    if request.method == 'POST':
        print("request posted")
        if forms.is_valid():
            print("form is valid")
            forms.save()
            print("form is saved")
            return redirect("home")
            
        else:
            print("form is not valid")
            
        
            
    context = {'forms':forms}
    return render(request, 'EventApp/addevent.html', context )
