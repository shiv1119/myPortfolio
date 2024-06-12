from django.db import models
from django.utils.text import slugify
from django.conf import settings


class Tag(models.Model):
    value = models.TextField(max_length=500)
    
    
    def __str__(self):
        return self.value


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=None)
    title = models.CharField(max_length=200)
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(auto_now_add=True, null=True)
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name="posts")
    is_liked = models.BooleanField(default=False)
    
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    
    
    
    
class AuthorProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        ('P', 'Prefer Not To Say'),
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="profile"
    )
    bio = models.TextField()
    profile_image = models.ImageField(upload_to="profile_image/", blank=True, null=True)
    user_date_of_birth = models.DateField(blank=True, null=True)
    user_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    portfolio_link = models.URLField(max_length=200, blank=True, null=True)
    
    
    
    def __str__(self):
        return f"Profile of {self.user.username}"
    

class Skill(models.Model):
    skills_value = models.TextField(max_length=500)
    
    
    def __str__(self):
        return self.skills_value
    
    
class  WorkExperience(models.Model):
    WORKING_TIME_CHOICES = (
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Freelance', 'Freelance'),
    )
    
    WORKING_TYPE_CHOICES = (
        ('Remote', 'Remote'),
        ('On-Site', 'On-Site'),
        ('Hybrid', 'Hybrid'),
    )
    author_profile = models.ForeignKey(AuthorProfile, on_delete=models.CASCADE, related_name="work_experiences")
    work_title = models.CharField(max_length=400)
    company_name = models.CharField(max_length=250)
    company_logo = models.ImageField(upload_to="company_logo_image/", blank=True, null=True)
    company_portfolio_link = models.URLField(max_length=200, blank=True, null=True)
    working_time = models.CharField(max_length=10, choices=WORKING_TIME_CHOICES)
    working_type = models.CharField(max_length=7, choices=WORKING_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name="work_experiences")
    activities_responsibilities = models.TextField(blank=True, null=True)
    
    
    def __str__(self):
        return self.work_title
    
    
class Education(models.Model):
    author_profile = models.ForeignKey(AuthorProfile, on_delete=models.CASCADE, related_name="educations")
    school_title = models.CharField(max_length=400)
    degree = models.CharField(max_length=400)
    field_of_study = models.CharField(max_length=400)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    grade = models.CharField(max_length=100)
    activities_and_societies = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name="educations")
    
    def __str__(self):
        return self.school_title