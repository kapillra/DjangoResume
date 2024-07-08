from django.shortcuts import render, redirect
from .models import *
from random import randint

default_data = {
    'site_name': 'ResumeBuilder',
    'auth_pages': ['login_page', 'register_page', 'reset_password_page']
}

def login_page(request):
    default_data['current_page'] = 'login_page'
    return render(request, "login_page.html", default_data)

# register page view
def register_page(request):
    default_data['current_page'] = 'register_page'
    return render(request, "register_page.html", default_data)

# reset password page view
def reset_password_page(request):
    default_data['current_page'] = 'reset_password_page'
    return render(request, "reset_password_page.html", default_data)

# profile page view
def profile_page(request):
    if 'email' not in request.session:
        return redirect(login_page)
    
    load_user_data(request) # calling the load user data function
    default_data['current_page'] = 'profile_page'
    return render(request, "profile_page.html", default_data)


# function to create username
def create_username(email):
    r = randint(1000, 9999)
    email = email.split("@")[0]
    print(f"{email}{r}")
    return f"{email}{r}"

# register functionality
def register(request):
    master = Master.objects.create(Email = request.POST['email'], Password=request.POST['password'])
    username = master.Email.split("@")[0]
    try:
        UserProfile.objects.create(Master = master, Username=username)
    except Exception as err:
        username = create_username(master.Email)
        UserProfile.objects.create(Master = master, Username=username)
    print('succesfully registered.')
    return redirect(login_page)

# load user data
def load_user_data(request):
    master = Master.objects.get(Email = request.session['email'])
    user = UserProfile.objects.get(Master = master)

    default_data['user_data'] = user

# login functionality
def login(request):
    master = Master.objects.get(Email = request.POST['email'], Password=request.POST['password'])
    user = UserProfile.objects.get(Master = master)
    request.session['email'] = master.Email

    return redirect(profile_page)

# profile update
def profile_update(request):
    master = Master.objects.get(Email = request.session['email'])
    user = UserProfile.objects.get(Master = master)

    user.FullName = request.POST['full_name']
    try:
        user.Username = request.POST['username']
    except Exception as err:
        print('username already taken.')

    user.BirthDate = request.POST['birth_date']
    user.Gender = request.POST['gender']
    user.Mobile = request.POST['mobile']
    user.Pincode = request.POST['pincode']
    user.City = request.POST['city']
    user.State = request.POST['state']
    user.Country = request.POST['country']
    user.Address = request.POST['address']

    user.save()

    # print(request.POST)

    return redirect(profile_page)

# add education
def add_education(request):
    master = Master.objects.get(Email=request.session['email'])
    user = UserProfile.objects.get(Master = master)
    
    Education.objects.create(
        UserProfile = user,
        Course = request.POST['course'],
        Standard = request.POST['class_standard'],
        BoardUniversity = request.POST['board_university'],
        StartDate = request.POST['start_date'],
        EndDate = request.POST['end_date'],
        IsContinue = True if 'is_continue' in request.POST else False
    )

    return redirect(profile_page)


# change passsword

def change_password(request):
    master = Master.objects.get(Email = request.session['email'])

    if master.Password == request.POST['old_password']:
        if request.POST['new_password'] == request.POST['repeat_password']:
            master.Password = request.POST['new_password']
            master.save()
        else:
            print('New password and repeat password must be same.')
    else:
        print('your current password did not matched.')

    return redirect(profile_page)

# logout
def logout(request):
    if 'email' in request.session:
        del request.session['email']
    return redirect(login_page)