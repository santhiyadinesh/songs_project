
from django.shortcuts import render,redirect
from .models import Songs
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import UserCreationForm


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import ReviewForm
from .forms import profileForm
from .models import Review  
from.models import UserProfile

 


# Create your views here.

def home(request):
    ab = Songs.objects.all()
    return render (request,'base.html',{'ab':ab})  

def playsong(request,name):
 if request.user.is_authenticated:
         ca = Songs.objects.get(name=name)
         return render (request,'play.html',{'ca':ca})
 else:
        return redirect("login")


def revsong(request):
    return render(request,'review.html')

def about(request):
    return render(request,'about.html')

def help(request):
    return render(request,'help.html')

def center(request):
    return render(request,'center.html')

def price(request):
    return render(request,'price.html')

def account(request):
    return render(request,'account.html')


def output(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form has been submitted successfully')
            return redirect(output)  
    else:
        form = ReviewForm()

    ca = Review.objects.all()
    return render(request, 'output.html', {'form': form, 'ca': ca})




@login_required(login_url='login') 
def profilepage(request):
    if request.method == 'POST':
        form = profileForm(request.POST)
        if form.is_valid():
       
            profile = form.save(commit=False)
            profile.user = request.user  
            profile.save()
            
            messages.success(request, 'Form has been submitted successfully')
            return redirect(profilepage)  
    else:
        form = profileForm()


    ca = UserProfile.objects.filter(user=request.user).first()
    
    return render(request, 'profile.html', {'form': form, 'ca': ca})



def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username,password = raw_password)
            login(request, user)
            return redirect(loginpage)
             
    else:

        form = UserCreationForm()
       
    return render(request,'register.html',{'form':form}) 


def loginpage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,'user has been created')
            return redirect(home)
           
        else:
            messages.error(request,'no such user')
            return redirect(register)

    return render(request,'login.html')

def outlog(request):
    logout(request)
    messages.success(request,'user has been logout successfully')
    return render(request,'logout.html')

def SearchResultsList(request):
    if request.method == "GET":
        searched = request.GET.get('searched')
        song = Songs.objects.filter(name__contains =searched)
        return render(request, 'search.html',{'searched':searched, 'song':song})
    else:
        return render(request, 'search.html',{})