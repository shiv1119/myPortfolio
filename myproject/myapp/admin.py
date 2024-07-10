
from django.contrib import admin
from .models import Post, Tag, AuthorProfile, WorkExperience, Education, TechnicalSkill, Certificate, Projects, SoftSkill, Repositories, Contact
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('title', 'content',)
    
@admin.register(Projects)
class ProjectsAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)       
    
    
@admin.register(WorkExperience)
class WorkExperienceAdmin(SummernoteModelAdmin):
    summernote_fields = ('activities_responsibilities',)   
    
@admin.register(Education)
class EducationAdmin(SummernoteModelAdmin):
    summernote_fields = ('activities_and_societies',)  
    
         
class WorkExperienceInline(admin.TabularInline):
    model = WorkExperience
    extra = 1

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1
    
class CertificateInline(admin.TabularInline):
    model = Certificate
    extra = 1
    
class ProjectsInline(admin.TabularInline):
    model = Projects
    extra = 1
    
class RepositoriesInline(admin.TabularInline):
    model = Repositories
    extra = 1

@admin.register(AuthorProfile)
class AuthorProfileAdmin(SummernoteModelAdmin):
    inlines = [WorkExperienceInline, EducationInline, CertificateInline, RepositoriesInline]
    summernote_fields = ('bio',)
    list_display = ('get_user_full_name', 'user_number', 'get_user_email')

    def get_user_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    get_user_full_name.short_description = 'Full Name'

    def get_user_email(self, obj):
        return obj.user.email
    get_user_email.short_description = 'User Email'


admin.site.register(Tag)
admin.site.register(TechnicalSkill)
admin.site.register(Certificate)
admin.site.register(SoftSkill)
admin.site.register(Repositories)
admin.site.register(Contact)


