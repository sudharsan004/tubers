from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contact_tuber.models import ContactInfo
# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Validation
        if (User.objects.filter(username=user_name).exists() or User.objects.filter(email=email).exists()):
            messages.warning(
                request, 'A user with User-name / Email already exists.')
            return redirect('register')
        else:
            if(password != confirm_password):
                messages.warning(request, 'Passwords do not match.')
                return redirect('register')
            elif (len(password) < 6):
                messages.warning(
                    request, 'Password must be atleast 6 characters')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=user_name,
                                                email=email, password=password)
                user.save()
                messages.success(request, 'Account created')
                return redirect('login')
    return render(request, 'user_accounts/register.html')


def login(request):
    if request.method == "POST":
        user_name = request.POST['user_name']
        password = request.POST['password']

        user = auth.authenticate(username=user_name, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login Success')
            return redirect('dashboard')
        else:
            messages.error(request, 'Wrong User Name/Password ')
            return redirect('login')

    return render(request, 'user_accounts/login.html')


# Django already has a build in logout method so give some other name to logout function
def logout_user(request):
    logout(request)
    messages.info(request, 'Successfully Logged out!')
    return redirect('home')


@login_required(login_url='login')
def dashboard(request):
    userid = request.user.id
    print(userid)
    contacted_ytubers = ContactInfo.objects.filter(
        user_id=6).values_list('ytuber_contacted', flat=True).distinct()
    data = {'ytubers': contacted_ytubers}
    return render(request, 'user_accounts/dashboard.html', data)


def create_new_user(request, un):
    password = '123456'
    if (User.objects.filter(username=un).exists()):
        messages.success(
            request, f'''Welcome {un}!''')
        return redirect('home')
    else:
        user = User.objects.create_user(username=un, password=password)
        user.save()
        messages.success(
            request, f'''Welcome {un}!, your username: "{un}"  password: "123456" ''')
        return redirect('home')
