from django.contrib import admin
from .models import ApplicantForm, ParentForm

# Register your models here.
admin.site.register(ApplicantForm)
admin.site.register(ParentForm)