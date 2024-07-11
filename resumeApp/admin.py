from django.contrib import admin
from .models import *

admin.site.site_header = admin.site.site_title = "ResumeBuilder"
admin.site.register(Master)
admin.site.register(UserProfile)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Project)