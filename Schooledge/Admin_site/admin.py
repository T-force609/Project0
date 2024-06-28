from django.contrib import admin

# Register your models here.

class AdminSiteArea(admin.AdminSite):
    site_header ='Admin_site'


Admin_site = AdminSiteArea(name='Admin Site')