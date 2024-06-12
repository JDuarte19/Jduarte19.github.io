from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .forms import AccountForm
from .models import Account

# Create your views here.
"""
There are two types of view types.

Function based views

Class based views

# using https://fontawesome.com/search?o=r&c=editing for icons
# using https://bootswatch.com/solar/ for css and js
# using https://www.youtube.com/watch?v=EUMpUUXKvP0&t=4953s as a tutorial for Django use


"""
# request is the http request a user used to access a webpage
def home(request):
    x = "home.html"
    return render(request, 'user_act/{}'.format(x))

def features(request):
    x = "features.html"
    return render(request, 'user_act/{}'.format(x))

def about(request):
    #extends from base.html
    x = "about.html"
    return render(request, 'user_act/{}'.format(x))

def profile(request):
    #extends base.html
    x = "profile.html"
    return render(request, 'user_act/{}'.format(x))

def admin(request):
    #extends from base.html
    x = "user_table.html"

    accounts = Account.objects.all()
    context = {}
    context['users'] = accounts

    return render(request, 'user_act/{}'.format(x),context)

def login(request):
    #should be used for token authentication 
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        return

def add_account(request):
    #extends from base.html
    #serves as new register page
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['user_name']
            email = form.cleaned_data['email']
            #pass the password to an encryption function
            password = form.cleaned_data['password']
            account = Account(user_name= username, email = email, password = password)
            account.save()
            return render(request, 'user_act/add_account.html', {'form':AccountForm(), 'success':True})
    else:
        form = AccountForm()
        return render(request, 'user_act/add_account.html', {'form':AccountForm()})

def view_account(request,id):
    account = Account.objects.get(pk=id)
    return HttpResponseRedirect(reverse('admin'))

def edit_info(request,id):
    if request.method=="POST":
        account = Account.objects.get(pk=id)
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return render(request, 'user_act/edit_info.html', {
                'form':form,
                'success':True
            })
    else:
        account = Account.objects.get(pk=id)
        form=AccountForm(instance=account)
        return render(request, 'user_act/edit_info.html',{'form':form})
    
def delete(request,id):
    if request.method == "POST":
        account = Account.objects.get(pk=id)
        account.delete()

    return HttpResponseRedirect(reverse('admin'))



def test(request):
    x = "test.html"
    #accounts = Account.objects.all()
    context = {}

    #if request.method == "POST":
        #if 'submit' in request.POST:
        #if 'delete' in request.POST:

    
    #context['form'] = form

    return render(request, 'user_act/{}'.format(x),context)