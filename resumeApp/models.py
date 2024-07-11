from django.db import models

class Master(models.Model):
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=20)

    class Meta:
        db_table = 'master'

    def __str__(self) -> str:
        return self.Email

gender_choices = (
    ('m', 'male'),
    ('f', 'female'),
)
class UserProfile(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=100, blank=True, null=True, default='')
    Username = models.CharField(max_length=100, blank=True, unique=True)
    About = models.TextField(max_length=255, blank=True, null=True, default='')
    Gender = models.CharField(choices=gender_choices, max_length=100, blank=True, null=True, default='')
    BirthDate = models.DateField(default="2000-01-01")
    Mobile = models.CharField(max_length=10, blank=True, null=True, default='')
    City = models.CharField(max_length=50, blank=True, null=True, default='')
    State = models.CharField(max_length=50, blank=True, null=True, default='')
    Country = models.CharField(max_length=50, blank=True, null=True, default='')
    Pincode = models.CharField(max_length=10, blank=True, null=True, default='')
    Address = models.TextField(max_length=255, blank=True, null=True, default='')

    class Meta:
        db_table = 'userprofile'

    def __str__(self) -> str:
        return self.FullName if self.FullName else 'Guest'

class Experience(models.Model):
    UserProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    JobTitle = models.CharField(max_length=100)
    Company = models.CharField(max_length=100)
    StartDate = models.DateField()
    EndDate = models.DateField()
    IsContinue = models.BooleanField(default=False)

    class Meta:
        db_table = 'experience'

    def __str__(self) -> str:
        return self.Company

class Education(models.Model):
    UserProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Course = models.CharField(max_length=255)
    Standard = models.CharField(max_length=255)
    BoardUniversity = models.CharField(max_length=255)
    StartDate = models.DateField()
    EndDate = models.DateField()
    IsContinue = models.BooleanField(default=False)

    class Meta:
        db_table = 'education'

class Project(models.Model):
    UserProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    ProjectName = models.CharField(max_length=255)
    Company = models.CharField(max_length=100)
    StartDate = models.DateField()
    EndDate = models.DateField()
    IsContinue = models.BooleanField(default=False)

    class Meta:
        db_table = 'project'

    def __str__(self) -> str:
        return self.ProjectName

skill_level = (
    ('40', 'beginner'),
    ('65', 'intermediate'),
    ('100', 'advance')
)
class Skill(models.Model):
    UserProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Level = models.CharField(choices=skill_level, max_length=25)

    class Meta:
        db_table = 'skill'