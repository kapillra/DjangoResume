from django.urls import path
from .views import *

urlpatterns = [
    path('', login_page, name="login_page"),
    path('register_page/', register_page, name="register_page"),
    path('reset_password_page/', reset_password_page, name="reset_password_page"),
    path('profile_page/', profile_page, name="profile_page"),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('profile_update/', profile_update, name="profile_update"),
    path('profile_photo_upload/', profile_photo_upload, name="profile_photo_upload"),
    path('change_password/', change_password, name="change_password"),
    
    path('add_education/', add_education, name="add_education"),
    path('delete_education/<int:id>/', delete_education, name="delete_education"),
    path('edit_education/<int:id>/', edit_education, name="edit_education"),
    path('edit_education_save/<int:id>/', edit_education_save, name="edit_education_save"),
    path('edit_edu_cancel/', edit_edu_cancel, name="edit_edu_cancel"),
    
    path('add_experience/', add_experience, name="add_experience"),
    path('edit_experience/<int:id>/', edit_experience, name="edit_experience"),
    path('edit_experience_save/<int:id>/', edit_experience_save, name="edit_experience_save"),
    path('delete_experience/<int:id>/', delete_experience, name="delete_experience"),
    path('edit_exp_cancel/', edit_exp_cancel, name="edit_exp_cancel"),
    
    path('add_project/', add_project, name="add_project"),
    path('edit_project/<int:id>/', edit_project, name="edit_project"),
    path('edit_project_save/<int:id>/', edit_project_save, name="edit_project_save"),
    path('delete_project/<int:id>/', delete_project, name="delete_project"),
    path('edit_proj_cancel/', edit_proj_cancel, name="edit_proj_cancel"),
    
    path('add_skills/', add_skills, name="add_skills"),
    path('delete_skill/<int:id>/', delete_skill, name="delete_skill"),

    # resumen viewer url
    path('resume_viewer_page/@<str:username>/', resume_viewer_page, name="resume_viewer_page"),
]