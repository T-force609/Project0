from django.shortcuts import render, get_list_or_404
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def Admin(request):
    return render(request, 'Admin_site/admin.html',)
