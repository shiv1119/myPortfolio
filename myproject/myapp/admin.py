
from django.contrib import admin
from .models import Post, Tag, AuthorProfile, WorkExperience, Education, Skill


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
class WorkExperienceInline(admin.TabularInline):
    model = WorkExperience
    extra = 1

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

@admin.register(AuthorProfile)
class AuthorProfileAdmin(admin.ModelAdmin):
    inlines = [WorkExperienceInline, EducationInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Skill)