from rest_framework import serializers
from .models import AuthorProfile, Certificate, Education, Projects, WorkExperience, SoftSkill, TechnicalSkill
from .models import AuthorProfile, Certificate, Education, Projects, WorkExperience

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class SoftSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftSkill
        fields = '__all__'

class TechnicalSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalSkill
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    soft_skills = SoftSkillSerializer(many=True, read_only=True)
    technical_skills = TechnicalSkillSerializer(many=True, read_only=True)
    class Meta:
        model = Education
        fields = '__all__'

class WorkExperienceSerializer(serializers.ModelSerializer):
    soft_skills = SoftSkillSerializer(many=True, read_only=True)
    technical_skills = TechnicalSkillSerializer(many=True, read_only=True)
    class Meta:
        model = WorkExperience
        fields = '__all__'


class AuthorProfileSerializer(serializers.ModelSerializer):
    certificates = CertificateSerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    work_experiences = WorkExperienceSerializer(many=True, read_only=True)
    soft_skills = SoftSkillSerializer(many=True, read_only=True)
    technical_skills = TechnicalSkillSerializer(many=True, read_only=True)

    class Meta:
        model = AuthorProfile
        fields = [
            'user', 'bio', 'profile_image', 'user_date_of_birth', 'user_gender',
            'technical_skills', 'soft_skills', 'github_username', 'portfolio_link',
            'user_number', 'user_linkedin', 'user_x', 'user_github', 
            'certificates', 'educations', 'projects', 'work_experiences'
        ]