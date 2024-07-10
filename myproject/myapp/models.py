from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django_summernote.fields import SummernoteTextField


class Tag(models.Model):
    value = models.TextField(max_length=500)
    
    
    def __str__(self):
        return self.value

class SoftSkill(models.Model):
    skills_value = models.TextField(max_length=500)
    
    def __str__(self):
        return self.skills_value
    
class TechnicalSkill(models.Model):
    skills_value = models.TextField(max_length=500)
    skills_logo = models.ImageField(upload_to="skills_logo/", blank=False)
    
    def __str__(self):
        return self.skills_value
    



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=None)
    title = SummernoteTextField()
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(auto_now_add=True, null=True)
    content = SummernoteTextField()
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
    bio = SummernoteTextField()
    profile_image = models.ImageField(upload_to="profile_image/", blank=True, null=True)
    user_date_of_birth = models.DateField(blank=True, null=True)
    user_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    technical_skills = models.ManyToManyField(TechnicalSkill, related_name="profile", blank=False)
    soft_skills = models.ManyToManyField(SoftSkill, related_name="profile", blank=False)
    github_username = models.CharField(max_length=100,blank=True, null=True)
    portfolio_link = models.URLField(max_length=200, blank=True, null=True)
    user_number = models.CharField(max_length=20, blank=True, help_text='Contact phone number', null=True)
    user_linkedin = models.URLField(blank=True, null=True)
    user_x = models.URLField(blank=True, null=True)
    user_github = models.URLField(blank=True, null=True)
    
    
    
    
    def __str__(self):
        return self.user.first_name +' ' +self.user.last_name
    


    
    
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
    technical_skills = models.ManyToManyField(TechnicalSkill, related_name="work_experiences")
    soft_skills = models.ManyToManyField(SoftSkill, related_name="work_experiences")
    activities_responsibilities = SummernoteTextField(blank=True, null=True)
    
    
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
    activities_and_societies = SummernoteTextField(blank=True, null=True)
    technical_skills = models.ManyToManyField(TechnicalSkill, related_name="educations")
    soft_skills = models.ManyToManyField(SoftSkill, related_name="educations")

    
    def __str__(self):
        return self.school_title
    
    

class Certificate(models.Model):
    author_profile = models.ForeignKey(AuthorProfile, on_delete=models.CASCADE, related_name="certificates")
    title = models.CharField(max_length=255)
    certificate_file = models.FileField(upload_to='certificates/')
    certificate_link = models.URLField(max_length=400, blank=True, null=True)
    certificate_provider_logo = models.ImageField(upload_to="certificates_provider_logo/", blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
    
    
class Contact(models.Model):
    firstName = models.CharField(max_length=100, blank=False)
    lastName = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=300, blank=False)
    mob_number = models.CharField(max_length = 20, blank=True, help_text='Contact phone number')
    message = models.TextField(blank=True)
    
    def __str__(self):
        return f"Message by {self.firstName +' ' +self.lastName}"
    
class Projects(models.Model):
    author_profile = models.ForeignKey(AuthorProfile, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=400)
    project_image = models.ImageField(upload_to='projects_images/', blank=True, null=True)
    github_link = models.URLField(max_length=600, blank=False)
    live_preview_link = models.URLField(max_length=600, blank=False)
    description = SummernoteTextField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    

class Repositories(models.Model):
    author_profile = models.ForeignKey(AuthorProfile, on_delete=models.CASCADE, related_name="repositories")
    repo_name = models.CharField(max_length=400, blank=False)
    repo_link = models.URLField(blank=True)
    
    
    def __str__(self):
        return self.repo_name

    
    
