from django.shortcuts import render, redirect
from .models import *
from random import randint
from datetime import date, datetime

default_data = {
    'site_name': 'ResumeBuilder',
    'auth_pages': ['login_page', 'register_page', 'reset_password_page'],
    'skill_level': skill_level,
}

def login_page(request):
    if 'email' in request.session:
        return redirect(profile_page)
    
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
    education = Education.objects.filter(UserProfile=user)
    experience = Experience.objects.filter(UserProfile=user)
    projects = Project.objects.filter(UserProfile=user)
    skills = Skill.objects.filter(UserProfile=user)

    default_data['user_data'] = user
    default_data['education'] = education
    default_data['experience'] = experience
    default_data['projects'] = projects
    default_data['skills'] = skills

    print(default_data['education'])

# login functionality
def login(request):
    master = Master.objects.get(Email = request.POST['email'], Password=request.POST['password'])
    user = UserProfile.objects.get(Master = master)
    request.session['email'] = master.Email

    return redirect(profile_page)

# photo upload
def profile_photo_upload(request):
    master = Master.objects.get(Email = request.session['email'])
    user = UserProfile.objects.get(Master = master)

    if 'profile_image' in request.FILES:
        user.ProfileImage = request.FILES['profile_image']
        user.save()

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

# edit education
def edit_education(request, id):
    edit_edu_data = Education.objects.get(id=id)

    edit_edu_data.StartDate = edit_edu_data.StartDate.strftime("%Y-%m-%d")
    edit_edu_data.EndDate = edit_edu_data.EndDate.strftime("%Y-%m-%d")
    default_data['edit_edu_data'] = edit_edu_data

    return redirect(profile_page)

# edit cancel
def edit_edu_cancel(request):
    if 'edit_edu_data' in default_data:
        del default_data['edit_edu_data']

    return redirect(profile_page)

# edit education save
def edit_education_save(request, id):
    education = Education.objects.get(id=id)
    education.Course = request.POST['course']
    education.Standard = request.POST['class_standard']
    education.BoardUniversity = request.POST['board_university']

    education.StartDate = request.POST['start_date']

    education.EndDate = request.POST['end_date']
    education.IsContinue = True if 'is_continue' in request.POST else False

    print(education)
    education.save()

    if 'edit_edu_data' in default_data:
        del default_data['edit_edu_data']

    return redirect(profile_page)

# delete education
def delete_education(request, id):
    Education.objects.get(id=id).delete()

    return redirect(profile_page)

# add experience
def add_experience(request):
    master = Master.objects.get(Email=request.session['email'])
    user = UserProfile.objects.get(Master = master)
    
    Experience.objects.create(
        UserProfile = user,
        JobTitle = request.POST['job_title'],
        Company = request.POST['company'],
        StartDate = request.POST['start_date'],
        EndDate = request.POST['end_date'],
        IsContinue = True if 'is_continue' in request.POST else False
    )

    return redirect(profile_page)

# edit experience
def edit_experience(request, id):
    edit_exp_data = Experience.objects.get(id=id)
    edit_exp_data.StartDate = edit_exp_data.StartDate.strftime("%Y-%m-%d")
    edit_exp_data.EndDate = edit_exp_data.EndDate.strftime("%Y-%m-%d")
    default_data['edit_exp_data'] = edit_exp_data

    return redirect(profile_page)

# edit cancel
def edit_exp_cancel(request):
    if 'edit_exp_data' in default_data:
        del default_data['edit_exp_data']

    return redirect(profile_page)

# edit experience save
def edit_experience_save(request, id):
    experience = Experience.objects.get(id=id)
    experience.JobTitle = request.POST['job_title']
    experience.Company = request.POST['company']

    experience.StartDate = request.POST['start_date']
    experience.EndDate = request.POST['end_date']
    experience.IsContinue = True if 'is_continue' in request.POST else False

    print(experience)
    experience.save()

    if 'edit_exp_data' in default_data:
        del default_data['edit_exp_data']

    return redirect(profile_page)

# delete experience
def delete_experience(request, id):
    Experience.objects.get(id=id).delete()
    return redirect(profile_page)

# add experience
def add_project(request):
    master = Master.objects.get(Email=request.session['email'])
    user = UserProfile.objects.get(Master = master)
    
    Project.objects.create(
        UserProfile = user,
        ProjectName = request.POST['project_name'],
        Company = request.POST['company'],
        StartDate = request.POST['start_date'],
        EndDate = request.POST['end_date'],
        IsContinue = True if 'is_continue' in request.POST else False
    )

    return redirect(profile_page)

# edit experience
def edit_project(request, id):
    project = Project.objects.get(id=id)
    project.StartDate = project.StartDate.strftime("%Y-%m-%d")
    project.EndDate = project.EndDate.strftime("%Y-%m-%d")
    default_data['edit_proj_data'] = project

    return redirect(profile_page)

# edit cancel
def edit_proj_cancel(request):
    if 'edit_proj_data' in default_data:
        del default_data['edit_proj_data']

    return redirect(profile_page)

# edit project save
def edit_project_save(request, id):
    project = Project.objects.get(id=id)
    project.ProjectName = request.POST['project_name']
    project.Company = request.POST['company']

    project.StartDate = request.POST['start_date']
    project.EndDate = request.POST['end_date']
    project.IsContinue = True if 'is_continue' in request.POST else False

    print(project)
    project.save()

    if 'edit_proj_data' in default_data:
        del default_data['edit_proj_data']

    return redirect(profile_page)

# delete project
def delete_project(request, id):
    Project.objects.get(id=id).delete()
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

# add skills
def add_skills(request):
    master = Master.objects.get(Email=request.session['email'])
    user = UserProfile.objects.get(Master = master)

    Skill.objects.create(
        UserProfile = user,
        Name = request.POST['skill_name'],
        Level = request.POST['level']
    )

    return redirect(profile_page)

# delete skill
def delete_skill(request, id):
    Skill.objects.get(id=id).delete()
    return redirect(profile_page)

# logout
def logout(request):
    if 'email' in request.session:
        del request.session['email']
    return redirect(login_page)