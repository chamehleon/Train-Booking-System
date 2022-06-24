from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .forms import UserUpdateForm
from django.contrib import messages
from django.http import JsonResponse
from .models import *
from .forms import *
def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirm_password']
        if password == confirmPassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'this Email is alread used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'this username is alread used')
                return redirect('register')

            else:
                if 'Admin' in request.POST:
                    data=User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                    data.is_staff=True
                    data.is_admin=True
                    data.is_superuser=True
                    data.save()
                   # messages.info(request,'now you have account')
                    return redirect('signin')
                else:
                    data=User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                    data.save()
                    messages.info(request,'now you have account')
        else:
            messages.info(request,'your confirm password is not correct')
            return redirect('register')
        return redirect('signin')
    else:
        return render(request,'customers/sign-up.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        data =auth.authenticate(username=username, password=password)
        
        if data is not None:
            auth.login(request,data)
            if  data.is_superuser == True:
                return redirect('index')
            else:
                return redirect('home')
            
        else: 
            messages.info(request,'the username or password is incorrect')
            return redirect('signin')
    else: 
        return render(request,'customers/sign-in.html')

def home(request):
    return render(request,'customers/home_user.html')
def user_enter(request):
    if request.is_ajax():
        return render(request ,'home.html')
    else:
        return render(request,'home.html')
def logout_user(request):
    auth.logout(request)
    return redirect('signin')
def userupdate(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance= request.user)
        if user_form.is_valid:
            user_form.save()
            
            messages.success(request, 'your data is updata successfully')
            return redirect('home')
        else:
            messages.info(request, 'there is/are feilds empty please check')
            return redirect('update')

    else:
        user_form = UserUpdateForm(instance=request.user)

    return render(request, 'customers/Updating-profile.html')
def check_user_register(request):
    username = request.GET.get('username')
    is_taken = User.objects.filter(username__iexact=username,).exists()
    data = {'is_taken':is_taken}
    if data['is_taken']: 
        data['error_message'] = "The username already taken"
    return JsonResponse(data)
def check_user_login(request):
    username = request.GET.get('username')
    is_taken = User.objects.filter(username__iexact=username,).exists()
    data = {'is_taken':is_taken}
    if data['is_taken']: 
        data['error_message'] = ""
    else:
        data['error_message'] = "The username is wrong"
    return JsonResponse(data)

